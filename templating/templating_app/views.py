from django.shortcuts import render
import datetime


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


def url_tag(request):
    return render(request, 'templating_app/url.html')


def verbatim(request):
    return render(request, 'templating_app/verbatim.html')


def widthratio(request):
    return render(request, 'templating_app/widthratio.html')


def with_tag(request):
    return render(request, 'templating_app/with.html')


def filters(request):
    none_var = None
    people = [
        {'name': 'Alissa', 'age': 29},
        {'name': 'Eddie', 'age': 36},
        {'name': 'Sebastian', 'age': 17},
    ]
    escape_ex = "<p>This HTML is escaped.</p>"
    fake_js = "jQuery('#database').val(db);"
    sentence = ['This sentence is the first item in a list.', 'Second', "Third"]
    numbers = [123.456, 234.567, 345.678]
    awesom_o = "Alissa\nrocks!"
    fake_string = "?Alissa=1&rocks=2"
    join_list = ['Using', 'the', 'join', 'filter.']
    last_list = ['First', 'Last item in the list']
    line_numbers = """Linenumbers
                   and
                   linebreaksbr
                   filters!"""
    cactus_count = 3
    now = datetime.datetime.now()
    birth_date = datetime.date(1981, 4, 20)
    fotc = datetime.date(2016, 6, 13)
    trunc_html = "<p>The truncatechars_html filter is keeping all HTML tags but still truncating this string.</p>"
    friends = ['Friends', ['Panchenkos', ['Anastasia', 'Alex'], 'Walters', ['Ellen', 'David']]]
    word_wrap = "I'm using the wordwrap filter to set a line length of 10 characters, beyond which text wraps."
    return render(request, 'templating_app/filters.html', {"none_var": none_var, "people": people,
                                                           "escape_ex": escape_ex, "fake_js": fake_js,
                                                           "sentence": sentence, "numbers": numbers,
                                                           "awesom_o": awesom_o, "fake_string": fake_string,
                                                           "join_list": join_list, "last_list": last_list,
                                                           "line_numbers": line_numbers, "cactus_count": cactus_count,
                                                           "now": now, "birth_date": birth_date,
                                                           "fotc": fotc, "trunc_html": trunc_html, "friends": friends,
                                                           "word_wrap": word_wrap})
