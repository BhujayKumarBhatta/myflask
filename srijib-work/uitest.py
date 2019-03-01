from subprocess import check_output
try:
        a=check_output(["sudo", "curl", "-I", "http://10.174.112.79:8899/get"])
        if 'HTTP/1.1 200 OK' in a:
             b = check_output(["sudo", "curl", "http://10.174.112.79:8899/get"])
             if 'SERIAL_NO' in b:
                    print('SERIAL NO present in json')
             if 'DIVISION_NAME' in b:
                    print('DIVISION NAME  present in Json')
             if 'TSP_NAME' in b:
                    print('TSP NAME  present in json')
             if 'CIRCUIT_ID' in b:
                    print('CIRCUIT ID present in json')
except Exception as e:
          print (e)