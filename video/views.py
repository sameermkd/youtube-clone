from django.shortcuts import render
import requests

def index(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer {API_KEY}"
    }

    response = requests.get(url, headers=headers)
    posts = response.json()
    data = posts['results']
    context = {
        "data":data
    }
    return render(request,"index.html",context)