"""
CSS Extractor
------------
Extracts inline CSS from HTML files into separate CSS files.
Creates a css directory and updates HTML files with proper link tags.

Usage:
python css_extractor.py file1.html file2.html file3.html
"""

import os
import sys
from bs4 import BeautifulSoup
from pathlib import Path

class CSSExtractor:
    def __init__(self):
        # Create css directory if it doesn't exist
        self.css_dir = 'css'
        if not os.path.exists(self.css_dir):
            os.makedirs(self.css_dir)
            print(f"Created directory: {self.css_dir}/")

    def process_html_file(self, html_file):
        """Process a single HTML file to extract CSS."""
        try:
            # Read the HTML file
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

            # Find the style tag
            style_tag = soup.find('style')
            if not style_tag:
                print(f"No style tag found in {html_file}")
                return False

            # Extract CSS content
            css_content = style_tag.string

            # Create CSS filename based on HTML filename
            css_filename = html_file.replace('.html', '.css')
            css_path = os.path.join(self.css_dir, os.path.basename(css_filename))

            # Write CSS to file
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css_content)
            print(f"Created: {css_path}")

            # Remove style tag
            style_tag.decompose()

            # Add link tag
            head_tag = soup.find('head')
            if head_tag:
                link_tag = soup.new_tag('link', 
                                      rel='stylesheet',
                                      href=f'css/{os.path.basename(css_filename)}?v=1.0.0')
                head_tag.append(link_tag)

                # Write modified HTML
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(str(soup.prettify()))
                print(f"Updated: {html_file}")
                return True

            print(f"No head tag found in {html_file}")
            return False

        except Exception as e:
            print(f"Error processing {html_file}: {str(e)}")
            return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python css_extractor.py file1.html file2.html ...")
        print("Example: python css_extractor.py index.html contact.html")
        return

    extractor = CSSExtractor()
    html_files = sys.argv[1:]
    
    print("\nProcessing HTML files...")
    for html_file in html_files:
        if os.path.exists(html_file):
            print(f"\nProcessing: {html_file}")
            extractor.process_html_file(html_file)
        else:
            print(f"\nFile not found: {html_file}")

if __name__ == "__main__":
    main()