# Memvid Knowledge Base Template

A ready-to-use template for creating searchable knowledge bases from PDFs and text files using [Memvid](https://github.com/Olow304/memvid) - a video-based AI memory library.

## 🚀 Features

- 📄 **PDF Processing** - Convert PDFs to searchable video memory
- 📝 **Text File Processing** - Index .txt and .md files
- 🔍 **Semantic Search** - Find information by meaning, not just keywords
- 💬 **AI Chat** - Ask questions about your documents (requires API key)
- 🎥 **Video Compression** - Efficient storage using video codecs
- 🔒 **No Database** - Everything in 2 files (.mp4 + .json)

## 📋 Prerequisites

- Python 3.8+
- pip

## 🛠️ Installation

### 1. Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/memvid-knowledge-base.git
cd memvid-knowledge-base
```

### 2. Install dependencies
```bash
pip install memvid PyPDF2 python-dotenv
```

### 3. (Optional) Set up Google AI API for chat features
Create a `.env` file:
```bash
GOOGLE_API_KEY=your-api-key-here
```

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 📖 Quick Start

### Process Text Files

1. **Add your files** to the `documents/` folder (.txt or .md)
2. **Run the processor:**
   ```bash
   python process_text_files.py
   ```
3. **Search your documents:**
   ```bash
   python search_documents.py
   ```

### Process PDFs

1. **Add PDFs** to the `pdfs/` folder
2. **Run the processor:**
   ```bash
   python process_pdf.py
   ```
3. **Search your PDFs:**
   ```bash
   python search_pdfs.py
   ```

### Chat with Your Documents

```bash
# For text files
python chat_documents.py

# For PDFs
python chat_pdfs.py
```

## 📁 Project Structure

```
memvid-knowledge-base/
├── documents/              # Put your .txt and .md files here
├── pdfs/                   # Put your PDF files here
│
├── process_text_files.py   # Convert text files to video memory
├── process_pdf.py          # Convert PDFs to video memory
│
├── search_documents.py     # Search text files (no API key needed)
├── search_pdfs.py          # Search PDFs (no API key needed)
│
├── chat_documents.py       # Chat with text files (requires API key)
├── chat_pdfs.py            # Chat with PDFs (requires API key)
│
├── video_info.py           # View info about video memory files
├── view_video_memory.py    # Extract video frames as images
├── play_video.py           # Play video memory files
│
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## 🎯 Usage Examples

### Example 1: Index Documentation

```bash
# Add markdown files to documents/
cp ~/my-docs/*.md documents/

# Process them
python process_text_files.py

# Search
python search_documents.py
```

### Example 2: Create PDF Library

```bash
# Add research papers to pdfs/
cp ~/papers/*.pdf pdfs/

# Process them
python process_pdf.py

# Search
python search_pdfs.py
```

### Example 3: Interactive Chat

```bash
# Set up API key in .env
echo "GOOGLE_API_KEY=your-key" > .env

# Chat with your documents
python chat_documents.py
```

## 🔍 How It Works

1. **Text → QR Codes** - Your text is converted to QR codes
2. **QR Codes → Video Frames** - QR codes are packed into video frames
3. **Video Compression** - Modern codecs compress the data efficiently
4. **Semantic Embeddings** - AI creates searchable embeddings
5. **Fast Retrieval** - Search by meaning in milliseconds

## 📊 Output Files

After processing, you'll get:

- `documents_library.mp4` - Compressed video containing your text
- `documents_library_index.json` - Search index with embeddings
- `pdf_library.mp4` - Compressed video containing PDF content
- `pdf_library_index.json` - Search index for PDFs

## 🎨 Advanced Features

### View Video Memory
```bash
# Extract frames as images
python view_video_memory.py

# Play video in window
python play_video.py

# Get video info
python video_info.py
```

### Customize Processing

Edit the scripts to adjust:
- Chunk size (default: ~500 characters)
- Number of search results
- Video codec settings

## 🐛 Troubleshooting

### TensorFlow Import Errors
All scripts include `os.environ['USE_TF'] = 'NO'` to avoid TensorFlow conflicts.

### API Key Not Found
Make sure `.env` file exists with:
```
GOOGLE_API_KEY=your-actual-key
```

### No Results Found
- Check that files are in the correct folder (`documents/` or `pdfs/`)
- Verify the video memory files were created (`.mp4` and `.json`)
- Try broader search queries

## 📝 License

MIT License - feel free to use this template for any project!

## 🙏 Credits

Built with [Memvid](https://github.com/Olow304/memvid) by Olow304

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📧 Support

For issues with:
- **This template**: Open an issue on this repo
- **Memvid library**: See [Memvid GitHub](https://github.com/Olow304/memvid)

---

**Happy Knowledge Building! 🚀**
