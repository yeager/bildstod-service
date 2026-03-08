#!/usr/bin/env python3
"""Convert SVG pictograms to PNG format using cairosvg"""

import cairosvg
import os
import sys
from pathlib import Path

def convert_svg_to_png(svg_file, png_file):
    """Convert a single SVG file to PNG"""
    try:
        cairosvg.svg2png(url=svg_file, write_to=png_file, output_width=500, output_height=500)
        print(f"✓ Converted {svg_file} -> {png_file}")
        return True
    except Exception as e:
        print(f"✗ Error converting {svg_file}: {e}")
        return False

def convert_batch(pictograms_dir):
    """Convert all SVG files in pictograms directory to PNG"""
    pictograms_path = Path(pictograms_dir)
    if not pictograms_path.exists():
        print(f"Directory {pictograms_dir} does not exist!")
        return

    svg_files = list(pictograms_path.glob("*.svg"))
    if not svg_files:
        print("No SVG files found!")
        return

    converted = 0
    total = len(svg_files)
    
    for svg_file in svg_files:
        png_file = svg_file.with_suffix('.png')
        if convert_svg_to_png(str(svg_file), str(png_file)):
            converted += 1
    
    print(f"\nConversion complete: {converted}/{total} files converted")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        convert_batch(sys.argv[1])
    else:
        convert_batch("/Users/bosse/.openclaw/workspace/bildstod-service/pictograms")