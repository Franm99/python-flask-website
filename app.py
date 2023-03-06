from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, load_applications_from_db

app = Flask(__name__)

COMPANY_NAME = '<YOUR COMPANY NAME>'
  
  
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name=COMPANY_NAME)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(load_jobs_from_db())


@app.route("/api/applications")
def list_applications():
    return jsonify(load_applications_from_db())


@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)
    
    if not job:
        return "Not Found", 404
    
    return render_template('jobpage.html', job=job, company_name=COMPANY_NAME)


@app.route("/job/<int:id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    
    print(job)
    
    add_application_to_db(id, data)
    
    return render_template('application_submitted.html', application=data, company_name=COMPANY_NAME, job=job)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)