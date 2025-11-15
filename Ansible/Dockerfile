# Imagen base de Ubuntu
FROM ubuntu:22.04

# Evita preguntas durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Actualizamos e instalamos SSH, sudo y utilidades básicas
RUN apt-get update && apt-get install -y \
    openssh-server \
    sudo \
    python3 \
    systemd \
    && apt-get clean

# Creamos el usuario ansible con password 'ansible'
RUN useradd -ms /bin/bash ansible && echo "ansible:ansible" | chpasswd

# Damos privilegios sudo sin pedir password
RUN echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Configuramos SSH
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

# Exponemos el puerto SSH
EXPOSE 22

# Comando al iniciar el contenedor
CMD ["/usr/sbin/sshd", "-D"]
