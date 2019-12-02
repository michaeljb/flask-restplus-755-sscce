FROM nginx:1.14.0

RUN apt-get update && apt-get install -y openssl

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./frp-sscce.conf /etc/nginx/conf.d/
COPY index.html /usr/share/nginx/html/

RUN mkdir /etc/nginx/ssl && openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl\
/nginx.crt -subj "/CN=michaeljb"

# RUN useradd --uid 1000 --user-group vagrant && \
#     touch /var/run/nginx.pid && \
#     chown -R vagrant:vagrant /var/run/nginx.pid && \
#     chown -R vagrant:vagrant /var/cache/nginx && \
#     chown -R vagrant:vagrant /etc/nginx
