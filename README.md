
---

# 🧠 WebPage Summarizer AI - `dolphin-llama3.1` + Ollama

**WebPage Summarizer AI** is a powerful Python script that scrapes any public webpage, extracts its main textual content, and generates a human-readable summary using the [`dolphin-llama3.1`](https://huggingface.co/CognitiveComputations/dolphin-llama3.1) model via [Ollama](https://ollama.com/). It’s perfect for quickly understanding long-form articles, portfolios, blogs, or news pages — all in one command.

![Python](https://img.shields.io/badge/Made%20With-Python-3776AB?style=for-the-badge&logo=python)  
![BeautifulSoup](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-ff69b4?style=for-the-badge)  
![LLM](https://img.shields.io/badge/LLM-Dolphin%20LLaMA3.1-blueviolet?style=for-the-badge)  

---

## 🚀 Features

- 🌐 **Web Scraper**: Extracts clean, readable content from any webpage using `requests` and `BeautifulSoup`.
- 🧠 **AI-Powered Summary**: Generates short and accurate summaries using a local LLM with `Ollama`.
- 🔧 **System Prompting**: Controlled behavior via a custom system prompt.
- 📄 **Readable Output**: Neatly displays extracted text and generated summary in the terminal.
- 💡 **Developer Friendly**: Clean and extendable Python code with class-based scraping.

---

## 📦 Tech Stack

| Tool            | Purpose                  |
|-----------------|--------------------------|
| `requests`      | Fetch HTML content       |
| `BeautifulSoup` | Parse and clean HTML     |
| `ollama`        | Chat with local LLM      |
| `dolphin-llama3.1` | Summarization LLM     |
| `Python 3.9+`   | Core scripting language  |

---
## Project WorkFLow

<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="800" height="500" fill="#f8f9fa" rx="10" ry="10"/>
  
  <!-- Title -->
  <text x="400" y="30" font-family="Arial, sans-serif" font-size="24" font-weight="bold" text-anchor="middle" fill="#333">WebPage Summarizer AI - Workflow</text>
  
  <!-- Start node -->
  <rect x="50" y="80" width="120" height="60" rx="30" ry="30" fill="#4285F4" stroke="#2C6BED" stroke-width="2"/>
  <text x="110" y="117" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="white">URL Input</text>
  
  <!-- Web Scraping Process -->
  <rect x="250" y="80" width="140" height="60" rx="10" ry="10" fill="#EA4335" stroke="#D62516" stroke-width="2"/>
  <text x="320" y="117" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="white">Fetch HTML</text>
  
  <!-- HTML Processing -->
  <rect x="470" y="80" width="140" height="60" rx="10" ry="10" fill="#FBBC05" stroke="#E2A403" stroke-width="2"/>
  <text x="540" y="117" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="white">Parse HTML</text>
  
  <!-- Text Extraction -->
  <rect x="690" y="80" width="70" height="60" rx="10" ry="10" fill="#34A853" stroke="#2A8940" stroke-width="2"/>
  <text x="725" y="110" font-family="Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="white">Extract</text>
  <text x="725" y="128" font-family="Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="white">Text</text>
  
  <!-- Content Processing -->
  <rect x="655" y="200" width="140" height="60" rx="10" ry="10" fill="#7B68EE" stroke="#5742E8" stroke-width="2"/>
  <text x="725" y="230" font-family="Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="white">Clean &</text>
  <text x="725" y="250" font-family="Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="white">Format Text</text>
  
  <!-- LLM Processing -->
  <rect x="470" y="200" width="140" height="60" rx="10" ry="10" fill="#9C27B0" stroke="#7B1FA2" stroke-width="2"/>
  <text x="540" y="230" font-family="Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="white">Send to</text>
  <text x="540" y="250" font-family="Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="white">Ollama API</text>
  
  <!-- Ollama Component -->
  <rect x="240" y="180" width="160" height="100" rx="10" ry="10" fill="#FF6F00" stroke="#E06400" stroke-width="2"/>
  <text x="320" y="210" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="white">Ollama</text>
  <text x="320" y="235" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">dolphin-llama3.1</text>
  <text x="320" y="255" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">Processes Text</text>
  <text x="320" y="275" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">Generates Summary</text>
  
  <!-- Summary Output -->
  <rect x="50" y="200" width="120" height="60" rx="10" ry="10" fill="#00BCD4" stroke="#0097A7" stroke-width="2"/>
  <text x="110" y="237" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="white">Summary</text>
  
  <!-- Display Component -->
  <rect x="20" y="320" width="180" height="120" rx="10" ry="10" fill="#3F51B5" stroke="#303F9F" stroke-width="2"/>
  <text x="110" y="345" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="white">Terminal Output</text>
  
  <!-- Terminal Content -->
  <rect x="35" y="360" width="150" height="65" rx="5" ry="5" fill="black" stroke="#444" stroke-width="2"/>
  <text x="110" y="380" font-family="Courier, monospace" font-size="10" text-anchor="middle" fill="#00FF00">Summary of: example.com</text>
  <text x="110" y="395" font-family="Courier, monospace" font-size="10" text-anchor="middle" fill="#00FF00">==================</text>
  <text x="110" y="410" font-family="Courier, monospace" font-size="10" text-anchor="middle" fill="#00FF00">This is a website about...</text>
  
  <!-- WebpageScraper Class -->
  <rect x="440" y="360" width="180" height="100" rx="10" ry="10" fill="#8BC34A" stroke="#689F38" stroke-width="2"/>
  <text x="530" y="385" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="white">WebpageScraper</text>
  <text x="530" y="410" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">- fetch_page()</text>
  <text x="530" y="430" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">- extract_text()</text>
  <text x="530" y="450" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">- clean HTML content</text>
  
  <!-- OllamaSummarizer Class -->
  <rect x="250" y="360" width="180" height="100" rx="10" ry="10" fill="#FF5722" stroke="#E64A19" stroke-width="2"/>
  <text x="340" y="385" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="white">OllamaSummarizer</text>
  <text x="340" y="410" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">- check_ollama_running()</text>
  <text x="340" y="430" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">- generate_summary()</text>
  <text x="340" y="450" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">- API communication</text>
  
  <!-- Main Function -->
  <rect x="630" y="360" width="150" height="100" rx="10" ry="10" fill="#795548" stroke="#5D4037" stroke-width="2"/>
  <text x="705" y="385" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="white">display_summary()</text>
  <text x="705" y="410" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">- Main workflow</text>
  <text x="705" y="430" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">- Orchestrates process</text>
  <text x="705" y="450" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">- Handles user interface</text>
  
  <!-- Flow Arrows -->
  <!-- Start to Fetch -->
  <path d="M 170 110 L 240 110" stroke="#666" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Fetch to Parse -->
  <path d="M 390 110 L 460 110" stroke="#666" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Parse to Extract -->
  <path d="M 610 110 L 680 110" stroke="#666" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Extract to Clean -->
  <path d="M 725 140 L 725 190" stroke="#666" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Clean to LLM -->
  <path d="M 655 230 L 620 230" stroke="#666" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- LLM to Ollama -->
  <path d="M 470 230 L 410 230" stroke="#666" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Ollama to Summary -->
  <path d="M 240 230 L 180 230" stroke="#666" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Summary to Display -->
  <path d="M 110 260 L 110 310" stroke="#666" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  
  <!-- Arrow Definitions -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#666"/>
    </marker>
  </defs>
  
  <!-- Legend -->
  <rect x="20" y="470" width="760" height="20" rx="5" ry="5" fill="#eee" stroke="#ddd" stroke-width="1"/>
  <text x="400" y="485" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="#666">WebPage Summarizer AI - Data Flow Diagram © 2025</text>
</svg>

## ⚙️ Setup & Usage

### 1️⃣ Install Requirements

```bash
pip install beautifulsoup4 requests ollama
```

### 2️⃣ Install Ollama & Run the Model

Install [Ollama](https://ollama.com) and pull the model:

```bash
ollama pull CognitiveComputations/dolphin-llama3.1
```

> ✅ You must have `ollama` running locally.

### 3️⃣ Run the Script

```bash
python summarize.py
```

Or modify the URL:

```python
display_summary("https://example.com")
```

---

## 🧪 Example Output

```
==================================================
 Summary of: https://aiman-portfolio-mu.vercel.app/
==================================================
Aiman is a Computer Science student with a focus on software development. The portfolio showcases his skills, projects, and contact information with a clean, responsive design.
==================================================
```

---

## 🗂️ File Structure

```
summarizer/
│
├── summarize.py          # Main script
├── README.md             # Project documentation
```

---

## 🛠️ Future Improvements

- [ ] Add GUI interface using Tkinter or PyWebIO  
- [ ] Support batch summarization for multiple URLs  
- [ ] Export summary to PDF/Markdown  
- [ ] Detect and skip paywalled or login-protected pages  

---

## 🧑‍💻 Author

Made with ❤️ by [Aiman](mailto:aimanalishezan@gmail.com)  
Portfolio: [aiman-portfolio.vercel.app](https://aiman-portfolio-mu.vercel.app/)

---

## 📄 License

This project is **open-source** under the [MIT License](LICENSE).

---
