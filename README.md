# 🎯 JAM - File Repository for Hands-on Lab

A simple, lightweight file-sharing repository designed for educational hands-on labs and workshops.

## 🚀 Quick Start

### Option 1: Run with Python (Recommended)

```bash
# Clone the repository
git clone https://github.com/samuel-bohman/jam.git
cd jam

# Start the server
python3 server.py
```

Then open your browser to: **http://localhost:8000**

### Option 2: Use any HTTP server

If you prefer another HTTP server:

```bash
# Using Python's built-in server
python3 -m http.server 8000

# Using Node.js http-server (requires npm install -g http-server)
http-server -p 8000

# Using PHP's built-in server
php -S localhost:8000
```

## 📁 Repository Structure

```
jam/
├── index.html          # Main landing page with file browser
├── server.py           # Simple Python HTTP server
├── files/              # Directory containing lab files
│   ├── lab-01-starter.txt
│   ├── lab-02-intermediate.txt
│   ├── lab-03-advanced.txt
│   ├── reference-materials.txt
│   └── tutorial-videos.txt
└── README.md           # This file
```

## 📝 Adding Your Own Files

1. Place your lab files in the `files/` directory
2. Update `index.html` to list your new files
3. Customize the descriptions and icons as needed

### Example: Adding a New Lab File

```html
<li class="file-item">
    <div class="file-info">
        <span class="file-icon">📄</span>
        <div>
            <div class="file-name">your-file.zip</div>
            <div class="file-description">Your file description</div>
        </div>
    </div>
    <a href="files/your-file.zip" class="download-btn" download>Download</a>
</li>
```

## 🎨 Customization

### Branding
Edit `index.html` to change:
- Title and description in the header
- Color scheme (CSS variables in the `<style>` section)
- File listings and descriptions

### File Types
The repository supports any file type:
- `.zip`, `.tar.gz` - Compressed archives
- `.pdf`, `.docx` - Documents
- `.txt`, `.md` - Text files
- `.mp4`, `.mov` - Videos (consider external hosting for large files)
- Any other file format your lab needs

## 🌐 Deployment Options

### GitHub Pages (Free & Easy)

1. Push your repository to GitHub
2. Go to Settings → Pages
3. Select the main branch as the source
4. Your site will be available at: `https://username.github.io/jam/`

### Other Hosting Options

- **Netlify**: Drag and drop deployment
- **Vercel**: Git-based deployment
- **AWS S3**: Static website hosting
- **Self-hosted**: Use any web server (Apache, Nginx, etc.)

## 🔒 Security Considerations

For production use, consider:
- Adding authentication if files are sensitive
- Using HTTPS for secure transfers
- Implementing access logging
- Setting up proper CORS policies
- Scanning uploaded files for malware

## 💡 Use Cases

Perfect for:
- Educational workshops and training
- Coding bootcamps and classes
- Conference hands-on sessions
- Team onboarding materials
- Study group resources
- Tutorial file distribution

## 🤝 Contributing

Feel free to customize this repository for your needs! Some ideas:
- Add user authentication
- Implement file upload functionality
- Add search and filtering
- Include file previews
- Add analytics tracking

## 📄 License

This is a simple educational tool. Use it freely for your labs and workshops!

## 🆘 Troubleshooting

**Port already in use?**
```bash
# Change the port in server.py or use:
python3 -m http.server 8080
```

**Files not downloading?**
- Check that files exist in the `files/` directory
- Verify file paths in `index.html` match actual files
- Ensure your browser isn't blocking downloads

**Server not starting?**
- Make sure Python 3 is installed: `python3 --version`
- Check firewall settings
- Try running with elevated permissions (not recommended for production)

---

Built with ❤️ for hands-on learning