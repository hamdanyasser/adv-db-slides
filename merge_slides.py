#!/usr/bin/env python3
"""
Merge all Advanced Database course slides into one PDF.
"""

from PyPDF2 import PdfMerger
import os

def merge_pdf_slides():
    """Merge all course slides in logical order."""

    # Define slide files in the desired order
    slide_files = [
        "Ch01_The Basics.pdf",
        "Ch02_Database Administration (1).pdf",
        "Ch03_psql.pdf",
        "Ch04_pgadmin.pdf",
        "Ch05_Data Types.pdf",
        "Ch05_Full Text Search.pdf"
    ]

    # Output file
    output_file = "adv_db_merged_slides.pdf"

    # Create PDF merger
    merger = PdfMerger()

    total_pages = 0
    files_merged = []

    print("Merging PDF slides...")
    print("-" * 60)

    for pdf_file in slide_files:
        if os.path.exists(pdf_file):
            print(f"Adding: {pdf_file}")
            merger.append(pdf_file)
            files_merged.append(pdf_file)

            # Count pages
            from PyPDF2 import PdfReader
            reader = PdfReader(pdf_file)
            page_count = len(reader.pages)
            total_pages += page_count
            print(f"  → {page_count} pages")
        else:
            print(f"Skipping (not found): {pdf_file}")

    print("-" * 60)

    # Write merged PDF
    merger.write(output_file)
    merger.close()

    print(f"\n✓ Successfully created: {output_file}")
    print(f"  Total pages: {total_pages}")
    print(f"  Files merged: {len(files_merged)}")

    return output_file, total_pages

if __name__ == "__main__":
    merge_pdf_slides()
