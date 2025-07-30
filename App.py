from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

# --- START: ADD THIS IMPORT STATEMENT ---
from column import bp as columns_blueprint # Import the blueprint from column.py
# --- END: ADD THIS IMPORT STATEMENT ---

# --- Initialize the Flask App ---
app = Flask(__name__)
CORS(app) 

# --- START: REGISTER THE BLUEPRINT ---
app.register_blueprint(columns_blueprint) # Link the blueprint to the app
# --- END: REGISTER THE BLUEPRINT ---

# --- Database Connection Details ---
DB_CONFIG = {
    'user': 'root',
    'password': 'Gudu@2005', # Your MySQL password
    'host': '127.0.0.1',
    'database': 'employees'
}

def get_db_connection():
    """Establishes and returns a database connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

# --- API Route to Get Employees (Existing Code) ---
@app.route('/api/employees', methods=['GET'])
def get_employees():
    """API endpoint to fetch employee data."""
    # ... (this function remains exactly the same)
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        if conn is None or not conn.is_connected():
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor(dictionary=True)
        query = "SELECT emp_no, first_name, last_name, gender, hire_date FROM employees LIMIT 100"
        cursor.execute(query)
        employees = cursor.fetchall()

        for employee in employees:
            if 'hire_date' in employee and employee['hire_date']:
                employee['hire_date'] = employee['hire_date'].isoformat()

        return jsonify(employees)
    except mysql.connector.Error as err:
        print(f"API Error: {err}")
        return jsonify({"error": "An error occurred while fetching data."}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# --- Main entry point to run the app ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
