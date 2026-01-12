#!/usr/bin/env python
"""
Example script demonstrating how to use ppt-to-web.

Usage:
    uv run python example.py
"""

from ppt_to_web import ppt_to_yaml, yaml_to_html


def main():
    print("PPT-to-Web Example")
    print("=" * 40)

    # Step 1: Convert PPTX to YAML
    # pptx_file = "example.pptx"
    # output_dir = "./output"
    #
    # print(f"\nConverting {pptx_file} to YAML...")
    # yaml_path = ppt_to_yaml(pptx_file, output_dir)
    # print(f"✓ YAML file created: {yaml_path}")
    #
    # # Step 2: Convert YAML to HTML
    # print(f"\nConverting YAML to HTML...")
    # html_path = yaml_to_html(yaml_path, output_dir)
    # print(f"✓ HTML file created: {html_path}")

    print("\nTo use this script:")
    print("1. Place a .pptx file in the project directory")
    print("2. Uncomment the lines above")
    print("3. Update pptx_file to match your file name")
    print("4. Run: uv run python example.py")

    print("\nOr use the CLI:")
    print("  ppt-to-web run presentation.pptx --output ./output")


if __name__ == "__main__":
    main()
