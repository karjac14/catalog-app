from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item, User
import datetime

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="John Smith", email="JohnSmith4567@email.com",
             picture='https://pbs.twimg.com/profile_images/\
             2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# for Women's Wear
category1 = Category(user_id=1, name="Women's Wear")

session.add(category1)
session.commit()

item2 = Item(
    user_id=1, name="Tops", description="Great top for every day wear",
    price="7.50", category=category1, created_date=datetime.datetime.now()
    )

session.add(item2)
session.commit()


item1 = Item(
    user_id=1, name="Blouses", description="Colorful clothes you will love",
    price="2.99", category=category1, created_date=datetime.datetime.now()
    )

session.add(item1)
session.commit()

item2 = Item(
    user_id=1, name="Sweaters", description="Nice tops for cool weather",
    price="5.50", category=category1, created_date=datetime.datetime.now()
    )

session.add(item2)
session.commit()

item3 = Item(
    user_id=1, name="Dresses", description="Fancy dresses for everyone",
    price="3.99", category=category1, created_date=datetime.datetime.now()
    )

session.add(item3)
session.commit()

item4 = Item(
    user_id=1, name="Pants", description="Comfy pants for everyday use",
    price="7.99", category=category1, created_date=datetime.datetime.now()
    )

session.add(item4)
session.commit()


# for Men's Wear
category2 = Category(user_id=1, name="Men's Wear")

session.add(category2)
session.commit()


item1 = Item(
    user_id=1, name="Shirts",
    description="Great wear everyday made with 100% cotton",
    price="7.99", category=category2, created_date=datetime.datetime.now()
    )

session.add(item1)
session.commit()

item2 = Item(
    user_id=1, name="Jeans",
    description="Nice streatchable denims just eveyone loves",
    price="$25", category=category2, created_date=datetime.datetime.now()
    )

session.add(item2)
session.commit()

item3 = Item(
    user_id=1, name="Cargo Shorts",
    description="Cool looking shorts (cuts above the knee)",
    price="15", category=category2, created_date=datetime.datetime.now()
    )


# for Childrens
category3 = Category(user_id=1, name="Children's Wear")

session.add(category3)
session.commit()


item1 = Item(
    user_id=1, name="Polo kids",
    description="Nice and colorful shirts for the cool kids",
    price="5.99", category=category3, created_date=datetime.datetime.now()
    )

session.add(item1)
session.commit()

item2 = Item(
    user_id=1, name="Caps",
    description="Colorful caps best for outdoor activities",
    price="5.99", category=category3, created_date=datetime.datetime.now()
    )

session.add(item2)
session.commit()


item4 = Item(
    user_id=1, name="Joggers",
    description="Soft Jeans for your kids",
    price="6.95", category=category3, created_date=datetime.datetime.now()
    )

session.add(item4)
session.commit()


print "manually added items in the Catalog!"
