# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2026-01-28

### Added
- Multi-agent collaboration documentation (`AGENTS.md`)
- This changelog file

### Changed
- Updated `README.md` with collaboration reference

## [0.1.0] - 2026-01-07

### Added
- Initial release
- PPTX to YAML conversion with `python-pptx`
- YAML to HTML rendering with Jinja2
- Chart extraction and ECharts conversion
  - Support for bar, line, pie, scatter, radar charts
- Image processing with Wand (ImageMagick)
- WMF/EMF vector image conversion via LibreOffice
- Smart image processing:
  - Auto-trim whitespace
  - Aspect ratio detection (landscape/portrait/square)
  - Portrait images with text wrapping
- CLI interface with Click
  - `convert`: PPTX → YAML
  - `build`: YAML → HTML
  - `run`: One-step conversion
- Two HTML templates:
  - `cover_story.html`: Magazine cover story style
  - `index.html`: Clean two-column layout
- Responsive web design
- Hero image support for cover pages
