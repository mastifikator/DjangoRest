FROM python:3
LABEL maintainer="N1k0"
ENV HTTP_PROXY="http://bproxy.msk.mts.ru:3128"
ENV HTTPS_PROXY="http://bproxy.msk.mts.ru:3128"
ENV NO_PROXY="backend1, backend2"

RUN echo 'Acquire::http::Proxy "http://bproxy.msk.mts.ru:3128";' > /etc/apt/apt.conf.d/proxy

RUN apt-get update && apt-get install -y openssh-server sudo
RUN mkdir /var/run/sshd
RUN echo 'root:123456' | chpasswd
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

COPY ansible_master_rsa.pub /root/.ssh/ansible_master_rsa.pub
RUN cat /root/.ssh/ansible_master_rsa.pub >> /root/.ssh/authorized_keys

EXPOSE 22 8001 8002 8003

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]
