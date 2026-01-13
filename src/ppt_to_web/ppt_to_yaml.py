import shutil
import subprocess
from pathlib import Path

import yaml
from pptx import Presentation
from pptx.enum.chart import XL_CHART_TYPE


def _extract_text_from_shape(shape) -> str:
    if not shape.has_text_frame:
        return ""
    return "\n".join(
        [run.text for para in shape.text_frame.paragraphs for run in para.runs]
    )


def _is_highlighted(shape) -> bool:
    return hasattr(shape, "fill") and shape.fill.type != 0


def _map_chart_type(chart_type: XL_CHART_TYPE) -> str:
    """Map python-pptx XL_CHART_TYPE to ECharts chart type string."""
    chart_type_mapping = {
        # Bar charts (horizontal bars in PowerPoint)
        XL_CHART_TYPE.BAR_CLUSTERED: "bar",
        XL_CHART_TYPE.BAR_STACKED: "bar",
        XL_CHART_TYPE.BAR_STACKED_100: "bar",
        # Column charts (vertical bars - most common)
        XL_CHART_TYPE.COLUMN_CLUSTERED: "bar",
        XL_CHART_TYPE.COLUMN_STACKED: "bar",
        XL_CHART_TYPE.COLUMN_STACKED_100: "bar",
        # Line charts
        XL_CHART_TYPE.LINE: "line",
        XL_CHART_TYPE.LINE_MARKERS: "line",
        XL_CHART_TYPE.LINE_STACKED: "line",
        XL_CHART_TYPE.LINE_STACKED_100: "line",
        XL_CHART_TYPE.LINE_MARKERS_STACKED: "line",
        XL_CHART_TYPE.LINE_MARKERS_STACKED_100: "line",
        # Pie charts
        XL_CHART_TYPE.PIE: "pie",
        XL_CHART_TYPE.PIE_EXPLODED: "pie",
        XL_CHART_TYPE.DOUGHNUT: "pie",
        XL_CHART_TYPE.DOUGHNUT_EXPLODED: "pie",
        # Area charts (ECharts line with areaStyle)
        XL_CHART_TYPE.AREA: "line",
        XL_CHART_TYPE.AREA_STACKED: "line",
        XL_CHART_TYPE.AREA_STACKED_100: "line",
        # Scatter/XY charts
        XL_CHART_TYPE.XY_SCATTER: "scatter",
        XL_CHART_TYPE.XY_SCATTER_LINES: "scatter",
        XL_CHART_TYPE.XY_SCATTER_LINES_NO_MARKERS: "scatter",
        XL_CHART_TYPE.XY_SCATTER_SMOOTH: "scatter",
        XL_CHART_TYPE.XY_SCATTER_SMOOTH_NO_MARKERS: "scatter",
        # Radar charts
        XL_CHART_TYPE.RADAR: "radar",
        XL_CHART_TYPE.RADAR_FILLED: "radar",
        XL_CHART_TYPE.RADAR_MARKERS: "radar",
    }
    return chart_type_mapping.get(chart_type, "bar")


def _extract_chart(shape, slide_idx: int, shape_idx: int) -> dict | None:
    """Extract chart data from a shape containing a chart."""
    if not shape.has_chart:
        return None

    try:
        chart = shape.chart
        chart_type_enum = chart.chart_type
        echarts_type = _map_chart_type(chart_type_enum)

        # Extract chart title
        title = ""
        if chart.has_title:
            try:
                title = chart.chart_title.text_frame.text
            except Exception:
                pass

        # Extract categories (x-axis labels)
        categories = []
        try:
            if chart.plots:
                plot_categories = chart.plots[0].categories
                if plot_categories:
                    categories = [str(cat) for cat in plot_categories]
        except Exception as e:
            print(f"Warning: Could not extract categories: {e}")

        # Extract series data
        series_data = []
        for series in chart.series:
            # Ensure series name is a plain string
            series_name = str(series.name) if series.name else f"Series {len(series_data) + 1}"
            series_values = []
            try:
                if series.values:
                    # Convert values to plain Python floats/ints
                    series_values = [float(v) if v is not None else 0 for v in series.values]
            except Exception:
                pass

            series_data.append({
                "name": series_name,
                "data": series_values,
            })

        # Skip empty charts
        if not series_data or all(not s["data"] for s in series_data):
            return None

        # Determine chart properties
        is_stacked = "STACKED" in chart_type_enum.name
        is_horizontal = chart_type_enum in {
            XL_CHART_TYPE.BAR_CLUSTERED,
            XL_CHART_TYPE.BAR_STACKED,
            XL_CHART_TYPE.BAR_STACKED_100,
        }
        is_area = "AREA" in chart_type_enum.name

        chart_data = {
            "type": "chart",
            "chart_type": echarts_type,
            "title": title,
            "categories": categories,
            "series": series_data,
            "is_stacked": is_stacked,
            "is_horizontal": is_horizontal,
            "is_area": is_area,
            "chart_id": f"chart_{slide_idx}_{shape_idx}",
        }

        return chart_data

    except Exception as e:
        print(f"Warning: Failed to extract chart from slide {slide_idx}, shape {shape_idx}: {e}")
        return None


