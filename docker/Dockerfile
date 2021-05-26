# getting base image ubuntu
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

#Installing the dependencies
RUN apt-get update
RUN apt install -y apache2 python3.9 git libapache2-mod-wsgi-py3 \
    python3-mysqldb python3-pip
RUN python3 -m pip install django
RUN python3 -m pip install django-cors-headers
RUN python3 -m pip install django-environ
RUN python3 -m pip install Pillow
#RUN pip install django-environ
RUN apt install nano

RUN echo "LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so" >> /etc/apache2/apache2.conf
RUN echo "WSGIScriptAlias / /var/www/purple-planner/test_project/project_4/project/project/wsgi.py" >> /etc/apache2/apache2.conf
RUN echo "WSGIPythonPath /var/www/purple-planner/test_project/project_4/project" >> /etc/apache2/apache2.conf
RUN echo "<Directory /var/www/purple-planner/test_project/project_4/project>" >> /etc/apache2/apache2.conf
RUN echo "<Files wsgi.py>" >> /etc/apache2/apache2.conf
RUN echo "	Require all granted" >> /etc/apache2/apache2.conf
RUN echo "</Files>" >> /etc/apache2/apache2.conf
RUN echo "</Directory>" >> /etc/apache2/apache2.conf
RUN echo "ServerName 127.0.0.1" >> /etc/apache2/apache2.conf
RUN echo "Alias /static/ /var/www/purple-planner/test_project/project_4/project/staticfiles/" >> /etc/apache2/apache2.conf
RUN echo "Alias /media/ /var/www/purple-planner/test_project/project_4/project/media/" >> /etc/apache2/apache2.conf
RUN echo "<Directory /var/www/purple-planner/test_project/project_4/project/staticfiles>" >> /etc/apache2/apache2.conf
RUN echo "Require all granted" >> /etc/apache2/apache2.conf
RUN echo "</Directory>" >> /etc/apache2/apache2.conf
RUN echo "<Directory /var/www/purple-planner/test_project/project_4/project/media>" >> /etc/apache2/apache2.conf
RUN echo "Require all granted" >> /etc/apache2/apache2.conf
RUN echo "</Directory>" >> /etc/apache2/apache2.conf

COPY first_group_project /var/www/purple-planner

CMD service apache2 start && /bin/bash
