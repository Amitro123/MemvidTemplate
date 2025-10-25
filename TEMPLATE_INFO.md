# Memvid Knowledge Base Template - Information

## 📦 What's Included

### Core Processing Scripts
- `process_text_files.py` - Convert text files to video memory
- `process_pdf.py` - Convert PDFs to video memory

### Search Scripts (No API Key Required)
- `search_documents.py` - Interactive search for text files
- `search_pdfs.py` - Interactive search for PDFs

### Chat Scripts (Requires Google AI API Key)
- `chat_documents.py` - Chat with text files
- `chat_pdfs.py` - Chat with PDFs

### Utility Scripts
- `video_info.py` - View information about video memory files
- `view_video_memory.py` - Extract video frames as images
- `play_video.py` - Play video memory in a window
- `test_search.py` - Automated search demo
- `test_rosen_pdf.py` - PDF search demo

### Example Scripts
- `video_memory.py` - Simple example
- `create_better_memory.py` - Create facts database
- `search_facts.py` - Search facts
- `interactive_chat.py` - Interactive chat session

### Configuration Files
- `.env.example` - Example environment variables
- `.gitignore` - Git ignore rules
- `requirements.txt` - Python dependencies

### Documentation
- `README.md` - Main documentation
- `GITHUB_SETUP.md` - GitHub setup guide
- `TEMPLATE_INFO.md` - This file

### Folder Structure
- `documents/` - Place your .txt and .md files here
- `pdfs/` - Place your PDF files here

## 🎯 Use Cases

This template is perfect for:

1. **Personal Knowledge Base**
   - Index your notes, articles, research papers
   - Quick semantic search across all documents

2. **Documentation System**
   - Create searchable documentation
   - Chat with your docs using AI

3. **Research Assistant**
   - Index academic papers
   - Find relevant information quickly

4. **Customer Support**
   - Index support documents
   - Quick answers to common questions

5. **Learning Resource**
   - Organize study materials
   - Interactive Q&A with your notes

## 🔧 Customization Ideas

### Modify Chunk Size
Edit the processing scripts to change chunk size:
```python
# In process_text_files.py
chunk_size = 500  # Adjust this value
```

### Add More File Types
Extend to support other formats:
```python
# Add .docx, .html, etc.
if file.endswith(('.txt', '.md', '.html')):
    # process file
```

### Change Search Results Count
```python
# In search scripts
results = retriever.search(query, top_k=10)  # Change from 5 to 10
```

### Use Different AI Providers
```python
# In chat scripts, add support for OpenAI or Anthropic
# Just set the appropriate API key in .env
```

## 📊 Performance Tips

1. **Large Documents**: Split into smaller chunks for better search accuracy
2. **Many Files**: Process in batches if you have hundreds of files
3. **Search Speed**: Smaller top_k values = faster results
4. **Storage**: Video files are highly compressed, but very large datasets may need optimization

## 🛡️ Security Notes

- ✅ `.env` file is in `.gitignore` - your API keys won't be committed
- ✅ Generated files are ignored - no user data in the repo
- ✅ Only template code is tracked by git

## 🤝 Contributing to the Template

If you improve this template:

1. Fork the repository
2. Make your changes
3. Test thoroughly
4. Submit a pull request

Ideas for contributions:
- Support for more file formats
- Better error handling
- Performance optimizations
- Additional AI providers
- Web interface
- Docker support

## 📝 Version History

- **v1.0** - Initial template release
  - PDF and text file processing
  - Semantic search
  - AI chat integration
  - Video memory visualization

## 🙏 Acknowledgments

- Built with [Memvid](https://github.com/Olow304/memvid) by Olow304
- Uses Google AI for chat features
- Powered by sentence-transformers for embeddings

## 📧 Support

For questions or issues:
- Open an issue on GitHub
- Check the [Memvid documentation](https://github.com/Olow304/memvid)
- Review the example scripts

---

**Happy building! 🚀**
