import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidChat

# To use chat functionality, you need to:
# 1. Install an LLM provider: pip install openai
# 2. Set your API key: export OPENAI_API_KEY="your-key-here"

# For now, this shows how to use it once you have the API key
try:
    chat = MemvidChat("facts.mp4", "facts_index.json")
    
    # Start a conversation
    response = chat.chat("What do you know about mountains?")
    print(response)
    
except Exception as e:
    print(f"Chat requires an LLM provider. Error: {e}")
    print("\nTo enable chat:")
    print("1. Install OpenAI: pip install openai")
    print("2. Set API key: set OPENAI_API_KEY=your-key-here")
    print("\nFor now, use search_facts.py for semantic search without LLM!")
