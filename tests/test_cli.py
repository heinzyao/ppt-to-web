"""Tests for CLI commands."""

from unittest.mock import patch

from click.testing import CliRunner

from ppt_to_web.cli import cli


class TestCli:
    def test_cli_group_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Convert PowerPoint" in result.output

    @patch("ppt_to_web.cli.ppt_to_yaml")
    def test_convert_command(self, mock_convert, tmp_path):
        pptx_file = tmp_path / "test.pptx"
        pptx_file.touch()
        mock_convert.return_value = str(tmp_path / "output" / "test.yaml")

        runner = CliRunner()
        result = runner.invoke(cli, ["convert", str(pptx_file)])
        assert result.exit_code == 0
        assert "YAML file created" in result.output
        mock_convert.assert_called_once()

    @patch("ppt_to_web.cli.yaml_to_html")
    def test_build_command(self, mock_build, tmp_path):
        yaml_file = tmp_path / "test.yaml"
        yaml_file.touch()
        mock_build.return_value = str(tmp_path / "output" / "test.html")

        runner = CliRunner()
        result = runner.invoke(cli, ["build", str(yaml_file)])
        assert result.exit_code == 0
        assert "HTML file created" in result.output
        mock_build.assert_called_once()

    @patch("ppt_to_web.cli.yaml_to_html")
    @patch("ppt_to_web.cli.ppt_to_yaml")
    def test_run_command(self, mock_convert, mock_build, tmp_path):
        pptx_file = tmp_path / "test.pptx"
        pptx_file.touch()
        mock_convert.return_value = str(tmp_path / "output" / "test.yaml")
        mock_build.return_value = str(tmp_path / "output" / "test.html")

        runner = CliRunner()
        result = runner.invoke(cli, ["run", str(pptx_file)])
        assert result.exit_code == 0
        assert "Conversion complete" in result.output
        mock_convert.assert_called_once()
        mock_build.assert_called_once()

    @patch("ppt_to_web.cli.yaml_to_html")
    def test_build_custom_template(self, mock_build, tmp_path):
        yaml_file = tmp_path / "test.yaml"
        yaml_file.touch()
        mock_build.return_value = str(tmp_path / "output" / "test.html")

        runner = CliRunner()
        result = runner.invoke(cli, ["build", str(yaml_file), "-t", "cover_story.html"])
        assert result.exit_code == 0
        mock_build.assert_called_once_with(str(yaml_file), "./output", "cover_story.html")

    def test_convert_missing_file(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["convert", "nonexistent.pptx"])
        assert result.exit_code != 0
