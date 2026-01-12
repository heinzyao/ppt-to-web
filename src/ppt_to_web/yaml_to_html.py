import os
from pathlib import Path
from typing import Dict, List, Any
from jinja2 import Environment, FileSystemLoader


def _create_html_env() -> Environment:
    template_dir = Path(__file__).parent.parent / "templates"
    return Environment(loader=FileSystemLoader(template_dir), autoescape=True)


def yaml_to_html(
    yaml_path: str,
    html_output_dir: str,
    template_name: str = "index.html",
    output_filename: str | None = None,
) -> str:
    import yaml

    yaml_file = Path(yaml_path)
    html_dir = Path(html_output_dir)
    html_dir.mkdir(parents=True, exist_ok=True)

    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    env = _create_html_env()
    template = env.get_template(template_name)

    html_content = template.render(data=data)

    if output_filename:
        html_output_path = html_dir / output_filename
    else:
        html_output_path = html_dir / f"{data['title']}.html"

    with open(html_output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    media_dir = yaml_file.parent / "media"
    if media_dir.exists():
        output_media_dir = html_dir / "media"
        output_media_dir.mkdir(exist_ok=True)

        for media_file in media_dir.iterdir():
            if media_file.is_file():
                import shutil

                src = media_file
                dst = output_media_dir / media_file.name
                if src != dst:
                    shutil.copy2(src, dst)

    return str(html_output_path)
