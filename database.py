from sqlalchemy import create_engine, text
import os 

db_connection_string = os.environ.get('DB_ACCESS_STRING')

print(db_connection_string)

connect_args = {
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
}

engine = create_engine(db_connection_string, connect_args=connect_args)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        return [dict(row) for row in result.all()]
