from flask import Flask, render_template, jsonify
# jsonify takes an object and convert to json object

app = Flask(__name__)

# Project database
PROJECTS = [{
  "Title": "Web-Scraping",
  "Name": "Scraping Youtube Using Selenium",
  "Start_date": "Oct-2022",
  "Key_learnings": ["Python", "Selenium", "BeautifulSoup"],
  "Link": "WS_colab_URL"
}, {
  "Title":
  "Web-Development",
  "Name":
  "Personal_Portfolio_Website",
  "Start_date":
  "Nov-2022",
  "Key_learnings": ["Python", "Flask", "SQL", "HTML/CSS", "JavaScript"],
  "Link":
  "WD_Replit_URL"
}, {
  "Title": "Data Visualization And Analysis",
  "Name": "Youtube Trand Analysis",
  "Start_date": "Nov-2022",
  "Key_learnings": ["Python", "Excel", "Tableau", "Numpy"],
  "Link": "DVA_URL"
}]


@app.route("/")
def reptor_homepage():
  return render_template("app.html", projects=PROJECTS)


# instead of list create JSON
@app.route("/projects")  #create new Endpoint
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
