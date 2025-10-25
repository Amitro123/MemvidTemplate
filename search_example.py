import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidRetriever

# Search your video memory
retriever = MemvidRetriever("knowledge_base.mp4", "knowledge_base.json")

# Perform semantic search
query = "What are the main topics?"
results = retriever.search(query, top_k=5)

print(f"Search results for: '{query}'\n")
print("=" * 60)

for i, result in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(f"Score: {result['score']:.4f}")
    print(f"Text: {result['text'][:200]}...")  # First 200 chars
    if 'metadata' in result:
        print(f"Source: {result['metadata'].get('source', 'Unknown')}")
    print("-" * 60)
