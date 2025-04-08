## SHL Assessment Recommender

An AI-powered Streamlit application that recommends SHL assessments based on job descriptions using advanced semantic and LLM-driven search techniques.

---

### 🧠 Powered By
- **SentenceTransformers** + **FAISS** for efficient semantic search
- **Gemini Flash** for:
  - Query rewriting
  - Result reranking
  - Fallback handling
- **Streamlit** for building an interactive user interface

---

## For cheking health
1. Start Univcorn server at http://127.0.0.1:8000/
2 . Go to Postman
3. Add the url http://127.0.0.1:8000/health
5. Output for this will be shown in body in postman
![Screenshot (717)](https://github.com/user-attachments/assets/379272e0-cd34-4840-beaf-5dc90ff7edb4)


## For recommend Jobs
1. Start Univcorn server at http://127.0.0.1:8000/
2 . Go to Postman
3. Add the url http://127.0.0.1:8000/recommend
4. Set method to Post and enter query in JSON Format and run the query.
5. Output for this will be shown in body in postman

![Screenshot (716)](https://github.com/user-attachments/assets/446e7ffb-584f-4d14-ab59-2775e28bb6e7)

### 🚀 Demo
Experience the live application here: [SHL Recommender Live App →](https://shlrecommendation.streamlit.app/)

---

### 📦 Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/shl-assessment-recommender.git
cd shl-assessment-recommender
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

---

### 🚧 Features
- Upload or paste job descriptions
- Get real-time SHL assessment recommendations
- Query understanding with LLM refinement
- Fast and scalable similarity search

---

### 🌐 Technologies
| Tech               | Role                             |
|--------------------|----------------------------------|
| SentenceTransformers | Semantic vector generation     |
| FAISS               | Fast vector indexing/search     |
| Gemini Flash        | LLM query enhancement & fallback|
| Streamlit           | Web application UI              |

---

### 🚪 License
MIT License. See `LICENSE` file for details.

---

### ✨ Contributing
Contributions, issues and feature requests are welcome. Feel free to check [issues](https://github.com/your-username/shl-assessment-recommender/issues) page.

---

Crafted with ❤️ for smarter hiring.


