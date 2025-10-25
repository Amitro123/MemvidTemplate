import os
os.environ['USE_TF'] = 'NO'

from memvid import MemvidRetriever

print("="*60)
print("Testing Document Search")
print("="*60)

retriever = MemvidRetriever("documents_library.mp4", "documents_library_index.json")

# Test queries
test_queries = [
    "What is machine learning?",
    "Tell me about deep learning",
    "What are the types of machine learning?",
    "How does memvid work?",
    "AI ethics"
]

for query in test_queries:
    print(f"\n{'='*60}")
    print(f"🔍 Query: {query}")
    print('='*60)
    
    results = retriever.search(query, top_k=3)
    
    for i, result in enumerate(results, 1):
        # Result is just a string in this version
        if isinstance(result, str):
            text = result
            score = "N/A"
        else:
            text = result.get('text', result)
            score = result.get('score', 'N/A')
        
        print(f"\n📄 Result {i}")
        
        # Extract source from chunk if present
        if text.startswith('[Source:'):
            source_end = text.find(']')
            source = text[1:source_end]
            content = text[source_end+2:]
        else:
            source = "Unknown"
            content = text
            
        print(f"   {source}")
        print(f"   Preview: {content[:200]}...")
        print("-"*60)

print("\n✅ Search test complete!")
print("\nTry interactive search with: python search_documents.py")
print("Or chat with: python chat_documents.py")
