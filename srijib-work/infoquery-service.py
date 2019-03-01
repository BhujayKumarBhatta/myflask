from sqlalchemy import *
from flask import Flask, jsonify, request
import urllib
import pyodbc
from sqlalchemy.orm import mapper, scoped_session, sessionmaker
import os

app=Flask(__name__)

quoted = urllib.quote_plus('DRIVER={FreeTDS};Server=10.10.10.26;Database=infooper;UID='+os.environ['DB_USERNAME']+';PWD='+os.environ['DB_PASSWORD']+';TDS_Version=7.0;Port=1433;')

engine=create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

metadata=MetaData()

db_session=scoped_session(sessionmaker (autocommit=False,
                                        autoflush=False,
                                        bind=engine
))

conn=engine.connect()

class DBSchema(object):
    query=db_session.query_property()
    metadata.create_all(bind=engine)

    def __init__(self, serial_no=None, circuit_id=None, division_name=None, tsp_name=None):
        self.serial_no=serial_no
        self.circuit_id=circuit_id
        self.division_name=division_name
        self.tsp_name=tsp_name

#    def __repr__(self):
#        return '<Div %r>' % self.division_name

schem=Table('vw_comm_links', metadata,
        Column('serial_no', Integer, primary_key=True),
        Column('circuit_id', Integer),
        Column('division_name', String(120)),
        Column('tsp_name', String(120)))

mapper(DBSchema, schem)

@app.route('/get')
def main():
         ob = []
         s = select([schem])
         result = conn.execute(s)
         for row in result:
             data = dict({'SERIAL_NO':str(row[0]), 'CIRCUIT_ID':str(row[1]), 'DIVISION_NAME':str(row[2]), 'TSP_NAME':str(row[3])})
             ob.append(data)
         return jsonify({'Output' : ob})

@app.route('/get_by_id', methods=['POST'])
def get_by_id():
        try:
                data_by_id = DBSchema.query.filter_by(circuit_id=str(request.json['CIRCUIT_ID'])).first()
                if data_by_id == None:
                        return 'Incorrect ID'
                else:
                        data = dict({'SERIAL_NO': data_by_id.serial_no, 'CIRCUIT_ID':data_by_id.circuit_id, 'DIVISION_NAME':data_by_id.division_name, 'TSP_NAME':data_by_id.tsp_name})
                        return jsonify({'OUTPUT' : data})
        except Exception as e:
                print(e)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8899, debug=True)
