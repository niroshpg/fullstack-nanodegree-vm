# Reset database and populate initial values

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_set_schema import *

engine = create_engine('sqlite:///catalogue.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Category).delete()
session.query(Item).delete()

category1 = Category(title="Soccer")
session.add(category1)
session.commit()

category2 = Category(title="Basketball")
session.add(category2)
session.commit()

category3 = Category(title="Football")
session.add(category3)
session.commit()

item1 = Item(
    # user=user1,
    category=category1,
    title="Soccuer Ball",
    description=(
        "Soccuer Ball "
        "description "
    ),
    author="admin"
)
session.add(item1)
session.commit()

session.commit()

print "Reset database for initial setup"
