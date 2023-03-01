from sqlalchemy import create_engine, text
import os 

db_connection_string = os.environ.get('DB_ACCESS_STRING')

connect_args = {
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
}

engine = create_engine(db_connection_string, connect_args=connect_args)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        result_all = result.all()
        print("TYPE -------- ", type(result_all[0]))
        return [dict(row._mapping) for row in result_all]
    

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
        rows = result.all()
        return dict(rows[0]._mapping) if len(rows) >= 0 else None
        