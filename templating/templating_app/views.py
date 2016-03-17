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


def firstof(request):
    the_other_thing = "The firstof tag is outputting this text, the value of the first non-empty variable I gave it."
    return render(request, 'templating_app/firstof.html', {"the_other_thing": the_other_thing})


def for_tag(request):
    example_list = ['This', 'is', 'an', 'ol', 'generated', 'by', 'a', 'for', 'loop', 'and', 'an', 'iterable', 'list']
    return render(request, 'templating_app/for.html', {"example_list": example_list})


def for_empty(request):
    example2_list = []
    return render(request, 'templating_app/for_empty.html', {"example2_list": example2_list})


def if_tag(request):
    pet_list = ['Shadow', 'Maxwell', 'Natasha', 'Ginger', 'Carla']
    return render(request, 'templating_app/if.html', {"pet_list": pet_list})


def ifchanged(request):
    pet_list = ['Shadow', 'Shadow', 'Maxwell', 'Natasha', 'Ginger', 'Carla']
    return render(request, 'templating_app/ifchanged.html', {"pet_list": pet_list})


def include(request):
    return render(request, 'templating_app/include.html')


def load(request):
    return render(request, 'templating_app/load.html')


def lorem(request):
    return render(request, 'templating_app/lorem.html')


def now_tag(request):
    return render(request, 'templating_app/now.html')


def regroup(request):
    musicians = [
        {'name': 'Marty Friedman', 'band': 'Megadeth', 'instrument': 'guitar'},
        {'name': 'Dave Ellefson', 'band': 'Megadeth', 'instrument': 'bass'},
        {'name': 'Simon Gallup', 'band': 'The Cure', 'instrument': 'bass'},
        {'name': 'Neil Pert', 'band': 'Rush', 'instrument': 'drums'},
        {'name': 'Lars Ulrich', 'band': 'Metallica', 'instrument': 'drums'},
    ]
    return render(request, 'templating_app/regroup.html', {"musicians": musicians})


def spaceless(request):
    return render(request, 'templating_app/spaceless.html')


def templatetag(request):
    return render(request, 'templating_app/templatetag.html')
