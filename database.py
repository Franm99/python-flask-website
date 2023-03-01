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
        print(result.all())
        print(result.all()[0])
        print(dict(result.all()[0]))
        return [dict(row) for row in result.all()]
