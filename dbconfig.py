from sqlmodel import create_engine
import dbschema

sql_file_name = "User.db"

sql_url = f"sqlite:///{sql_file_name}"

engine = create_engine(sql_url, echo=True)