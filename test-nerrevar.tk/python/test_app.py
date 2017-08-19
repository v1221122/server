import os
import json

import falcon

from sqlalchemy import create_engine, Column, Integer, Time, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from react.render import render_component

session = sessionmaker()

engine = create_engine("postgresql+psycopg2://user1:01050062@localhost:5432/userdb",
                client_encoding="utf-8")
session.configure(bind=engine)

base = declarative_base()

class Event(base):
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
    def on_get(self, req, resp):
        sess = session()
        data = sess.query(Event).order_by(Event.time).add_columns(Event.time, Event.caption)
        events = []
        for item in data:
            event = dict([("time", str(item.time)), ("caption", str(item.caption))])
            events.append(event)
            
        resp.body = json.dumps(events)
        resp.set_header("Access-Control-Allow-Origin", "http://localhost:3000, http://localhost:5000")
        resp.status = falcon.HTTP_200
        sess.close()

    def on_post(self, req, resp):
        data = json.load(req.stream)
        event = Event(data["time"], data["caption"])
        
        sess = session()
        sess.add(event)
        sess.commit()
        
        resp.body = "inserted"
        resp.set_header("Access-Control-Allow-Origin", "http://localhost:3000, http://localhost:5000")
        resp.status = falcon.HTTP_200
        
        sess.close()

        
    def on_options(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.append_header("Access-Control-Allow-Origin", "http://localhost:3000, http://localhost:5000")
        resp.append_header("Access-Control-Allow-Method", "POST, GET, OPTIONS")
        resp.append_header("Access-Control-Allow-Headers", "Content-Type")
    
class Change_time_app(object):
    def on_post(self, req, resp):
        data = json.load(req.stream)
    
        sess = session()
    
        event = sess.query(Event).filter_by(caption=data["caption"]).first()
        event.time = data["time"]
        
        sess.add(event)
        sess.commit()
    
        resp.body = "updated"
        resp.set_header("Access-Control-Allow-Origin", "http://localhost:3000, http://localhost:5000")
        resp.status = falcon.HTTP_200
        
        sess.close()
    
class Delete_app(object):
    def on_post(self, req, resp):
        data = json.load(req.stream)
    
        sess = session()
    
        event = sess.query(Event).filter_by(caption=data["caption"], time=data["time"]).first()
        
        sess.delete(event)
        sess.commit()
    
        resp.body = "deleted"
        resp.set_header("Access-Control-Allow-Origin", "http://localhost:3000, http://localhost:5000")
        resp.status = falcon.HTTP_200
        
        sess.close()
    
test_app = Test_app()
change_time_app = Change_time_app()
delete_app = Delete_app()

app = falcon.API()
app.add_route("/events", test_app)
app.add_route("/change_time", change_time_app)
app.add_route("/delete", delete_app)