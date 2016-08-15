#!/usr/bin/env bash

# Should work on Debian based systems

apt-get update
apt-get install -y software-properties-common
apt-add-repository ppa:ansible/ansible
apt-get update
apt-get install ansible
cp ../ansible/development.ansible-hosts /etc/ansible/hosts
