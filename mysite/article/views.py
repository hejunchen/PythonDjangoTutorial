from django.shortcuts import render_to_response
from article.models import Article
from django.http import HttpResponse


# load all available Article objects
def articles(request):

    language = 'en-us'
    session_language = 'en-us'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response('articles.html',
        {
            'articles': Article.objects.all(),
            'language': language,
            'session_language': session_language,
        }
    )

# load one specific Article object
def article(request, article_id=1):
    return render_to_response('article.html',
        {
            'article': Article.objects.get(id=article_id),
        }
    )

# pass the language and set the value in cookie
def language(request, language='en-us'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response