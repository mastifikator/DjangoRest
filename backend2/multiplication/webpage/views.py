from django.shortcuts import render
import socket


def index(request):
    operation = 'multiplication'
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(str(host_name))
    host_port = request.META['SERVER_PORT']
    return render(request, "webpage/index.html", {"operation": operation, "host_name": host_name, "host_ip": host_ip, "host_port": host_port})
