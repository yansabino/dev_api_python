from flask_restful import Resource

skills = ['Python', 'Java', 'Node.js', 'React.js']

class Skills(Resource):
    def get(self):
        return skills