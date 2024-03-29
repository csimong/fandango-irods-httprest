from flask import Flask
from flask_restx import Api
from db import db
from views import ns_project

# Instanciate flask app and Flask-RESTx Api
app = Flask(__name__)
api = Api(app, version='1.0', title='FandanGO iRODS API', description='iRODS microservice API within fandanGO application') 

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fandango-irods.db' # URI configuration (sqlite and fandango.db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Associate db to flask app
db.init_app(app)

# Create all db tables under app context
with app.app_context():
    db.create_all()

# Import and register namespaces
api.add_namespace(ns_project, path='/projects')

if __name__ == '__main__':
    app.run(port=4000, debug=True)
