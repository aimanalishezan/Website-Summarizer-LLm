
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

![webpage summarizer](https://github.com/user-attachments/assets/db9e591e-a9ec-49a5-a538-b57d335da1bb)


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
