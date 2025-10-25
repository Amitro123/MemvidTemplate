import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidChat
from dotenv import load_dotenv

load_dotenv()

# Check API key
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("❌ Google API key not found!")
    print("Your API key should be in the .env file.\n")
    exit(1)

# Check if documents library exists
if not os.path.exists("documents_library.mp4"):
    print("❌ Documents library not found!")
    print("Please run 'python process_text_files.py' first to create the library.\n")
    exit(1)

print("="*60)
print("Chat with Your Documents")
print("="*60)
print("\n⏳ Loading documents library...")

try:
    chat = MemvidChat("documents_library.mp4", "documents_library_index.json")
    print("✓ Documents library loaded successfully!")
    
    print("\nAsk questions about your documents (type 'quit' to exit)")
    print("="*60 + "\n")
    
    while True:
        question = input("You: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break
            
        if not question:
            continue
            
        try:
            print("\n⏳ Thinking...")
            response = chat.chat(question)
            print(f"\nAssistant: {response}\n")
            print("-"*60)
        except Exception as e:
            print(f"❌ Error: {e}\n")
            
except Exception as e:
    print(f"❌ Failed to initialize: {e}")
    print("\nTroubleshooting:")
    print("1. Check your API key is valid")
    print("2. Ensure internet connection")
    print("3. Run 'python process_text_files.py' first")
