import os 

from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

connect_args = {
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
}


DB_CONNECTION_STRING = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(DB_CONNECTION_STRING, connect_args=connect_args)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        result_all = result.all()
        return [dict(row._mapping) for row in result_all]
    

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
        rows = result.all()
        return dict(rows[0]._mapping) if len(rows) >= 0 else None
    

def load_applications_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM applications"))
        result_all = result.all()
        return [dict(row._mapping) for row in result_all]
    

def add_application_to_db(id, data):
    with engine.connect() as conn:
        
        data = data.to_dict()
        data['job_id'] = id 
        
        query = text("""INSERT INTO applications (job_id, name, surname, email, linkedin_url, education, work_experience, resume_url)
                     VALUES(:job_id, :name, :surname, :email, :linkedin_url, :education, :work_experience, :resume_url)""")
        
        conn.execute(query, **data)
        
        