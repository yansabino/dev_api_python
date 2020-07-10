from flask import Flask, request
from flask_restful import Resource, Api
import json
from skills import Skills

from skills import Skills

app = Flask(__name__)
api = Api(app)

developers = [
    {
        'id': '0',
        'name': 'Yan',
        'skills': ['Node.js', 'Python', 'Flask']
    },
    {
        'id': '1',
        'name': 'Dessa',
        'skills': ['Node.js']
    }
]


class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = "Dev not found".format(id)
            response = {"status": 400, "message": message}
        return response

    def put(self, id):
        data = json.loads(request.data)
        developers[id] = data
        return data

    def delete(self, id):
        developers.pop(id)
        return {"status": 200, "message": "Dev Deleted"}


class DevList(Resource):
    def get(self):
        return developers

    def post(self):
        data = json.loads(request.data)
        index = len(developers)
        data["id"] = index
        developers.append(data)
        return {'status': 200, 'message': 'Developer inserted successfully'}


api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(DevList, '/dev/')
api.add_resource(Skills, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)
