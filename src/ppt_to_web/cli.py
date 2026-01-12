import click
from pathlib import Path
from ppt_to_web import ppt_to_yaml, yaml_to_html


@click.group()
def cli():
    """Convert PowerPoint presentations to professional web pages."""
    pass


@cli.command()
@click.argument("pptx_path", type=click.Path(exists=True))
@click.option(
    "--output", "-o", default="./output", help="Output directory for YAML files"
)
def convert(pptx_path: str, output: str):
    """Convert PPTX to YAML format."""
    yaml_path = ppt_to_yaml(pptx_path, output)
    click.echo(f"YAML file created: {yaml_path}")


@cli.command()
@click.argument("yaml_path", type=click.Path(exists=True))
@click.option(
    "--output", "-o", default="./output", help="Output directory for HTML files"
)
@click.option("--template", "-t", default="index.html", help="HTML template to use")
def build(yaml_path: str, output: str, template: str):
    """Convert YAML to HTML web page."""
    html_path = yaml_to_html(yaml_path, output, template)
    click.echo(f"HTML file created: {html_path}")


@cli.command()
@click.argument("pptx_path", type=click.Path(exists=True))
@click.option("--output", "-o", default="./output", help="Output directory")
@click.option("--template", "-t", default="index.html", help="HTML template to use")
def run(pptx_path: str, output: str, template: str):
    """Convert PPTX to HTML in one step."""
    click.echo(f"Converting {pptx_path} to YAML...")
    yaml_path = ppt_to_yaml(pptx_path, output)
    click.echo(f"YAML file created: {yaml_path}")

    click.echo(f"Converting YAML to HTML...")
    html_path = yaml_to_html(yaml_path, output, template)
    click.echo(f"HTML file created: {html_path}")

    click.echo("\nConversion complete!")
    click.echo(f"Open {html_path} in your browser to view the result.")


if __name__ == "__main__":
    cli()
