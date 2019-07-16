from flask import Flask
from flask_restplus import Resource, Api
from Model.DataBase import db_session

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()