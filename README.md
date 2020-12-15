I felt like finally delving into microservices architecture.

FastAPI description is found on https://fastapi.tiangolo.com. 
Find the coding in attached main.py file.

As for the dockerization:

1.) The "Dockerfile" needs to be placed in the project folder, so that "main.py" is in folder "app", while "Dockerfile" is on the same level as "app".
I have decided to build up the docker file using Python 3.7 as base image (as opposed to the short cuts provided in https://fastapi.tiangolo.com/deployment/docker/), so there was more to do. From the cmd, "docker build -t myimage ." has to be executed from within the project folder.
Make sure all files are closed and not in active use by any other applications when invoking the docker container using "docker run -d --name mycontainer -p 80:80 myimage".

Unfortunately https://fastapi.tiangolo.com/deployment/docker/ is not very verbose about how to actually access the container and its running applications themselves, so I relied on https://www.modius-techblog.de/linux/python-flask-app-mit-docker-deployen/ to retrieve the valuable information that 127.0.0.1:80/enums/Catan could test my application.

