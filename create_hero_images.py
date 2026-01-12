#!/usr/bin/env python
"""
Create professional hero/cover images for the one-page magazine design.
"""

from PIL import Image, ImageDraw, ImageFont
import os


def create_hero_images():
    os.makedirs("hero_images", exist_ok=True)

    def create_hero_gradient(filename, colors, title_text="Strategic Report"):
        img = Image.new("RGB", (1920, 800))
        draw = ImageDraw.Draw(img)

        width, height = img.size

        for y in range(height):
            r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * y / height)
            g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * y / height)
            b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * y / height)
            draw.line([(0, y), (width, y)], fill=(r, g, b))

        try:
            title_font = ImageFont.truetype("Arial", 80)
            subtitle_font = ImageFont.truetype("Arial", 30)
        except OSError:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()

        title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
        title_x = (width - title_bbox[2]) // 2
        title_y = 350

        draw.text((title_x, title_y), title_text, fill="white", font=title_font)

        subtitle_text = "Professional Analysis & Insights"
        subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
        subtitle_x = (width - subtitle_bbox[2]) // 2
        draw.text(
            (subtitle_x, 460),
            subtitle_text,
            fill=(255, 255, 255, 200),
            font=subtitle_font,
        )

        img.save(f"hero_images/{filename}", "PNG")
        print(f"✓ Created: {filename}")

    def create_geometric_pattern(filename, base_color, pattern_color):
        img = Image.new("RGB", (1920, 800), base_color)
        draw = ImageDraw.Draw(img)

        for i in range(0, 1920, 40):
            for j in range(0, 800, 40):
                if (i // 40 + j // 40) % 2 == 0:
                    draw.rectangle([i, j, i + 40, j + 40], fill=pattern_color)

        overlay = Image.new("RGBA", (1920, 800), (0, 0, 0, 100))
        img.paste(overlay, (0, 0), overlay)

        draw = ImageDraw.Draw(img)
        try:
            title_font = ImageFont.truetype("Arial", 80)
            subtitle_font = ImageFont.truetype("Arial", 30)
        except OSError:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()

        draw.text(
            (960, 350), "Strategic Insights", fill="white", font=title_font, anchor="mm"
        )
        draw.text(
            (960, 460),
            "Executive Report",
            fill=(255, 255, 255, 220),
            font=subtitle_font,
            anchor="mm",
        )

        img.save(f"hero_images/{filename}", "PNG")
        print(f"✓ Created: {filename}")

    def create_circle_pattern(filename):
        img = Image.new("RGB", (1920, 800), "#0a1628")
        draw = ImageDraw.Draw(img)

        for i in range(20):
            x = i * 100 + 50
            y = 400 + (i % 2) * 100
            radius = 150 - i * 5
            draw.ellipse(
                [x - radius, y - radius, x + radius, y + radius],
                outline="#722f37",
                width=2,
            )

        overlay = Image.new("RGBA", (1920, 800), (10, 22, 40, 200))
        img.paste(overlay, (0, 0), overlay)

        draw = ImageDraw.Draw(img)
        try:
            title_font = ImageFont.truetype("Arial", 80)
        except OSError:
            title_font = ImageFont.load_default()

        draw.text(
            (960, 400), "Annual Report 2024", fill="white", font=title_font, anchor="mm"
        )

        img.save(f"hero_images/{filename}", "PNG")
        print(f"✓ Created: {filename}")

    def create_minimal_hero(filename):
        img = Image.new("RGB", (1920, 800), "#f8f6f3")
        draw = ImageDraw.Draw(img)

        draw.rectangle([100, 100, 1820, 700], outline="#722f37", width=4)
        draw.rectangle([150, 150, 1770, 650], outline="#0a1628", width=2)

        try:
            title_font = ImageFont.truetype("Arial", 70)
            subtitle_font = ImageFont.truetype("Arial", 28)
        except OSError:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()

        draw.text(
            (960, 350),
            "Business Transformation",
            fill="#0a1628",
            font=title_font,
            anchor="mm",
        )
        draw.text(
            (960, 450),
            "Strategic Roadmap & Analysis",
            fill="#666666",
            font=subtitle_font,
            anchor="mm",
        )

        draw.line([(300, 520), (1620, 520)], fill="#c4a962", width=3)

        img.save(f"hero_images/{filename}", "PNG")
        print(f"✓ Created: {filename}")

    print("Creating hero images for magazine-style design...")

    create_hero_gradient(
        "hero_gradient_navy.png", [(10, 22, 40), (114, 47, 55)], "Strategic Analysis"
    )

    create_hero_gradient(
        "hero_gradient_gold.png", [(114, 47, 55), (196, 169, 98)], "Executive Insights"
    )

    create_geometric_pattern("hero_geometric.png", "#0a1628", "#1a2d45")

    create_circle_pattern("hero_circles.png")

    create_minimal_hero("hero_minimal.png")

    print("\n✓ All hero images created in 'hero_images/' directory")
    print("\n💡 Usage:")
    print("  Copy desired image to: hero_images/hero_custom.png")
    print("  Or specify custom path in conversion")


if __name__ == "__main__":
    create_hero_images()
