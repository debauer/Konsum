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


def authenticate_pin(name="testposplsignore",pin= 12345678):
    connection = engine.connect()
    res =connection.execute(select([User]).where(
                and_(
                    User.NickName == name ,
                    User.UserPin == pin
                )
            ))
    if len(res._saved_cursor._result.rows) != 0 :
        print("success")
        return True
    else:
        print("fail")
        return False
    connection.close()

def authenticate_rfid(rfid="asdasdadasdasd"):
    connection = engine.connect()
    res =connection.execute(select([User]).where(
                    User.KartenID == rfid
            ))
    if len(res._saved_cursor._result.rows) != 0 :
        print("success")
        return True
    else:
        print("fail")
        return False
    connection.close()

def getBalance(UserID= 0):
    connection = engine.connect()
    res =connection.execute(select([Transaction]).where(
        
    ))
    if len(res._saved_cursor._result.rows) != 0 :
        print("success")
        return True
    else:
        print("fail")
        return False
    connection.close()