FROM ubuntu:trusty
MAINTAINER Patrick Spencer <pkspenc@gmail.com>

RUN apt-get update && apt-get install -y \
    software-properties-common

RUN apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ansible

# setting LANG=en_US.TUF-8 seems to fix a problem with ansible setting up postgres
ADD ./ansible /var/ansible
RUN cp /var/ansible/development.ansible-hosts /etc/ansible/hosts
RUN export LANG=en_US.UTF-8
RUN ansible-playbook /var/ansible/site.yml
