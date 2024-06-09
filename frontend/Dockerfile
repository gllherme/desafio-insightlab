FROM node:20-alpine

WORKDIR /code

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

RUN npx next build

CMD ["npx", "next", "start"]