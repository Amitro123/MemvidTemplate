import os
import json

def show_video_info():
    """
    Show information about all video memory files
    """
    print("="*60)
    print("Video Memory Files Overview")
    print("="*60)
    
    video_files = [
        ("pdf_library.mp4", "pdf_library_index.json"),
        ("documents_library.mp4", "documents_library_index.json"),
        ("facts.mp4", "facts_index.json"),
        ("memory.mp4", "memory_index.json")
    ]
    
    for video_file, index_file in video_files:
        if os.path.exists(video_file):
            print(f"\n📹 {video_file}")
            
            # Get file size
            video_size = os.path.getsize(video_file)
            print(f"   Size: {video_size:,} bytes ({video_size/1024:.2f} KB)")
            
            # Check index file
            if os.path.exists(index_file):
                index_size = os.path.getsize(index_file)
                print(f"   Index: {index_file} ({index_size:,} bytes)")
                
                # Try to read index info
                try:
                    with open(index_file, 'r') as f:
                        index_data = json.load(f)
                        if 'chunks' in index_data:
                            print(f"   Chunks: {len(index_data['chunks'])}")
                        if 'metadata' in index_data:
                            print(f"   Metadata: {index_data['metadata']}")
                except:
                    pass
            
            print(f"   Status: ✅ Ready to use")
        else:
            print(f"\n📹 {video_file}")
            print(f"   Status: ❌ Not created yet")
    
    print("\n" + "="*60)
    print("\nHow to view the videos:")
    print("  1. Extract frames: python view_video_memory.py")
    print("  2. Play video: python play_video.py")
    print("  3. Open in media player: Right-click → Open with → VLC/Media Player")
    print("="*60)

if __name__ == "__main__":
    show_video_info()
