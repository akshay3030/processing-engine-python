# python-processing-engine

# Python Flask Example

#1.Install Python 2.7:

https://www.python.org/downloads/release/python-2711/

Add python directory to the PATH.

#Check pip package versions
pip freeze | grep Flask

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
docker build -t akshay3030/python-processing-engine:dataframe .

Run in normal-mode : docker run -p 9091:5000 akshay3030/python-processing-engine

Run in detached-mode : docker run -d -p 9091:5000 akshay3030/python-processing-engine


Run a command inside docker container:

docker exec -it {docker-ps-id} /bin/bash

docker exec -it {docker-ps-id} ls

#Docker Compose (Note: Use Docker Swarm & docker-machine to setup the cluster mode ,run Compose on a Swarm cluster)

docker-compose up

docker-compose down

# ELB with Docker on ECS
https://aws.amazon.com/blogs/compute/microservice-delivery-with-amazon-ecs-and-application-load-balancers/

# Input Json for latest run

url: http://localhost:5000/calculate?model_name=valuation
{"input1":2,"input2":3,"input3":4,"input4":5}	

#Docker Swarm Example

https://rominirani.com/docker-swarm-tutorial-b67470cf8872

docker-machine create --driver virtualbox <machine-name>

docker swarm init --advertise-addr 192.168.99.100 (start swarm manager)

docker swarm join --tokens <ssh-keys> <ip>:<2377> (from workernode to join master)

docker-machine ssh <machine-name>

eval $(docker-machine evn <machine>) (generate new ips)

docker service create --replicas 5 -p 9091:5000 --name flask akshay3030/python-processing-engine:dataframe  (create 5 copies of this container)

docker service ls

#ECS service is running ecs task in cluster mode
