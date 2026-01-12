#!/usr/bin/env python
"""
Quick start demo script for PPT-to-Web.

This script demonstrates the complete workflow:
1. Create sample images
2. Create sample PowerPoint presentation
3. Convert PPTX to YAML
4. Convert YAML to HTML
5. Open the result in browser

Usage:
    PYTHONPATH=src uv run python quick_start.py
"""

import subprocess
import sys
import webbrowser
from pathlib import Path


def run_command(cmd, description):
    """Run a command and print the result."""
    print(f"\n{description}...")
    result = subprocess.run(cmd, shell=True, capture_output=False)
    if result.returncode != 0:
        print(f"✗ Failed: {description}")
        return False
    print(f"✓ {description} completed")
    return True


def main():
    print("=" * 60)
    print("PPT-to-Web Quick Start Demo")
    print("=" * 60)

    commands = [
        ("uv run python create_sample_images.py", "Step 1: Creating sample images"),
        ("uv run python create_sample_ppt.py", "Step 2: Creating sample presentation"),
        (
            "PYTHONPATH=src uv run python test_conversion.py",
            "Step 3: Converting to web page",
        ),
    ]

    for cmd, desc in commands:
        if not run_command(cmd, desc):
            print(f"\n✗ Demo failed at: {desc}")
            sys.exit(1)

    print("\n" + "=" * 60)
    print("✓ Demo Complete!")
    print("=" * 60)

    html_path = Path("output/sample_presentation.html")
    if html_path.exists():
        print(f"\n📊 Generated files:")
        print(f"   • {html_path}")
        print(f"   • output/sample_presentation.yaml")
        print(f"   • output/media/ (5 images)")

        print(f"\n🌐 Opening in browser...")
        try:
            webbrowser.open(f"file://{html_path.absolute()}")
        except Exception as e:
            print(f"Could not open browser: {e}")
            print(f"Please open manually: {html_path.absolute()}")

        print(f"\n💡 Next steps:")
        print(f"   1. Review the generated web page")
        print(f"   2. Check output/sample_presentation.yaml for extracted data")
        print(f"   3. Create your own PPTX and convert it!")
        print(f"   4. Read USER_GUIDE.md for detailed documentation")
    else:
        print(f"\n✗ HTML file not found at {html_path}")


if __name__ == "__main__":
    main()
