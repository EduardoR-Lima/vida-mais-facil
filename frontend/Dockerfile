FROM node:22.19.0-slim AS build-stage

WORKDIR /app
COPY ./vida-mais-facil/package*.json .
RUN npm install
COPY ./vida-mais-facil .
RUN npm run build

FROM nginx:1.29.3-alpine AS production-stage

RUN mkdir /app
COPY --from=build-stage ./app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80