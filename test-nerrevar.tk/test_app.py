import os

import falcon

from sqlalchemy import create_engine, Column, Integer, Time, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from react.render import render_component

session = sessionmaker()
engine = create_engine("postgresql+psycopg2://user:01050062@localhost:5432/userdb",
            client_encoding="utf-8")
            
session.configure(bind=engine)

base = declarative_base()

class event(base):
    __tablename__ = "event"
    
    id = Column(Integer, primary_key = True)
    time = Column(Time)
    caption = Column(String(100))
    
    def __init__(self, time, caption):
        self.time = time
        self.caption = caption
    
    def __repr__(self):
        return "<event(id='%s', time='%s', caption='%s')>" % (
                self.id, self.time, self.caption)


class Test_app(object):
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        
        event_table = event()
        events = session.query(event).order_by(event.time).all()
        for e in events:
            print (e.time + e.caption)
        
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "hello"

        

test_app = Test_app()
app = falcon.API()
app.add_route("/", test_app)