from subprocess import check_output, check_call
try:
        a=check_output(["sudo", "curl", "-I", "http://10.174.112.79:8989/"])
        if 'HTTP/1.1 200 OK' in a:
             b = check_output(["sudo", "curl", "http://10.174.112.79:8989/"])
             if 'Welcome to the InfoOps CURD API.' in b:
                    print('Output OK')
             else:
                        print('Output Not OK')
        c = check_output(["sudo", "curl", "-I", "http://10.174.112.79:8989/get"])
        if 'CIRCUIT_ID' in c:
                print('Getting Circuit ID')
        d = check_call(["sudo", "curl", "-i", "-H", "Content-Type: application/json", "-X", "GET", "-d", '{"CIRCUIT_ID":"091NEWD623007456829"}', "http://10.174.112.79:8989/get_data_by_id"])
        if d!=None:
                print(d)

        e = check_call(["sudo", "curl", "-i", "-H", "Content-Type: application/json", "-X", "POST", "-d", '{"CIRCUIT_ID":"091NEWD623007456829", "Verification_status": "OK", "Payment_status": "Paid"}', "http://10.174.112.79:8989/update"])
        if e!=None:
                print(e)
except Exception as e:
          print (e)
