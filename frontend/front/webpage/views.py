from django.shortcuts import render
from .forms import UserForm
import requests
import json
from yaml import safe_load


def index(request):
    userform = UserForm()
    with open('config.yml', 'r') as f:
        data = safe_load(f)

    backend1_adress = data['backend']['server1']['adress']
    backend1_port = data['backend']['server1']['port']
    backend2_adress = data['backend']['server2']['adress']
    backend2_port = data['backend']['server2']['port']
    backend1_url = 'http://' + backend1_adress + ':' + str(backend1_port)
    backend2_url = 'http://' + backend2_adress + ':' + str(backend2_port)

    if request.method == "POST":
        value1 = request.POST.get("first_value")
        value2 = request.POST.get("second_value")

        r1 = requests.get(
            backend1_url + '/restapi?value1=' + value1 + '&value2=' + value2)
        r2 = requests.get(
            backend2_url + '/restapi?value1=' + value1 + '&value2=' + value2)

        dictionaryResult1 = dict(json.loads(r1.content))
        dictionaryResult2 = dict(json.loads(r2.content))

        return render(request, "webpage/result.html", {"r1": dictionaryResult1, "r2": dictionaryResult2})
    else:
        return render(request, "webpage/index.html", {"form": userform, "url1": backend1_url, "url2": backend2_url})
