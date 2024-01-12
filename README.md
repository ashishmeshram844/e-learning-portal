# e-learning-portal

- This Website main Goal is provide projects and e-learning tutorials available to the people in one website. 
- You can find projects related to different field. 
- This Website contain the information which you are looking for kindly have a detailed look over the site. This in turn helps you to enhance your skill.
### Requirements : 
- Only Need Docker this will setup the project automatically on docker
- docker (24.0.7)
- You can get help from official docker site for installation of docker
- **https://docs.docker.com/get-docker/**
- Install Docker in ubuntu using snap store :

        sudo snap refresh --revision=2893 docker
        sudo apt install docker-compose


### Start Project : 
- To run project you need to run only single command in this single command your project is set and configured on containers in docker and expose needed ports on your local system.
- following command is use to start your project on docker containers and expose the ports for usage of the project in local system

        make up

### Stop Project : 
- To stop project which is running on your docker containers
- following  command is use to stop the project which are running on docker containers

        make down



### All Required Applications running on following ports :
- **API Application** :  - **http://localhost:8001**

- **UI Application** : - **http://localhost:8000**

- **Mongo DB URI** : - **mongodb://root:Ashish123@mongo:27017/**
