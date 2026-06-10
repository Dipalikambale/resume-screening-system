print("Step 1")

from extractor import extract_text_from_pdf

print("Step 2")

text = extract_text_from_pdf("DIPALI KAMBALE RESUME.pdf")

print("Step 3")

print("Length:", len(text))

print(text[:500])

print("Step 4")