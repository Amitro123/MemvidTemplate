import cv2
import os

def play_video(video_path):
    """
    Play the video memory file in a window
    """
    if not os.path.exists(video_path):
        print(f"❌ Video file not found: {video_path}")
        return
    
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
    print(f"Playing: {video_path}")
    print("="*60)
    print(f"Total Frames: {total_frames}")
    print(f"Resolution: {width}x{height}")
    print(f"FPS: {fps}")
    print("\nPress 'q' to quit, SPACE to pause/resume")
    print("="*60)
    
    window_name = f"Video Memory: {os.path.basename(video_path)}"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    
    paused = False
    frame_num = 0
    
    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                print("\n✓ Video finished")
                break
            
            frame_num += 1
            
            # Add frame info overlay
            text = f"Frame {frame_num}/{total_frames} - QR Code Data"
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.7, (0, 255, 0), 2)
            
            cv2.imshow(window_name, frame)
        
        # Wait for key press (1ms delay for smooth playback)
        key = cv2.waitKey(int(1000/fps) if fps > 0 else 30) & 0xFF
        
        if key == ord('q'):
            print("\n✓ Stopped by user")
            break
        elif key == ord(' '):
            paused = not paused
            status = "PAUSED" if paused else "PLAYING"
            print(f"\n{status}")
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("\nWhich video memory do you want to play?\n")
    print("1. PDF Library (pdf_library.mp4)")
    print("2. Documents Library (documents_library.mp4)")
    print("3. Facts (facts.mp4)")
    print("4. Simple Memory (memory.mp4)")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    videos = {
        "1": "pdf_library.mp4",
        "2": "documents_library.mp4",
        "3": "facts.mp4",
        "4": "memory.mp4"
    }
    
    if choice in videos:
        play_video(videos[choice])
    else:
        print("Invalid choice!")
