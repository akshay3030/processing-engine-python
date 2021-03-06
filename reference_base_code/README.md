# Python Flask Example

1.Install Python 2.7:

https://www.python.org/downloads/release/python-2711/

Add python directory to the PATH.


2. Install pip:

python get-pip.py install

3. Install Flask.

 python -m pip install --proxy http://proxy.kdc.capitalone.com:8099 Flask

for SSL:

python -m pip install --proxy http://proxy.kdc.capitalone.com:8099 Flask-SSLify

python -m pip install --proxy http://proxy.kdc.capitalone.com:8099 pyopenssl

Run from gitshell to generate key and certificate:

openssl req -new -x509 -keyout key.pem -out server.pem -days 365 -nodes

openssl req -new -x509 -keyout clientKey.pem -out client.pem -days 365 -nodes

4. To run the sample server:


python helloServer.py

Run Model dynamically, using python dynamically load a module:

curl -H "Content-Type: application/json" -X POST -d '{"x":10,"y":30}' http://localhost:8075/calculate?model_name=multiply

curl -H "Content-Type: application/json" -X POST -d '{"x":10,"y":30}' http://localhost:8075/calculate?model_name=add

5. To access it:

GET Request Sample:

http://localhost:5000/hello/mito

Sample POST Request:


curl -H "Content-Type: application/json" -X POST -d '{"x":10,"y":30}' http://localhost:5000/calculate

or

curl -H "Content-Type: application/json" -X POST -d '{"name":"Darren"}' http://localhost:5000/hello2


6. To run https server:

Be sure to have key.pem and server.pem in the directory from where you are executing:

python helloServerSS.py

access it: https://localhost
will show the listing of the current directory.

7. to Run https API:
Be sure to have key.pem and server.pem in the directory from where you are executing:

python sslAPI.py

access it: https://localhost/hello/mito1

8. to Run redirect request:

Be sure to have key.pem and server.pem in the directory from where you are executing:

python redirectAPI.py

access it: https://localhost
or http://localhost

9. two way ssl:

python twoWayServer.py

python twoWayClient.py
