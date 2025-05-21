# 🧠 SQL Chatbot with LangChain, Azure OpenAI & Streamlit

This project lets you **interact with your MySQL database using natural language**. Simply ask a question like _"What is the total revenue this month?"_ and get a **natural language answer**, powered by **LangChain**, **Azure OpenAI**, and **Streamlit**.

---

## 🚀 Features

- 🔍 Ask questions in plain English
- 🧠 Converts your question to SQL using Azure OpenAI
- 📊 Executes the query on a MySQL database
- 💬 Responds with a human-readable, natural language answer
- 🌐 Simple and clean Streamlit UI

---

## 🧰 Tech Stack

| Tool                  | Purpose                            |
|-----------------------|------------------------------------|
| Streamlit             | UI for asking questions            |
| LangChain             | Prompt management & chaining       |
| Azure OpenAI          | LLM for generating SQL & responses |
| MySQL (via PyMySQL)   | Database to query                  |
| python-dotenv         | Environment variable management    |

---

## 📁 Project Structure

.
├── app.py # Main application script
├── requirements.txt # Python dependencies
├── .env # Your environment variables 
├── README.md # Project documentation

🖥️ How It Works
You enter a question like “List all users who signed up last week.”

LangChain prompts the Azure OpenAI model to generate the appropriate SQL query based on your database schema.

The SQL is run against your MySQL database.

LangChain prompts the model again to translate the raw results into a human-readable answer.

You get a clean, relevant response in natural language.


▶️ Run the App

streamlit run app.py
Open your browser and go to: http://localhost:8501 (or Streamlit will auto-launch it).


📄 License
This project is licensed under the MIT License.

---------🙋‍♀️ Author---------
Marpally Latha Devi,
Prompt Engineer | Generative AI Developer,
GitHub: lathadevi158
