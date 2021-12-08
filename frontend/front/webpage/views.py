from django.shortcuts import render
from .forms import UserForm
import requests
import json


def index(request):
    userform = UserForm()

    if request.method == "POST":
        value1 = request.POST.get("first_value")
        value2 = request.POST.get("second_value")

        r1 = requests.get(
            'http://localhost:8001/restapi?value1=' + value1 + '&value2=' + value2)
        r2 = requests.get(
            'http://localhost:8002/restapi?value1=' + value1 + '&value2=' + value2)

        dictionaryResult1 = dict(json.loads(r1.content))
        dictionaryResult2 = dict(json.loads(r2.content))

        return render(request, "webpage/result.html", {"r1": dictionaryResult1, "r2": dictionaryResult2})
    else:
        return render(request, "webpage/index.html", {"form": userform})
