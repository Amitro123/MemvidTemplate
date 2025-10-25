import os
os.environ['USE_TF'] = 'NO'  # Disable TensorFlow to avoid import errors

from memvid import MemvidEncoder, MemvidChat   

chat = MemvidChat("memory.mp4", "memory_index.json")
chat.start_session()
response = chat.chat("What do you know about fact 1?")
print(response)