from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Flask Backend is running on port 8085!"

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from App Server!"})

@app.route('/student')
def get_students():
    students = [
        {"id": 1, "name": "Nguyen Van A", "major": "Cloud Computing"},
        {"id": 2, "name": "Tran Thi B", "major": "AI Engineering"},
        {"id": 3, "name": "Le Van C", "major": "Software DevOps"}
    ]
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)
