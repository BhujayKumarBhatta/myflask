virtualenv -p python3 ~/venvp3

source ~/venvp3/bin/activate

git clone ....

cd tokenleader

pip install --upgrade pip

pip install -r requirement.txt

sshkeygen < press enter to select all defaults>

python -m unittest discover tests

export FLASK_APP='app_run.py'

flask run

To generate token :

curl -X POST -d '{"username": "susan", "password": "mysecret"}' \ -H "Content-Type: Application/json" localhost:5000/token/gettoken

To verify token:

curl -X POST -d '{"auth_token":" "}' -H "Content-Type: Application/json" localhost:5000/token/verify_token

for db migration

flask db init flask db migrate -m < COMMENT > flask db upgrde