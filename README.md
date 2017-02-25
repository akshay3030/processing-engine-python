# python-processing-engine

# Python Flask Example

#1.Install Python 2.7:

https://www.python.org/downloads/release/python-2711/

Add python directory to the PATH.


#2. Install pip:

python get-pip.py install

#3. Install Flask.

python -m pip install --proxy {host:port} Flask

for SSL:

python -m pip install --proxy {host:port} Flask-SSLify

python -m pip install --proxy {host:port} pyopenssl

Run from gitshell to generate key and certificate:

openssl req -new -x509 -keyout key.pem -out server.pem -days 365 -nodes

openssl req -new -x509 -keyout clientKey.pem -out client.pem -days 365 -nodes

#4. To run the Scoring Engine server:

python ScoringServer.py

Run Model dynamically, using python dynamically load a module:

curl -H "Content-Type: application/json" -X POST -d '{"x":10,"y":30}' http://localhost:9090/calculate?model_name=multiply

curl -H "Content-Type: application/json" -X POST -d '{"x":10,"y":30}' http://localhost:9090/calculate?model_name=add

#Docker Instructions
docker build -t akshay3030/python-processing-engine .

Run in normal-mode : docker run -p 9091:5000 akshay3030/python-processing-engine

Run in detached-mode : docker run -d -p 9091:5000 akshay3030/python-processing-engine


Run a command inside docker container:

docker exec -it {docker-ps-id} /bin/bash

docker exec -it {docker-ps-id} ls


# ELB with Docker on ECS
https://aws.amazon.com/blogs/compute/microservice-delivery-with-amazon-ecs-and-application-load-balancers/
