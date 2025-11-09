#!/usr/bin/env python3
"""
Extract questions from midterm-demo.docx
"""

from docx import Document

def extract_midterm_questions(docx_path):
    """Extract all text from the midterm demo document."""

    doc = Document(docx_path)

    full_text = []

    print("Extracting questions from midterm-demo.docx...")
    print("=" * 80)

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            full_text.append(text)
            print(text)

    print("=" * 80)

    return full_text

if __name__ == "__main__":
    questions = extract_midterm_questions("midterm-demo.docx")
    print(f"\nExtracted {len(questions)} paragraphs from the document.")
