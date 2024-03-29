from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from db import db
from db import Project
from utils import update_or_create_project

# Create Namespaces
ns_project = Namespace('projects', description='Projects operations')

# Create Models for Swagger
project_model = ns_project.model('Project', {
    'id': fields.Integer(description='The project ID'),
    'name': fields.String(required=True, description='The project name'),
    'details': fields.String(required=True, description='The project details'),
    'rawdata': fields.String(required=True, description='The project raw data')
})

# Create enpoints for Namespace "projects"
@ns_project.route('/')
class ProjectList(Resource):
    @ns_project.doc('list_projects')
    @ns_project.marshal_list_with(project_model)
    def get(self):
        projects = Project.query.all()
        return projects

@ns_project.route('/copydata/')
class ProjectData(Resource):

    @ns_project.doc('create_or_update_project')
    @ns_project.expect(project_model, validate=True)
    def post(self):

        # Get data from request
        data = ns_project.payload
        project_id = data['id']
        project_name = data['name']
        project_details = data['details']
        project_rawdata = data['rawdata']

        # Update or create project
        project = update_or_create_project(project_id, project_name, project_details, project_rawdata)

        # DO WHATEVER
        #... irods commands to create, given project_id and raw_data_path, a collection and get success boolean and irods info dict (containing ticket id) 
        
        return {'message': 'Project created or updated successfully'}, 200