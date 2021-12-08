from django.http import HttpResponse
import json
import socket


def index(request):
    operation = 'additional'
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(str(host_name))
    host_port = request.META['SERVER_PORT']

    value1 = request.GET["value1"]
    value2 = request.GET["value2"]
    result = int(value1) + int(value2)

    result_dict = {'operation': operation,
                   'value': result,
                   'host_name': str(host_name),
                   'host_ip': host_ip,
                   'host_port': host_port}

    serializedResult = json.dumps(result_dict)
    return HttpResponse(serializedResult)
