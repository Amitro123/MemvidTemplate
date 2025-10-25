import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidEncoder

# Initialize encoder BEFORE using it
encoder = MemvidEncoder(chunk_size=512)

# Check if documents directory exists
if not os.path.exists("documents"):
    os.makedirs("documents")
    print("Created 'documents' folder - please add your text files there")
else:
    # Process all text files in documents folder
    for file in os.listdir("documents"):
        if file.endswith((".txt", ".md")):
            with open(f"documents/{file}", "r", encoding="utf-8") as f:
                # Add text with metadata
                encoder.add_text(f.read(), metadata={"source": file})
                print(f"Added {file}")
    
    # Build video ONCE after all files are processed
    encoder.build_video("knowledge_base.mp4", "knowledge_base.json")
    print("Video memory created: knowledge_base.mp4")
