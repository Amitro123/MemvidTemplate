import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidChat
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("❌ Google API key not found!")
    print("\nTo set it up:")
    print("1. Run: setup_google_api.bat")
    print("   OR")
    print("2. Manually run: set GOOGLE_API_KEY=your-key-here")
    print("\nThen run this script again.")
    exit(1)

print("✓ Google API key found!")
print("Loading video memory...")

try:
    # Initialize chat with Google AI (it will auto-detect Google from env variable)
    chat = MemvidChat("memory.mp4", "memory_index.json")
    
    print("✓ Chat initialized successfully!")
    print("\n" + "="*60)
    print("Ask a question about your knowledge base:")
    print("="*60 + "\n")
    
    # Example queries
    questions = [
        "What do you know about fact 1?",
        "Tell me about the important facts",
        "What information do you have?"
    ]
    
    for question in questions:
        print(f"Q: {question}")
        response = chat.chat(question)
        print(f"A: {response}")
        print("-" * 60)
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure:")
    print("1. Your API key is valid")
    print("2. You have internet connection")
    print("3. The memory.mp4 and memory_index.json files exist")
