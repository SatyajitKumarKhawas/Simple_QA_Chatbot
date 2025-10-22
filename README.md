
## 💬 Gemini Q&A Demo

A simple **Streamlit app** powered by **Google Gemini 2.5 Flash** that answers user questions in real time.



### 🚀 Features

* Fast, context-aware answers from Gemini
* Clean Streamlit UI
* Secure `.env` API key handling



### ⚙️ Setup

```bash
git clone https://github.com/your-username/gemini-qa-demo.git
cd gemini-qa-demo
pip install streamlit google-generativeai python-dotenv
```

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

Run the app:

```bash
streamlit run app.py
```

---

### 🧠 Code Overview

```python
model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(q):
    return model.generate_content(q).text
```

---

### 📁 Structure

```
app.py
.env
README.md
requirements.txt
```

---

### ✨ Author

**Satyajit Kumar Khawas**

