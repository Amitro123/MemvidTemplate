# GitHub Setup Guide

Follow these steps to upload this project to GitHub as a template.

## Step 1: Clean Up the Project

Run the cleanup script to remove generated files and user data:

```bash
python cleanup_for_github.py
```

This will:
- ✅ Remove all generated .mp4 and .json files
- ✅ Remove your .env file with API keys
- ✅ Remove user documents (sample files)
- ✅ Remove temporary/test files
- ✅ Keep all the template scripts
- ✅ Keep folder structure

## Step 2: Initialize Git Repository

```bash
# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Memvid Knowledge Base Template"
```

## Step 3: Create GitHub Repository

### Option A: Using GitHub Website

1. Go to https://github.com/new
2. Repository name: `memvid-knowledge-base` (or your preferred name)
3. Description: "A template for creating searchable knowledge bases from PDFs and text files using Memvid"
4. Choose: **Public** (so others can use it as a template)
5. ✅ Check "Template repository" (important!)
6. Don't initialize with README (we already have one)
7. Click "Create repository"

### Option B: Using GitHub CLI

```bash
# Install GitHub CLI if needed: https://cli.github.com/

# Create repository
gh repo create memvid-knowledge-base --public --source=. --remote=origin

# Mark as template
gh repo edit --template
```

## Step 4: Push to GitHub

```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/memvid-knowledge-base.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 5: Configure as Template

On GitHub:

1. Go to your repository settings
2. Scroll to "Template repository" section
3. ✅ Check "Template repository"
4. Save

## Step 6: Add Topics (Optional but Recommended)

Add these topics to make your repo discoverable:

- `memvid`
- `knowledge-base`
- `pdf-search`
- `semantic-search`
- `ai`
- `template`
- `python`
- `document-search`

## Step 7: Test the Template

1. Go to your repository on GitHub
2. Click "Use this template" button
3. Create a new repository from it
4. Clone and test that everything works

## 🎉 Done!

Your template is now live on GitHub! Others can use it by clicking "Use this template".

## 📝 Recommended: Add a License

Add a LICENSE file (MIT recommended):

```bash
# Create LICENSE file
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

# Commit and push
git add LICENSE
git commit -m "Add MIT license"
git push
```

## 🔗 Share Your Template

Share the link: `https://github.com/YOUR_USERNAME/memvid-knowledge-base`

People can use it by clicking "Use this template" → "Create a new repository"
