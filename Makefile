
up:
	cd backend-application && sudo docker-compose up --build -d && cd ..
	cd front-application && sudo docker-compose up --build -d && cd ..
down:
	cd backend-application && sudo docker-compose down && cd ..
	cd front-application && sudo docker-compose down && cd ..


