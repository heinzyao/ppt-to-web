"""Tests for yaml_to_html module."""

import yaml

from ppt_to_web.yaml_to_html import _create_html_env, yaml_to_html


class TestCreateHtmlEnv:
    def test_returns_jinja_env(self):
        env = _create_html_env()
        assert env is not None
        assert env.autoescape is True

    def test_tojson_filter(self):
        env = _create_html_env()
        assert "tojson" in env.filters
        result = env.filters["tojson"]({"key": "值"})
        assert '"key"' in result
        assert '"值"' in result  # ensure_ascii=False

    def test_templates_loadable(self):
        env = _create_html_env()
        template = env.get_template("index.html")
        assert template is not None

    def test_cover_story_loadable(self):
        env = _create_html_env()
        template = env.get_template("cover_story.html")
        assert template is not None


class TestYamlToHtml:
    def _make_yaml(self, tmp_path, data):
        tmp_path.mkdir(parents=True, exist_ok=True)
        yaml_path = tmp_path / "test.yaml"
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True)
        return str(yaml_path)

    def _sample_data(self):
        return {
            "title": "test_presentation",
            "cover_title": "Test Title",
            "hero_image": None,
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Slide 1",
                    "content": [{"type": "text", "value": "Hello World"}],
                    "media": [],
                    "is_highlighted": False,
                    "layout": "Title Slide",
                }
            ],
            "highlighted_sections": [],
            "total_slides": 1,
        }

    def test_creates_html_file(self, tmp_path):
        data = self._sample_data()
        yaml_path = self._make_yaml(tmp_path / "yaml_dir", data)
        output_dir = tmp_path / "html_output"

        html_path = yaml_to_html(yaml_path, str(output_dir))
        assert html_path.endswith(".html")
        with open(html_path) as f:
            content = f.read()
        assert "Hello World" in content

    def test_custom_output_filename(self, tmp_path):
        data = self._sample_data()
        yaml_path = self._make_yaml(tmp_path / "yaml_dir", data)
        output_dir = tmp_path / "html_output"

        html_path = yaml_to_html(yaml_path, str(output_dir), output_filename="custom.html")
        assert html_path.endswith("custom.html")

    def test_cover_story_template(self, tmp_path):
        data = self._sample_data()
        yaml_path = self._make_yaml(tmp_path / "yaml_dir", data)
        output_dir = tmp_path / "html_output"

        html_path = yaml_to_html(yaml_path, str(output_dir), template_name="cover_story.html")
        assert html_path.endswith(".html")
        with open(html_path) as f:
            content = f.read()
        assert len(content) > 0

    def test_copies_media_directory(self, tmp_path):
        data = self._sample_data()
        yaml_dir = tmp_path / "yaml_dir"
        yaml_path = self._make_yaml(yaml_dir, data)

        # Create a fake media file
        media_dir = yaml_dir / "media"
        media_dir.mkdir()
        (media_dir / "test_image.png").write_bytes(b"fake png")

        output_dir = tmp_path / "html_output"
        yaml_to_html(yaml_path, str(output_dir))

        assert (output_dir / "media" / "test_image.png").exists()

    def test_no_media_dir_ok(self, tmp_path):
        data = self._sample_data()
        yaml_dir = tmp_path / "yaml_dir"
        yaml_path = self._make_yaml(yaml_dir, data)
        output_dir = tmp_path / "html_output"

        # Should not raise even without media dir
        html_path = yaml_to_html(yaml_path, str(output_dir))
        assert html_path.endswith(".html")

    def test_chinese_content(self, tmp_path):
        data = self._sample_data()
        data["slides"][0]["content"][0]["value"] = "這是中文內容"
        yaml_path = self._make_yaml(tmp_path / "yaml_dir", data)
        output_dir = tmp_path / "html_output"

        html_path = yaml_to_html(yaml_path, str(output_dir))
        with open(html_path, encoding="utf-8") as f:
            content = f.read()
        assert "這是中文內容" in content

    def test_with_chart_data(self, tmp_path):
        data = self._sample_data()
        data["slides"][0]["media"] = [
            {
                "type": "chart",
                "chart_type": "bar",
                "title": "Revenue",
                "categories": ["Q1", "Q2"],
                "series": [{"name": "Sales", "data": [10, 20]}],
                "is_stacked": False,
                "is_horizontal": False,
                "is_area": False,
                "chart_id": "chart_0_0",
            }
        ]
        yaml_path = self._make_yaml(tmp_path / "yaml_dir", data)
        output_dir = tmp_path / "html_output"

        # Use cover_story which supports charts
        html_path = yaml_to_html(yaml_path, str(output_dir), template_name="cover_story.html")
        with open(html_path, encoding="utf-8") as f:
            content = f.read()
        assert "chart_0_0" in content
