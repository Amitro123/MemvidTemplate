import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidEncoder

# Create more meaningful chunks
chunks = [
    "The Eiffel Tower is located in Paris, France and was completed in 1889.",
    "Python is a high-level programming language created by Guido van Rossum.",
    "The human brain contains approximately 86 billion neurons.",
    "Mount Everest is the highest mountain on Earth at 8,849 meters above sea level.",
    "The speed of light in vacuum is approximately 299,792,458 meters per second.",
    "Shakespeare wrote 37 plays and 154 sonnets during his lifetime.",
    "DNA stands for Deoxyribonucleic Acid and contains genetic instructions.",
    "The Amazon rainforest produces about 20% of the world's oxygen.",
]

print("Creating video memory with interesting facts...")
encoder = MemvidEncoder()
encoder.add_chunks(chunks)
encoder.build_video("facts.mp4", "facts_index.json")
print("✓ Created: facts.mp4 and facts_index.json")
print(f"✓ Stored {len(chunks)} facts")
