import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidRetriever

# Use retriever instead of chat (doesn't need LLM)
retriever = MemvidRetriever("memory.mp4", "memory_index.json")

# Search for information
query = "fact 1"
print(f"Searching for: '{query}'")
print("=" * 60)

results = retriever.search(query, top_k=3)

if results:
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"  Score: {result['score']:.4f}")
        print(f"  Text: {result['text']}")
else:
    print("No results found")
