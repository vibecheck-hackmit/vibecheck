FROM node:20-alpine3.18
WORKDIR /app
COPY frontend .
EXPOSE 3000
RUN npm install --force
RUN npm run build
CMD ["npm","run","start"]
