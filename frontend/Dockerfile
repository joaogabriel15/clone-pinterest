FROM node:20-alpine3.18
# Add a work directory
WORKDIR /usr/src/app
# Cache and Install dependencies
COPY package.json .

RUN npm install
# Copy app files
COPY . .
# Expose port

EXPOSE 3000

