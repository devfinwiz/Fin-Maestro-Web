FROM node:16.11.1-alpine3.14 as build

WORKDIR /src
ENV PATH /src/node_modules/.bin:$PATH
COPY package*.json ./
RUN npm install
COPY . ./


ARG REACT_APP_BACKEND_ADDRESS
ENV REACT_APP_BACKEND_ADDRESS=$REACT_APP_BACKEND_ADDRESS



RUN npm run build
# production environment
FROM nginx:1.19.10-alpine 

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /src/build /usr/share/nginx/html


EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
