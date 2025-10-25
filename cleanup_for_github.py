"""
Cleanup script to prepare project for GitHub
Removes generated files and user data while keeping the template structure
"""
import os
import shutil

def cleanup():
    print("="*60)
    print("Cleaning up project for GitHub")
    print("="*60)
    
    # Files to delete
    files_to_delete = [
        # Generated video memory files
        "memory.mp4",
        "memory_index.json",
        "facts.mp4",
        "facts_index.json",
        "documents_library.mp4",
        "documents_library_index.json",
        "pdf_library.mp4",
        "pdf_library_index.json",
        "knowledge_base.mp4",
        "knowledge_base.json",
        
        # Environment file with API key
        ".env",
        
        # Old README
        "README.md",
        
        # Temporary/test files
        "fix_dependencies.py",
        "fix_tf_issue.py",
        "set_api_key.bat",
        "setup_google_api.bat",
        
        # Old guide files (keeping only the new ones)
        "HOW_TO_USE_WITH_FILES.md",
        "QUICK_START.md",
        "COMPLETE_GUIDE.md",
    ]
    
    # Folders to delete
    folders_to_delete = [
        "venv",
        "__pycache__",
        "video_frames",
        "pdf_frames",
        "document_frames",
        "facts_frames",
        "memory_frames",
    ]
    
    # User documents to delete (keep the folders)
    user_files = [
        "documents/ai_and_machine_learning.txt",
        "documents/sample.txt",
        "pdfs/ROSEN.pdf",
    ]
    
    deleted_files = 0
    deleted_folders = 0
    
    # Delete files
    for file in files_to_delete:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"✓ Deleted: {file}")
                deleted_files += 1
            except Exception as e:
                print(f"✗ Error deleting {file}: {e}")
    
    # Delete folders
    for folder in folders_to_delete:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"✓ Deleted folder: {folder}/")
                deleted_folders += 1
            except Exception as e:
                print(f"✗ Error deleting {folder}: {e}")
    
    # Delete user files
    for file in user_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"✓ Deleted user file: {file}")
                deleted_files += 1
            except Exception as e:
                print(f"✗ Error deleting {file}: {e}")
    
    # Rename new README
    if os.path.exists("README_NEW.md"):
        try:
            os.rename("README_NEW.md", "README.md")
            print(f"✓ Renamed README_NEW.md → README.md")
        except Exception as e:
            print(f"✗ Error renaming README: {e}")
    
    print("\n" + "="*60)
    print(f"✅ Cleanup complete!")
    print(f"   Deleted {deleted_files} files")
    print(f"   Deleted {deleted_folders} folders")
    print("="*60)
    
    print("\n📁 Project is ready for GitHub!")
    print("\nNext steps:")
    print("1. Review the files")
    print("2. Initialize git: git init")
    print("3. Add files: git add .")
    print("4. Commit: git commit -m 'Initial commit'")
    print("5. Create GitHub repo and push")
    print("="*60)

if __name__ == "__main__":
    response = input("This will delete generated files and user data. Continue? (yes/no): ")
    if response.lower() in ['yes', 'y']:
        cleanup()
    else:
        print("Cleanup cancelled.")
