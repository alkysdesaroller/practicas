FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y openssh-server python3 sudo apt-utils ca-certificates && \
    update-ca-certificates

RUN useradd -ms /bin/bash ansible \
    && echo 'ansible:ansible' | chpasswd \
    && adduser ansible sudo

RUN echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN mkdir /var/run/sshd
EXPOSE 22
EXPOSE 80

CMD ["/usr/sbin/sshd", "-D"]
