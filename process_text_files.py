import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidEncoder
from dotenv import load_dotenv

load_dotenv()

print("="*60)
print("Text Files to Video Memory Converter")
print("="*60)

# Initialize encoder
encoder = MemvidEncoder()

# Check if documents folder exists
if not os.path.exists("documents"):
    os.makedirs("documents")
    print("\n✓ Created 'documents' folder")
    print("📁 Please add your text files (.txt, .md) to the 'documents' folder and run this script again.\n")
    exit(0)

# Find all text files
text_files = [f for f in os.listdir("documents") 
              if f.endswith(('.txt', '.md', '.markdown'))]

if not text_files:
    print("\n❌ No text files found in 'documents' folder")
    print("📁 Please add .txt or .md files to the 'documents' folder and try again.\n")
    exit(1)

print(f"\n📚 Found {len(text_files)} text file(s):")
for file in text_files:
    print(f"  - {file}")

print("\n⏳ Processing files...")

# Process each file
total_chars = 0
all_chunks = []

for text_file in text_files:
    file_path = os.path.join("documents", text_file)
    print(f"\n  Processing: {text_file}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            total_chars += len(content)
            
        # Split content into chunks (approximately 500 chars each)
        chunk_size = 500
        for i in range(0, len(content), chunk_size):
            chunk = content[i:i+chunk_size]
            # Add source filename to the chunk
            chunk_with_source = f"[Source: {text_file}]\n{chunk}"
            all_chunks.append(chunk_with_source)
            
        print(f"  ✓ Added: {text_file} ({len(content)} characters)")
    except Exception as e:
        print(f"  ✗ Error with {text_file}: {e}")

# Add all chunks to encoder
if all_chunks:
    encoder.add_chunks(all_chunks)

# Build video memory
print("\n⏳ Building video memory...")
encoder.build_video("documents_library.mp4", "documents_library_index.json")

print("\n" + "="*60)
print("✅ Success!")
print("="*60)
print(f"Created: documents_library.mp4")
print(f"Created: documents_library_index.json")
print(f"\nProcessed {len(text_files)} file(s)")
print(f"Total content: {total_chars:,} characters")
print("\nNext steps:")
print("  1. Run: python search_documents.py")
print("  2. Or: python chat_documents.py")
print("="*60)
