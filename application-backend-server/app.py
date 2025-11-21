from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="10.10.10.13", 
        user="root",
        password="root123",
        database="studentdb"
    )

@app.route('/')
def index():
    return "✅ Flask Backend connected to MariaDB!"

# --- ROUTE ĐỂ BẠN TEST CURL ---
@app.route('/hello')
def hello():
    return jsonify(message="Hello from App Server!")
# ------------------------------

# CRUD - READ
@app.route('/student', methods=['GET'])
def get_students():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(students)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# CRUD - CREATE
@app.route('/student', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (student_id, fullname, dob, major) VALUES (%s,%s,%s,%s)",
            (data['student_id'], data['fullname'], data['dob'], data['major'])
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Student added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# CRUD - UPDATE
@app.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET fullname=%s, dob=%s, major=%s WHERE id=%s",
            (data['fullname'], data['dob'], data['major'], id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": f"Student {id} updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# CRUD - DELETE
@app.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": f"Student {id} deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/secure')
def secure_route():
    return "✅ Tuyệt vời! Bạn đã truy cập được endpoint /secure!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)