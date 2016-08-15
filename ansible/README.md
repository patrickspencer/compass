Requirements: Ubuntu 14.04

Install ansible:
```
apt-get update
apt-get install -y software-properties-common
apt-add-repository ppa:ansible/ansible
apt-get update
apt-get install ansible
```

Make folders:
```
mkdir /var/compass
mkdir /var/compass/ansible
```

For development setup do the following:
```
cp /var/compass/ansible/development.ansible-hosts /etc/ansible/hosts
```
