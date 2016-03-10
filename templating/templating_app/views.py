from django.shortcuts import render


def index(request):
    return render(request, 'templating_app/index.html')


def autoescape(request):
    autoescape_ex = "<p>This content has autoescape on.</p>"
    autoescape_off_ex = "<p>This content has autoescape off.</p>"
    return render(request, 'templating_app/autoescape.html', {"autoescape_ex": autoescape_ex, "autoescape_off_ex": autoescape_off_ex})
