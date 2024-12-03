from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


#variables

some_data = {
    "name": "Bobby",
    "lastname": "Rixer"
    }

todos = [
    {
        "label": "My first task",
        "done": False
    }
]

#endpoints

@app.route('/todos', methods=['GET'])
def hello_world():
    todoList = jsonify(todos)
    return todoList

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    try:
        todos.pop(position)
    except IndexError:
        return jsonify({"message": "Invalid position"}), 400
    return jsonify(todos), 200




if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)