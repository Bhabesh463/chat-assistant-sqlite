Chat Assistant for SQLite Database
____________________________________________________________________________________________________________________________________________________________________
A Flask-based Chat Assistant that interacts with an SQLite database to answer user queries. It supports natural language queries and converts them into SQL commands to fetch data.

____________________________________________________________________________________________________________________________________________________________________
🚀 Features
✔ Accepts natural language queries (e.g., "Who is the manager of Sales?").
✔ Converts queries into SQL and fetches data from the SQLite database.
✔ Handles various queries related to employees, departments, and salaries.
✔ Includes a simple frontend UI to interact with the assistant.
✔ Supports error handling for invalid queries.

___________________________________________________________________________________________________________________________________________________________________
/Assignment
│── app.py                   # Main Flask application
│── database_setup.py         # Script to create & populate the database
│── database.db               # SQLite database file
│── requirements.txt          # Dependencies for the project
│── README.md                 # Project documentation (this file)
│── /templates                # Folder for frontend HTML files
│   ├── index.html            # Simple frontend UI
____________________________________________________________________________________________________________________________________________________________________
🛠️ Setup & Run Locally
1️⃣ Install Dependencies
First, install Python (if not already installed).
Then, install required dependencies:

pip install -r requirements.txt
2️⃣ Create the Database
Run the following command to create database.db:


python database_setup.py
3️⃣ Start the Flask Server
Run the Flask app:


python app.py
If successful, you’ll see:


 * Running on http://127.0.0.1:5000/
4️⃣ Open the Frontend UI
Go to:

http://127.0.0.1:5000/
Enter a query and test the assistant!

📌 Example Queries
Try asking:
✔ "Who is the manager of the Sales department?"
✔ "Show me all employees in the Engineering department."
✔ "List all employees hired after 2021-01-01."
✔ "What is the total salary expense for the Marketing department?"

🚀 Deployment on Render
The assistant is deployed on Render. You can access it here:
👉 Live App

⚠️ Known Limitations & Improvements
🔹 Limitations
The assistant only supports predefined queries and cannot answer random general questions.
No authentication is added (so anyone can access it).
🔹 Future Improvements
✅ Add AI-powered natural language processing (using OpenAI or spaCy).
✅ Enhance the frontend with a chatbot-like UI.
✅ Improve error handling for better responses.

🤝 Contributing
Feel free to fork this repository, make improvements, and submit a pull request! 😊

📜 License
This project is open-source under the MIT License.

Link- https://chat-assistant-sqlite-tzd3.onrender.com/












