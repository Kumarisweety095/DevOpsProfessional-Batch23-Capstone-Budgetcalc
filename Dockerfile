#Stage 1
FROM node:current-alpine as build
RUN mkdir -p /app
WORKDIR app
COPY package.json /app
RUN npm install
RUN npm install -g @angular/cli
RUN npm install bulma
RUN npm uninstall node-sass && npm install node-sass
COPY . /app
RUN ng build
# Stage 2
FROM nginx:1.17.1-alpine
COPY --from=build /app/dist/budget-app /usr/share/nginx/html
