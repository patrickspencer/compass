FROM ubuntu:trusty
MAINTAINER Patrick Spencer <pkspenc@gmail.com>

RUN apt-get update && apt-get install -y \
    software-properties-common

RUN apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ansible

RUN mkdir /var/compass
ADD . /var/compass
RUN cp /var/compass/ansible/development.ansible-hosts /etc/ansible/hosts
