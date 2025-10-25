import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidEncoder
from dotenv import load_dotenv

load_dotenv()

print("="*60)
print("PDF to Video Memory Converter")
print("="*60)

# Initialize encoder
encoder = MemvidEncoder()

# Check if pdfs folder exists
if not os.path.exists("pdfs"):
    os.makedirs("pdfs")
    print("\n✓ Created 'pdfs' folder")
    print("📁 Please add your PDF files to the 'pdfs' folder and run this script again.\n")
    exit(0)

# Find all PDF files
pdf_files = [f for f in os.listdir("pdfs") if f.endswith('.pdf')]

if not pdf_files:
    print("\n❌ No PDF files found in 'pdfs' folder")
    print("📁 Please add PDF files to the 'pdfs' folder and try again.\n")
    exit(1)

print(f"\n📚 Found {len(pdf_files)} PDF file(s):")
for pdf in pdf_files:
    print(f"  - {pdf}")

print("\n⏳ Processing PDFs...")

# Process each PDF
for pdf_file in pdf_files:
    pdf_path = os.path.join("pdfs", pdf_file)
    print(f"\n  Processing: {pdf_file}")
    
    try:
        # Add PDF to encoder (no metadata parameter supported)
        encoder.add_pdf(pdf_path)
        print(f"  ✓ Added: {pdf_file}")
    except Exception as e:
        print(f"  ✗ Error with {pdf_file}: {e}")

# Build video memory
print("\n⏳ Building video memory...")
encoder.build_video("pdf_library.mp4", "pdf_library_index.json")

print("\n" + "="*60)
print("✅ Success!")
print("="*60)
print(f"Created: pdf_library.mp4")
print(f"Created: pdf_library_index.json")
print(f"\nProcessed {len(pdf_files)} PDF file(s)")
print("\nNext steps:")
print("  1. Run: python search_pdfs.py")
print("  2. Or: python chat_pdfs.py")
print("="*60)
