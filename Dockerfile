#Stage 1
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
# Stage 2
FROM nginx:1.17.1-alpine
COPY --from=build /dist/budget-app /usr/share/nginx/html
