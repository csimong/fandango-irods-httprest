from flask import request, jsonify
from db import db
from db import Project
from utils import update_or_create_project


def register_views(app):
    @app.route('/projects/', methods=['GET'])
    def get_projects():
            projects = Project.query.all()
            projects_list = [project.to_dict() for project in projects]
            return jsonify(projects_list)

    @app.route('/copydata/', methods=['POST'])
    def get_copydata():
            
            # Get data from request
            data = request.get_json()

            project_id = data['id']
            project_name = data['name']
            project_details = data['details']
            project_rawdata = data['rawdata']

            # Update or create project
            project = update_or_create_project(project_id, project_name, project_details, project_rawdata)

            # DO WHATEVER
            #... irods commands to create, given project_id and raw_data_path, a collection and get success boolean and irods info dict (containing ticket id) 

            return jsonify({'message': 'Project created or updated successfully'}), 200