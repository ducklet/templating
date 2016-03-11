from django.shortcuts import render


def index(request):
    return render(request, 'templating_app/index.html')


def autoescape(request):
    autoescape_ex = "<p>This content has autoescape on.</p>"
    autoescape_off_ex = "<p>This content has autoescape off.</p>"
    return render(request, 'templating_app/autoescape.html',
                  {"autoescape_ex": autoescape_ex, "autoescape_off_ex": autoescape_off_ex})


def comment(request):
    return render(request, 'templating_app/comment.html')


def csrf_token(request):
    return render(request, 'templating_app/csrf_token.html')


def cycle(request):
    return render(request, 'templating_app/cycle.html')


def debug(request):
    dict(alissa=1, eddie=2)
    return render(request, 'templating_app/debug.html', {"dict": dict})


def extends(request):
    return render(request, 'templating_app/extends.html')


def filter(request):
    return render(request, 'templating_app/filter.html')
