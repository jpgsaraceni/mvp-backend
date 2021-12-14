FROM node:14

# Create app directory
WORKDIR /usr/app

# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY package*.json ./
COPY prisma ./prisma/

# Install app dependencies
RUN npm install

COPY . .

EXPOSE 4000
# 👇 new migrate and start app script
CMD [ "npm", "run", "build:docker" ]