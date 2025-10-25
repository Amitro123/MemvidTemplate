import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidChat
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("❌ Google API key not found!")
    print("\nQuick setup: set GOOGLE_API_KEY=your-key-here")
    print("Then run this script again.\n")
    exit(1)

print("="*60)
print("Interactive Chat with Video Memory")
print("="*60)
print("\nLoading knowledge base...")

try:
    # Use the facts database if it exists, otherwise use memory.mp4
    if os.path.exists("facts.mp4"):
        chat = MemvidChat("facts.mp4", "facts_index.json")
        print("✓ Loaded: facts.mp4 (interesting facts database)")
    else:
        chat = MemvidChat("memory.mp4", "memory_index.json")
        print("✓ Loaded: memory.mp4")
    
    print("\nType your questions below (or 'quit' to exit)")
    print("="*60 + "\n")
    
    while True:
        question = input("You: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break
            
        if not question:
            continue
            
        try:
            response = chat.chat(question)
            print(f"\nAssistant: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
            
except Exception as e:
    print(f"❌ Failed to initialize: {e}")
    print("\nTroubleshooting:")
    print("1. Check your API key is valid")
    print("2. Ensure internet connection")
    print("3. Run 'python create_better_memory.py' first to create facts.mp4")
