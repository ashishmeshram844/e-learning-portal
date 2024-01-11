FROM node
RUN apt-get -y update
WORKDIR /ui-app
COPY . .
RUN npm install

CMD ["npm","run","start"]
