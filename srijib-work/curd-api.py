
from sqlalchemy import *
from flask import Flask, jsonify, request
import urllib
#from sqlalchemy.engine.url import URL
from sqlalchemy.orm import mapper, scoped_session, sessionmaker
import os

app=Flask(__name__)

engine = create_engine('mysql://'+os.environ['DBmy_USERNAME']+':'+os.environ['DBmy_PASSWORD']+'@127.0.0.1/info_invoice')

m=MetaData()

db_session=scoped_session(sessionmaker (autocommit=False,
                                        autoflush=False,
                                        bind=engine
))

conn=engine.connect()

class InvoiceSchema(object):
    query=db_session.query_property()
    m.create_all(bind=engine)

    def __init__(self, Circuit_ID=None, Verification_status=None, Payment_status=None):
        self.Circuit_ID=Circuit_ID
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

mapper(InvoiceSchema, schem)

@app.route('/create_schema')
def create():
#       schem.drop(engine)
#       inspector = inspect(engine)
#       return 'Table dropped'
        try:
                if not engine.dialect.has_table(engine, 'tbl_info_invoice'):
                        schem.create(engine)
#                       inspector = inspect(engine)
                        return 'Table craeted successfully.'
                else:
                        return 'Table was already created before.'
        except Exception as e:
                print(e)

@app.route('/update', methods=['POST'])
def update_by_id():
        try:
                data_by_id = InvoiceSchema.query.filter_by(Circuit_ID=str(request.json['CIRCUIT_ID'])).first()
                if data_by_id == None:
                        return 'Incorrect ID'
                else:
                        data_by_id.Verification_status = request.json['Verification_status']
                        data_by_id.Payment_status = request.json['Payment_status']
                        db_session.commit()
                        return 'Data Updated Successfully. \n'
        except Exception as e:
                print(e)

@app.route('/get', methods=['GET'])
def get_all():
        try:
                s = select([schem])
                results = conn.execute(s)
#               print(results)
                rows = results.cursor.fetchall()
#               print(rows)
                columns = results.cursor.description
#               print(columns)
                if rows:
                        result = [{columns[index][0]:column for index, column in enumerate(row)}   for row in rows]
                        return jsonify({'OUTPUT' : result})
                else:
                        return jsonify({'OUTPUT' : 'No records available.'})
        except Exception as e:
                print(e)

@app.route('/get_data_by_id', methods=['GET'])
def get_by_id():
        try:
#               id1 = str(request.json['CIRCUIT_ID'])
                s = select([schem], schem.c.Circuit_ID==str(request.json['CIRCUIT_ID']))
                results = conn.execute(s)
                rows = results.cursor.fetchall()
                columns = results.cursor.description
#               print(columns)
                if rows:
                        result = [{columns[index][0]:column for index, column in enumerate(row)}   for row in rows]
                        return jsonify({'OUTPUT' : result[0]})
                else:
                        return jsonify({'OUTPUT' : 'No records available for the given id '+str(request.json['CIRCUIT_ID'])})
        except Exception as e:
                print(e)

@app.route('/')
def main():
        return 'Welcome to the InfoOps CURD API.'

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8989, debug=True)
