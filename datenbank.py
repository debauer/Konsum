from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import and_
from sqlalchemy import select

connect_string = 'mysql+pymysql://strichliste:korkenzieher@strichliste.local:3306/strichliste'
Base = automap_base()
engine = create_engine(connect_string)
Base.prepare(engine, reflect=True)
User = Base.classes.User
Transaction = Base.classes.Transaction
Products = Base.classes.Products
session = Session(engine)


def test():
    connection = engine.connect()
    res = connection.execute(select([User]).where(
                and_(
                    User.NickName == "Korkenzieher",
                    User.UserPin == 1235
                )
            ))
    for row in res:
        print (row.UserID)
    connection.close()

test()