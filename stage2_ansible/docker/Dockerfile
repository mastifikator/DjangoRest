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

COPY ansible1_master_rsa.pub /root/.ssh/ansible1_master_rsa.pub
COPY ansible2_master_rsa.pub /root/.ssh/ansible2_master_rsa.pub
RUN cat /root/.ssh/ansible1_master_rsa.pub >> /root/.ssh/authorized_keys
RUN cat /root/.ssh/ansible2_master_rsa.pub >> /root/.ssh/authorized_keys

EXPOSE 22 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]
