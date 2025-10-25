import os
os.environ['USE_TF'] = 'NO'

from memvid import MemvidRetriever

print("="*60)
print("Testing ROSEN.pdf Search")
print("="*60)

retriever = MemvidRetriever("pdf_library.mp4", "pdf_library_index.json")

# Test queries - adjust these based on what you expect in the PDF
test_queries = [
    "What is this document about?",
    "main topics",
    "summary",
]

for query in test_queries:
    print(f"\n{'='*60}")
    print(f"🔍 Query: {query}")
    print('='*60)
    
    results = retriever.search(query, top_k=3)
    
    for i, result in enumerate(results, 1):
        # Result is just a string
        if isinstance(result, str):
            text = result
        else:
            text = result.get('text', result)
        
        print(f"\n📄 Result {i}")
        # Show first 300 characters
        preview = text[:300] if len(text) > 300 else text
        print(f"   {preview}...")
        print("-"*60)

print("\n✅ PDF search test complete!")
print("\nTry interactive search: python search_pdfs.py")
print("Or chat: python chat_pdfs.py")
