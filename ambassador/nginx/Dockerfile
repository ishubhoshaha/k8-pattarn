FROM nginx:alpine

#COPY local nginx config file to container
COPY ./nginx.conf /etc/nginx/nginx.conf

# Remove default nginx homepage
RUN rm -rf /usr/share/nginx/html/*

EXPOSE 3000

ENTRYPOINT ["nginx", "-g", "daemon off;"]

