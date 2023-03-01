from flask import Flask, render_template, jsonify

app = Flask(__name__)

COMPANY_NAME = 'Kabrito'
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'company': 'Jovian',
        'location': 'Barcelona, Spain',
        'salary': '2.000 E'
        
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'company': 'Adesluz S.L.',
        'location': 'Cuenca, Spain',
        'salary': '2.200 E'
        
    },
    {
        'id': 3,
        'title': 'Waiter/Waitress',
        'company': 'Los Amigos Cervecería', 
        'location': 'Málaga, Spain',
        
    },
    {
        'id': 4,
        'title': 'Full-Stack Developer',
        'company': 'Tiktok',
        'location': 'Remote',
        'salary': '3.500 E'
        
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name=COMPANY_NAME)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)