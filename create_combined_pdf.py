#!/usr/bin/env python3
"""
Create combined PDF: All course slides + sample midterm solutions
"""

from PyPDF2 import PdfMerger

def create_combined_pdf():
    """Merge course slides and midterm solutions into one comprehensive PDF."""

    files_to_merge = [
        "adv_db_merged_slides.pdf",
        "midterm_sample_solutions.pdf"
    ]

    output_file = "adv_db_merged_with_sample.pdf"

    print("Creating combined PDF...")
    print("-" * 60)

    merger = PdfMerger()

    for pdf_file in files_to_merge:
        print(f"Adding: {pdf_file}")
        merger.append(pdf_file)

    merger.write(output_file)
    merger.close()

    print("-" * 60)
    print(f"\n✓ Successfully created: {output_file}")
    print(f"\nThis file contains:")
    print(f"  1. All course slides (169 pages)")
    print(f"  2. Sample midterm questions & solutions")
    print(f"\nYou now have:")
    print(f"  • adv_db_merged_slides.pdf (course slides only)")
    print(f"  • midterm_sample_solutions.pdf (sample exam only)")
    print(f"  • adv_db_merged_with_sample.pdf (everything combined)")

if __name__ == "__main__":
    create_combined_pdf()
