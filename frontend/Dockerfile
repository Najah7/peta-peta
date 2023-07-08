FROM node:18.16.1-bullseye

LABEL MAINTAINER="Project PetaPeta"

# RUN npm config set unsafe-perm true
RUN npm install -g npm
RUN npm install -g create-next-app
RUN npm install -g next
RUN mkdir /frontend

WORKDIR /frontend
COPY ./frontend /frontend

WORKDIR /frontend/petapeta

CMD sh -c "npm install && npm run dev"

