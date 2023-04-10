from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Молодец, что ты все еще тут')


def second_page(request):
    return HttpResponse('А это вторая страница')
