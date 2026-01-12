#!/usr/bin/env python
"""
Create sample images for demonstration purposes.
"""

from PIL import Image, ImageDraw, ImageFont
import os


def create_sample_images():
    os.makedirs("sample_images", exist_ok=True)

    def create_chart_image(filename, title, color, bars):
        img = Image.new("RGB", (800, 400), color="white")
        draw = ImageDraw.Draw(img)

        draw.rectangle([0, 0, 799, 399], outline="#e0e0e0", width=2)

        draw.rectangle([50, 50, 750, 80], fill="#0a1628")
        draw.text((400, 60), title, fill="white", anchor="mm")

        bar_width = 100
        gap = 50
        start_x = 100

        for i, (label, value) in enumerate(bars):
            x = start_x + i * (bar_width + gap)
            height = value * 2.5
            y = 350 - height

            draw.rectangle([x, y, x + bar_width, 350], fill=color)
            draw.text((x + bar_width // 2, 370), label, fill="#4a4a4a", anchor="mm")
            draw.text(
                (x + bar_width // 2, y - 20), f"{value}%", fill="#1a1a1a", anchor="mm"
            )

        img.save(f"sample_images/{filename}", "PNG")
        print(f"✓ Created: {filename}")

    def create_icon_image(filename, color, icon_type):
        img = Image.new("RGB", (400, 400), color="white")
        draw = ImageDraw.Draw(img)

        draw.ellipse([50, 50, 350, 350], fill=color)
        draw.ellipse([100, 100, 300, 300], fill="white")

        if icon_type == "growth":
            draw.polygon([(200, 120), (160, 250), (240, 250)], fill=color)
        elif icon_type == "target":
            draw.ellipse([175, 175, 225, 225], fill=color)
            draw.ellipse([185, 185, 215, 215], fill="white")
            draw.ellipse([195, 195, 205, 205], fill=color)

        img.save(f"sample_images/{filename}", "PNG")
        print(f"✓ Created: {filename}")

    def create_diagram_image(filename):
        img = Image.new("RGB", (800, 500), color="white")
        draw = ImageDraw.Draw(img)

        colors = ["#0a1628", "#722f37", "#f8f6f3", "#4a4a4a"]

        boxes = [
            (100, 100, 250, 200, "Phase 1", colors[0]),
            (300, 100, 450, 200, "Phase 2", colors[1]),
            (500, 100, 650, 200, "Phase 3", colors[2]),
            (100, 300, 350, 400, "Foundation", colors[3]),
            (450, 300, 650, 400, "Scale", colors[3]),
        ]

        for x1, y1, x2, y2, label, color in boxes:
            draw.rectangle([x1, y1, x2, y2], fill=color, outline="#e0e0e0", width=2)
            draw.text(
                ((x1 + x2) // 2, (y1 + y2) // 2),
                label,
                fill="white" if color != "#f8f6f3" else "#1a1a1a",
                anchor="mm",
            )

        img.save(f"sample_images/{filename}", "PNG")
        print(f"✓ Created: {filename}")

    print("Creating sample images...")
    create_chart_image(
        "growth_chart.png",
        "Revenue Growth Rate",
        "#722f37",
        [("2021", 45), ("2022", 62), ("2023", 78), ("2024", 95)],
    )

    create_chart_image(
        "market_share.png",
        "Market Share by Region",
        "#0a1628",
        [("North", 35), ("Europe", 28), ("Asia", 25), ("Other", 12)],
    )

    create_icon_image("growth_icon.png", "#722f37", "growth")
    create_icon_image("target_icon.png", "#0a1628", "target")

    create_diagram_image("roadmap_diagram.png")

    print("\n✓ All sample images created in 'sample_images/' directory")


if __name__ == "__main__":
    create_sample_images()
