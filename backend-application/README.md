# API Application
- This is a FastAPI Application where all apis are created
- This api's are integrated in frontend applications
- This apis can be integrated in any application like web,  android and ios also.

### Requirements for this application : 
- for running this application we only need python in our system
- for installation guide of python you can visit :  **https://www.python.org/downloads/**


### Setup application on docker : 
- If you already set upped whole application then no need to setup this application seperately
- make  sure docker is installed in your system
- if you want to setup this application only then use following commands
    1. **Setup of Database** : 
        
        This commands setup the mongo database in docker container and expose mongo on 27017 port 
        
            cd database/
            docker-compose up

    2. **Setup backend application :** 

        This command setup the backend api application in container and expose port 8001 on your local system to access apis into your local.

            cd backend-application/
            docker-compose up
### Application Running on : 
- **api server document available on**  : **http://localhost:8001/docs**


