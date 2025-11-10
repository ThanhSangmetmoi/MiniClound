from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="relational-database",  # tên service docker-compose đúng
        user="root",
        password="root123",
        database="studentdb"
    )


@app.route('/')
def index():
    return "✅ Flask Backend connected to MariaDB!"

# CRUD - READ
@app.route('/student', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(students)

# CRUD - CREATE
@app.route('/student', methods=['POST'])
def add_student():
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

# CRUD - UPDATE
@app.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
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

# CRUD - DELETE
@app.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": f"Student {id} deleted successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)
