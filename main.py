from flask import Flask, render_template, jsonify
# jsonify takes an object and convert to json object

app = Flask(__name__)



from database import engine # *******
from sqlalchemy import text # *******
def db_project(): 
# Starting new connection 
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM `projects`"))
  
  projects = []
  for row in result.all():
    projects.append(dict(row))

  return projects

  

@app.route("/")
def reptor_homepage():
  projects = db_project()
  return render_template("app.html", projects=projects)


# instead of list create JSON
@app.route("/api/projects")  #create new Endpoint
def json_projects():
  return jsonify(PROJECTS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

  #  *********************************************************

#   from flask_sqlalchemy import SQLAlchemy

# # from app import db

# from Flask_Personal_Portfolio import db as rdb
# rdb.create_all()

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///raptor_projects.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
# db = SQLAlchemy(app)

# class Projects(db.Model):
#   Project_ID = db.Column(db.Integer, primary_key=True)
#   Title = db.Column(db.String(255), nullable=False)
#   Name = db.Column(db.String(255), nullable=False)
#   Start_date = db.Column(db.Date)
#   Status = db.Column(db.String(255))
#   Key_Learning = db.Column(db.String(255))
#   Link = db.Column(db.String(255))

#     def __repr__(self) -> str:
#     project_info = f"ID:{self.Project_ID}, {self.Title},{self.Name}, {self.Start_date},{self.Status}, Learnings: {self.Key_Learning}, {self.Link}"
#     return project_info
