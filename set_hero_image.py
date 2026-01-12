#!/usr/bin/env python
"""
Add or modify hero image in YAML configuration.

Usage:
    uv run python set_hero_image.py hero_gradient_navy.png
    uv run python set_hero_image.py --list
"""

import yaml
from pathlib import Path
import sys


def list_available_hero_images():
    """List available hero images."""
    hero_dir = Path("hero_images")
    if not hero_dir.exists():
        print("No hero_images directory found.")
        return []

    images = list(hero_dir.glob("*.png")) + list(hero_dir.glob("*.jpg"))
    if not images:
        print("No hero images found in hero_images/ directory.")
        return []

    print("\nAvailable hero images:")
    print("=" * 50)
    for i, img in enumerate(images, 1):
        print(f"  {i}. {img.name}")
        size = img.stat().st_size / 1024
        print(f"     Size: {size:.1f} KB")
    print("=" * 50)
    return images


def set_hero_image(yaml_path: str, hero_image: str | None = None):
    """Set or remove hero image in YAML configuration."""
    yaml_file = Path(yaml_path)

    if not yaml_file.exists():
        print(f"✗ YAML file not found: {yaml_file}")
        return False

    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if hero_image is None:
        data["hero_image"] = None
        print("✓ Hero image removed")
    else:
        hero_path = Path(hero_image)

        if not hero_path.exists():
            print(f"✗ Image not found: {hero_path}")
            return False

        data["hero_image"] = str(hero_path)
        print(f"✓ Hero image set: {hero_path}")
        print(f"  Size: {hero_path.stat().st_size / 1024:.1f} KB")

    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
        )

    return True


def main():
    if "--list" in sys.argv or "-l" in sys.argv:
        list_available_hero_images()
        return

    if "--remove" in sys.argv or "-r" in sys.argv:
        yaml_file = "output/sample_presentation.yaml"
        set_hero_image(yaml_file, None)
        return

    if len(sys.argv) > 1:
        hero_image = sys.argv[1]
        yaml_file = "output/sample_presentation.yaml"

        hero_path = Path(hero_image)
        if not hero_path.exists():
            hero_path = Path("hero_images") / hero_image

        if set_hero_image(yaml_file, str(hero_path)):
            print(f"\n💡 Now regenerate HTML to see the hero image:")
            print(f"   PYTHONPATH=src uv run python test_onepage.py")
    else:
        print("Usage:")
        print("  uv run python set_hero_image.py <hero_image.png>  # Set hero image")
        print(
            "  uv run python set_hero_image.py --list           # List available images"
        )
        print("  uv run python set_hero_image.py --remove         # Remove hero image")
        print()
        print("Examples:")
        list_available_hero_images()


if __name__ == "__main__":
    main()
