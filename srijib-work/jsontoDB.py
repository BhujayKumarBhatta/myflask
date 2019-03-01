"""
Json to DB writer raw data as string


"""
from sqlalchemy import *
from flask import Flask, json
from e2j import Xlstojson
import urllib
import pyodbc
from sqlalchemy.orm import mapper, scoped_session, sessionmaker
import os
app=Flask(__name__)
xlsjson = Xlstojson()
engine = create_engine('mysql://'+os.environ['DBmy_USERNAME']+':'+os.environ['DBmy_PASSWORD']+'@127.0.0.1/info_invoice')
conn = engine.connect()
m=MetaData()
db_session=scoped_session(sessionmaker (autocommit=False,
                                        autoflush=False,
                                        bind=engine
))
conn=engine.connect()
class DBSchema(object):
    query=db_session.query_property()
    m.create_all(bind=engine)
    def __init__(self, Customer=None, Name_1=None, Invoice_No=None, Account_No=None, Circuit_ID=None, City=None, Side_Location=None, Speed=None, ARC=None, GST_No=None,Division=None, Period=None, Invoice_Date=None, Tax_Name=None, Total=None, SERVICE_TYPE=None, INFOBAHN_REMARKS=None, Verification_status=None, Payment_status=None):
        self.Customer=Customer
        self.Name_1=Name_1
        self.Invoice_No=Invoice_No
        self.Account_No=Account_No
        self.Circuit_ID=Circuit_ID
        self.City=City
        self.Side_Location=Side_Location
        self.Speed=Speed
        self.ARC=ARC
        self.GST_No=GST_No
        self.Division=Division
        self.Period=Period
        self.Invoice_Date=Invoice_Date
        self.Tax_Name=Tax_Name
        self.Total=Total
        self.SERVICE_TYPE=SERVICE_TYPE
        self.INFOBAHN_REMARKS=INFOBAHN_REMARKS
        self.Verification_status=Verification_status
        self.Payment_status=Payment_status


#    def __repr__(self):
#        return '<Div %r>' % self.div_name

schem = Table('tbl_info_invoice', m,
                                Column('SL_No', Integer, primary_key=True),
                                Column('Customer', String(120)),
                                Column('Name_1', String(120)),
                                Column('Invoice_No', String(120)),
                                Column('Account_No', String(250)),
                                Column('Circuit_ID', String(250)),
                                Column('City', String(250)),
                                Column('Side_Location', String(250)),
                                Column('Speed', String(120)),
                                Column('ARC', Integer),
                                Column('GST_No', String(120)),
                                Column('Division', String(120)),
                                Column('Period', String(120)),
                                Column('Invoice_Date', Date),
                                Column('Tax_Name', String(120)),
                                Column('Total', Integer),
                                Column('SERVICE_TYPE', String(120)),
                                Column('INFOBAHN_REMARKS', String(120)),
                                Column('Verification_status', String(120)),
                                Column('Payment_status', String(120)))


mapper(DBSchema, schem)

@app.route('/insert')
def main():
#       print(xlsjson.converter())
        json_str = json.loads(xlsjson.converter())
#       print(json_str)
        for i in json_str:
                print(i)
                js_data=DBSchema(**i)
                db_session.add(js_data)
                db_session.commit()
        return 'Successfully inserted data into table.'

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8989, debug=True)
