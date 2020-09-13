FROM node:current-alpine AS build
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
RUN npm install -g @angular/cli
RUN npm install bulma
RUN npm uninstall node-sass && npm install node-sass
EXPOSE 4200
CMD [ "npm", "start" ]
COPY . .
RUN ng build
