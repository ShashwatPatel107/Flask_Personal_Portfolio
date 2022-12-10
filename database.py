import os
import sqlalchemy
from sqlalchemy import create_engine,engine , text
# connect to my sql with sqlalchemy
connection_info = os.environ['CONNECTION_INFO']


# args for secure connection
engine = create_engine(connection_info, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })


def db_project(): 
# Starting new connection 
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM `projects`"))
  
  projects = []
  for row in result.all():
    projects.append(dict(row))

  return projects
