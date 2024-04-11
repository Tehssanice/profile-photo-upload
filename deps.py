from dbconfig import engine
from sqlmodel import Session


def get_session():
    session = Session(engine)
    return session