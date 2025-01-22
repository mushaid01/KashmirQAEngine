# KashmirQAEngine 🌍☁️

Welcome to the **KashmirQAEngine**—an intelligent AI-driven solution to answer all your queries about Kashmir’s rich history, culture, significant events, and current affairs. Powered by state-of-the-art AI and vector-based search technologies, this chatbot delivers precise and engaging responses. 

---

## 🔬 Features

### 🎨 Knowledge Areas
- **⛪ History**: Ancient and modern history of Kashmir.
- **🎨 Culture**: Traditional crafts, cuisines, and festivals.
- **📊 Current Affairs**: Insights on recent developments and ongoing events.

### 🤖 AI-Powered Capabilities
- **Contextual Understanding**: Retrieves information based on user queries.
- **Accurate Results**: Uses vectorstores and embeddings for precise answers.
- **Dynamic Routing**: Automatically decides between vector-based retrieval and live web search.

### 🚀 Advanced Grading and Validation
- **`question_router`**: Routes user questions to the appropriate data source—vectorstore or web search—based on context.
- **`rag_chain`**: Generates accurate and relevant answers by combining retrieval-augmented generation techniques.
- **`Retrieval Grader`**: Ensures retrieved documents are relevant to the question.
- **`Hallucination Grader`**: Validates that the generation is grounded in the retrieved documents.
- **`Answer Grader`**: Verifies that the generated answer directly addresses the user’s question.

---

## 🛠️ Installation

### Prerequisites
- Python 3.10+
- Virtual Environment (optional but recommended)
- API Keys for:
  - [Groq](https://groq.com/)
  - [Tavily Search](https://tavily.com/)

### Setup Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mushaid01/KashmirQAEngine
   cd KashmirQAEngine
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create Environment Variables**:
   - Add your API keys in the `.env` file:
     ```
     GROQ_API_KEY=your_groq_api_key
     TAVILY_API_KEY=your_tavily_api_key
     ```

5. **Run the Application**:
   ```bash
   python agent.py
   ```

---

## 🛠️ How It Works

### Workflow Overview 🔄
1. **Question Routing**:
   - The `question_router` determines whether to use:
     - **Vectorstore**: For pre-loaded documents on Kashmir.
     - **Web Search**: For real-time queries.

2. **Retrieval**:
   - Uses Chroma to retrieve document chunks based on relevance.
   - Graded for relevance by the **Retrieval Grader**.

3. **Response Generation**:
   - `rag_chain` combines retrieved documents and the user’s question to generate precise answers.
   - Validated by the **Hallucination Grader** to ensure grounding in documents.

4. **Answer Grading**:
   - The **Answer Grader** ensures the generated response directly addresses the user’s query.

---

## 🎨 Demo 👇

### Sample Query:
**“How did the Partition of 1947 impact Kashmir?”**

#### Bot Response:
```json
{
  "datasource": "vectorstore",
  "answer": "The Partition of 1947 led to the princely state of Jammu and Kashmir being caught between India and Pakistan, eventually resulting in territorial disputes and conflicts."
}
```

---

## 🚀 Future Enhancements

### 🎨 Planned Features
- Integration with additional language models for multilingual support.
- Enhanced document grading for better relevance.
- Real-time sentiment analysis for user feedback.

---

## 🌍 Community and Support
### 👤 Contributors
We welcome contributions from developers, researchers, and enthusiasts!.

### 📢 Feedback
Have questions or suggestions? [Open an issue](https://github.com/mushaid01/KashmirQAEngine/issues) or email us at mir786mushaid@gmail.com.

---

Made with ❤️ by the **Mir Mushaidul Islam**.
