FROM nginx:1.20-alpine
RUN mkdir /site
COPY /static /site/static
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]