from db import db
from db import Project

def update_or_create_project(id, name, details, rawdata):

    # Check if project already exists
    project = Project.query.get(id)

    if project:
        # If exists, update the rest of the fields
        project.name = name
        project.details = details
        project.rawdata = rawdata
    else:
        # It not, create it
        project = Project(id=id, name=name, details=details, rawdata=rawdata)
        db.session.add(project)  

    # Save changes
    db.session.commit()

    return project