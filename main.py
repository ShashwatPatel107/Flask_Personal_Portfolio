from flask import Flask, render_template, jsonify
# jsonify takes an object and convert to json object

from database import db_project 

app = Flask(__name__)

  

@app.route("/")
def reptor_homepage():
  projects = db_project() # call function from database.py
  return render_template("app.html", projects=projects) 


  

# instead of list create JSON
@app.route("/api/projects")  #create new Endpoint
def json_projects():
  return jsonify(PROJECTS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

