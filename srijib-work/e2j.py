# -*- coding: utf-8 -*-
"""
Excel to Json converter


"""

import xlrd
import json
import pprint
class Xlstojson(object):
        def converter(self):
                data = []
                book = xlrd.open_workbook('HOTELAprJun2018.xlsx')
                for sheet in book.sheets():
                        for i in range(1, sheet.nrows-1):
                                row1 = sheet.row_values(i)
                                data.append(dict({'Customer': str(row1[1]),
                                                'Name_1': str(row1[2]),
                                                'Invoice_No' : str(row1[3]),
                                                'Account_No' : str(row1[4]),
                                                'Circuit_ID' : str(row1[5]),
                                                'City' : str(row1[6]),
                                                'Side_Location' : str(row1[7]),
                                                'Speed' : str(row1[8]),
                                                'ARC' : row1[9],
                                                'GST_No' : str(row1[10]),
                                                'Division' : str(row1[11]),
                                                'Period' : str(row1[12]),
                                                'Invoice_Date' : str(row1[13]),
                                                'Tax_Name' : str(row1[14]),
                                                'Total' : row1[15],
                                                'SERVICE_TYPE' : str(row1[16]),
                                                'INFOBAHN_REMARKS' : str(row1[17])}))
#               pprint.pprint(data)
                return json.dumps(data)
