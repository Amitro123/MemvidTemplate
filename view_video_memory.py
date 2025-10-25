import cv2
import os

def view_video_frames(video_path, output_folder="video_frames"):
    """
    Extract and save frames from the video memory file
    """
    if not os.path.exists(video_path):
        print(f"❌ Video file not found: {video_path}")
        return
    
    # Create output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open video
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"❌ Could not open video: {video_path}")
        return
    
    # Get video info
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print("="*60)
    print(f"Video Memory: {video_path}")
    print("="*60)
    print(f"Total Frames: {total_frames}")
    print(f"Resolution: {width}x{height}")
    print(f"FPS: {fps}")
    print(f"\nExtracting frames to: {output_folder}/")
    print("-"*60)
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save frame as image
        frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_path, frame)
        print(f"✓ Saved: frame_{frame_count:04d}.png")
        frame_count += 1
    
    cap.release()
    
    print("-"*60)
    print(f"\n✅ Extracted {frame_count} frames")
    print(f"📁 Frames saved in: {output_folder}/")
    print("\nEach frame contains QR codes with your text data!")
    print("="*60)

if __name__ == "__main__":
    print("\nWhich video memory do you want to view?\n")
    print("1. PDF Library (pdf_library.mp4)")
    print("2. Documents Library (documents_library.mp4)")
    print("3. Facts (facts.mp4)")
    print("4. Simple Memory (memory.mp4)")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    videos = {
        "1": ("pdf_library.mp4", "pdf_frames"),
        "2": ("documents_library.mp4", "document_frames"),
        "3": ("facts.mp4", "facts_frames"),
        "4": ("memory.mp4", "memory_frames")
    }
    
    if choice in videos:
        video_file, output_folder = videos[choice]
        view_video_frames(video_file, output_folder)
    else:
        print("Invalid choice!")
