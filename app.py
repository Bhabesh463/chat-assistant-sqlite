from flask import Flask, request, jsonify
import sqlite3
import re

app = Flask(__name__)

def query_database(sql, params=()):
    """Executes SQL query and returns results."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results

def parse_query(user_input):
    """Converts user input into an SQL query."""
    user_input = user_input.lower()

    # Query 1: Show all employees in a department
    match = re.search(r"employees in the (.+?) department", user_input)
    if match:
        dept = match.group(1).capitalize()
        return f"SELECT Name FROM Employees WHERE Department = ?", (dept,)

    # Query 2: Get department manager
    match = re.search(r"manager of the (.+?) department", user_input)
    if match:
        dept = match.group(1).capitalize()
        return f"SELECT Manager FROM Departments WHERE Name = ?", (dept,)

    # Query 3: Employees hired after a date
    match = re.search(r"employees hired after (\d{4}-\d{2}-\d{2})", user_input)
    if match:
        date = match.group(1)
        return f"SELECT Name FROM Employees WHERE Hire_Date > ?", (date,)

    # Query 4: Total salary expense for a department
    match = re.search(r"total salary expense for the (.+?) department", user_input)
    if match:
        dept = match.group(1).capitalize()
        return f"SELECT SUM(Salary) FROM Employees WHERE Department = ?", (dept,)

    return None, None
# API for post method
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("query", "")
    
    sql, params = parse_query(user_input)
    
    if sql:
        results = query_database(sql, params)
        return jsonify({"response": results if results else "No data found."})
    
    return jsonify({"response": "I didn't understand that. Please try again."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # ✅ Use Render's PORT variable
    app.run(debug=True, host="0.0.0.0", port=port)