def _extract_media(
    shape, slide_idx: int, shape_idx: int, media_dir: Path
) -> str | None:
    if not hasattr(shape, "image"):
        return None

    try:
        image_bytes = shape.image.blob
        ext = shape.image.ext.lower()

        # Web-friendly formats that don't need conversion
        web_formats = {"png", "jpg", "jpeg", "gif", "webp", "svg"}

        # If format is already web-friendly, save directly
        if ext in web_formats:
            filename = f"slide_{slide_idx}_shape_{shape_idx}.{ext}"
            filepath = media_dir / filename
            with open(filepath, "wb") as f:
                f.write(image_bytes)
            return f"media/{filename}"

        # Save original file first
        original_filename = f"slide_{slide_idx}_shape_{shape_idx}.{ext}"
        original_filepath = media_dir / original_filename
        with open(original_filepath, "wb") as f:
            f.write(image_bytes)

        png_filename = f"slide_{slide_idx}_shape_{shape_idx}.png"
        png_filepath = media_dir / png_filename

        # Try LibreOffice conversion first (best for WMF/EMF)
        soffice_path = shutil.which("soffice") or "/opt/homebrew/bin/soffice"
        if Path(soffice_path).exists():
            try:
                result = subprocess.run(
                    [
                        soffice_path,
                        "--headless",
                        "--convert-to",
                        "png",
                        "--outdir",
                        str(media_dir),
                        str(original_filepath),
                    ],
                    capture_output=True,
                    timeout=30,
                )
                if result.returncode == 0 and png_filepath.exists():
                    original_filepath.unlink()
                    return f"media/{png_filename}"
            except (subprocess.TimeoutExpired, FileNotFoundError):
                pass

        # Try ImageMagick as fallback
        try:
            result = subprocess.run(
                ["magick", str(original_filepath), str(png_filepath)],
                capture_output=True,
                timeout=30,
            )
            if result.returncode == 0 and png_filepath.exists():
                original_filepath.unlink()
                return f"media/{png_filename}"
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

        # Try Pillow as last fallback
        try:
            from PIL import Image
            import io

            img = Image.open(io.BytesIO(image_bytes))
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.save(png_filepath, "PNG")
            original_filepath.unlink()
            return f"media/{png_filename}"
        except Exception:
            pass

        # All conversion failed, keep original
        return f"media/{original_filename}"

    except Exception as e:
        print(f"Warning: Failed to extract media from slide {slide_idx}, shape {shape_idx}: {e}")
        return None


def ppt_to_yaml(pptx_path: str, yaml_output_dir: str) -> str:
    pptx_file = Path(pptx_path)
    yaml_dir = Path(yaml_output_dir)
    yaml_dir.mkdir(parents=True, exist_ok=True)

    media_dir = yaml_dir / "media"
    media_dir.mkdir(parents=True, exist_ok=True)

    prs = Presentation(str(pptx_file))

    slides_data = []
    highlighted_sections = []

    for slide_idx, slide in enumerate(prs.slides):
        slide_data = {
            "slide_number": slide_idx + 1,
            "title": "",
            "content": [],
            "media": [],
            "is_highlighted": False,
            "layout": slide.slide_layout.name if slide.slide_layout else "",
        }

        for shape_idx, shape in enumerate(slide.shapes):
            if shape.has_text_frame:
                text = _extract_text_from_shape(shape).strip()
                if text:
                    if shape_idx == 0 and not slide_data["title"]:
                        slide_data["title"] = text
                    else:
                        slide_data["content"].append({"type": "text", "value": text})

            # Check for chart BEFORE image (charts may also have image representations)
            if shape.has_chart:
                chart_data = _extract_chart(shape, slide_idx, shape_idx)
                if chart_data:
                    slide_data["media"].append(chart_data)
            elif hasattr(shape, "image"):
                media_path = _extract_media(shape, slide_idx, shape_idx, media_dir)
                if media_path:
                    slide_data["media"].append({"type": "image", "path": media_path})

            if _is_highlighted(shape):
                slide_data["is_highlighted"] = True

        if slide_data["title"] or slide_data["content"] or slide_data["media"]:
            slides_data.append(slide_data)
            if slide_data["is_highlighted"]:
                highlighted_sections.append(
                    {
                        "slide_number": slide_idx + 1,
                        "title": slide_data["title"],
                        "content": slide_data["content"][:3],
                    }
                )

    # Extract cover title from first slide
    cover_title = pptx_file.stem
    if slides_data and slides_data[0].get("title"):
        cover_title = slides_data[0]["title"].replace("\n", " ").strip()

    output_data = {
        "title": pptx_file.stem,
        "cover_title": cover_title,
        "hero_image": None,
        "slides": slides_data,
        "highlighted_sections": highlighted_sections,
        "total_slides": len(slides_data),
    }

    yaml_path = yaml_dir / f"{pptx_file.stem}.yaml"
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(
            output_data,
            f,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
        )

    return str(yaml_path)
