import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidRetriever

# Check if PDF library exists
if not os.path.exists("pdf_library.mp4"):
    print("❌ PDF library not found!")
    print("Please run 'python process_pdf.py' first to create the library.\n")
    exit(1)

print("="*60)
print("PDF Library Search")
print("="*60)

# Initialize retriever
retriever = MemvidRetriever("pdf_library.mp4", "pdf_library_index.json")

# Interactive search
print("\nSearch your PDF library (type 'quit' to exit)")
print("-"*60)

while True:
    query = input("\nSearch query: ").strip()
    
    if query.lower() in ['quit', 'exit', 'q']:
        print("\nGoodbye!")
        break
        
    if not query:
        continue
    
    print(f"\n🔍 Searching for: '{query}'")
    print("="*60)
    
    # Search with top 5 results
    results = retriever.search(query, top_k=5)
    
    if not results:
        print("No results found.")
        continue
    
    for i, result in enumerate(results, 1):
        print(f"\n📄 Result {i} (Score: {result['score']:.4f})")
        
        # Show source if available
        if 'metadata' in result and 'source' in result['metadata']:
            print(f"   Source: {result['metadata']['source']}")
        
        # Show text content (first 300 chars)
        text = result['text']
        if len(text) > 300:
            text = text[:300] + "..."
        print(f"   Text: {text}")
        print("-"*60)
