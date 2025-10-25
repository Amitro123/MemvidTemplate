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

# Check if PDF library exists
if not os.path.exists("pdf_library.mp4"):
    print("❌ PDF library not found!")
    print("Please run 'python process_pdf.py' first to create the library.\n")
    exit(1)

print("="*60)
print("Chat with Your PDF Library")
print("="*60)
print("\n⏳ Loading PDF library...")

try:
    chat = MemvidChat("pdf_library.mp4", "pdf_library_index.json")
    print("✓ PDF library loaded successfully!")
    
    print("\nAsk questions about your PDFs (type 'quit' to exit)")
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
    print("3. Run 'python process_pdf.py' first")
