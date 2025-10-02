# 🏓 Reweave - Pickleball Bag Try-On

An AI-powered web application that lets users try on different pickleball bags using Google Gemini AI.

## ✨ Features

- 📸 **Photo Upload**: Upload your photo to see how you'd look
- 👜 **Bag Selection**: Choose from premium pickleball bag collections
- 🤖 **AI Generation**: Google Gemini AI creates realistic try-on images
- 📱 **Mobile Friendly**: Responsive design works on all devices
- 🎨 **Modern UI**: Clean blue and white theme

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Reweave
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:8501`

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI**: Google Gemini 2.5 Flash Image Preview
- **Image Processing**: PIL (Pillow)
- **Environment**: Python 3.13+

## 📁 Project Structure

```
Reweave/
├── app.py              # Main Streamlit application
├── main.py             # Command-line version
├── requirements.txt    # Python dependencies
├── logo.png           # Company logo
├── viman.jpg          # Sample user photo
├── *Bag.png           # Bag collection images
└── README.md          # This file
```

## 🎯 Usage

1. Upload a clear photo of yourself
2. Select a bag from the collection
3. Click "Generate Your Champion Look!"
4. Download your AI-generated image

## 🏆 Bag Collections

- Batikara Collection
- Bloom Collection  
- Kaleido Collection
- Marigold Collection
- Mosaie Collection

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is licensed under the MIT License.

---

**Made with ❤️ for Pickleball Players**
