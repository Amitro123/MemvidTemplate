import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidRetriever

# Search the facts database
retriever = MemvidRetriever("facts.mp4", "facts_index.json")

# Try different queries
queries = [
    "What is the tallest mountain?",
    "Tell me about Python programming",
    "Where is the Eiffel Tower?",
    "How fast is light?",
]

for query in queries:
    print(f"\n{'='*60}")
    print(f"Query: {query}")
    print('='*60)
    
    results = retriever.search(query, top_k=2)
    
    for i, result in enumerate(results, 1):
        print(f"\n  Result {i} (Score: {result['score']:.4f}):")
        print(f"  → {result['text']}")
