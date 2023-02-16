import os
import sqlalchemy
from sqlalchemy import create_engine, engine, text
# connect to my sql with sqlalchemy


# database information goes here
# HOST, USER, Pass
connection_string = "mysql+pymysql://50tw8c2rvl6qzgut2xrw:pscale_pw_lFhP4LmriCPcBFAevspt9B6d2zaTBay9tlVVN40gFZ0@us-east.connect.psdb.cloud/shashwat_projects?charset=utf8mb4"

engine = create_engine(connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def db_project():
  # Starting new connection
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM `shashwat_project`"))

  projects = []
  for row in result.all():
    projects.append(dict(row))
    # Projects is rows of database table
  return projects
