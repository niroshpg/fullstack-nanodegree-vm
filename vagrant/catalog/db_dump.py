# Reset database and populate initial values
from flask import (Flask, jsonify)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_set_schema import *

engine = create_engine('sqlite:///catalogue.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

print "DB content:"

app = Flask(__name__)
with app.app_context():
    catergoriesSerielized = [i.serialize for i in session.query(Category).all()]
    print jsonify(categories=catergoriesSerielized).get_data(as_text=True)

    itemsSerielized = [i.serialize for i in session.query(Item).all()]
    print jsonify(Items=itemsSerielized).get_data(as_text=True)

print "over"
session.commit()
