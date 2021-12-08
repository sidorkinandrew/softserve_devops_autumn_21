FROM alpine:latest

RUN apk update && apk upgrade && apk add apache2 openrc curl

CMD /usr/sbin/httpd -D FOREGROUND
