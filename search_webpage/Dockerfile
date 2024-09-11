FROM node:18-alpine
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY package.json .
COPY package-lock.json .
RUN npm install 
COPY . .
CMD [ "npm", "start" ]