from flask import Flask
from flask_restful import Resource, Api
import analyzer

app = Flask(__name__)
api = Api(app)

class Analyze(Resource):
    def get(self, sentence):
        return analyzer.analyze(sentence)

api.add_resource(Analyze, '/<string:sentence>')

if __name__ == '__main__':
    app.run(debug=True)