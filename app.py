from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
        'name': 'Yan',
        'skills': ['Node.js', 'Python', 'Flask']
    },
    {
        'name': 'Dessa',
        'skills': ['Node.js']
    }
]


@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            message = "Dev not found".format(id)
            response = {"status": 400, "message": message}
        return jsonify(response)
    elif request.method == 'PUT':
        data = json.loads(request.data)
        developers[id] = data
        return jsonify(data)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({"status": 200, "message": "Dev Deleted"})


@app.route('/dev/', methods=['POST', 'GET'])
def dev_list():
    if request.method == 'POST':
        data = json.loads(request.data)
        developers.append(data)
        return jsonify({'status': 200, 'message': 'Developer inserted successfully'})
    elif request.method == 'GET':
        response = developers
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
