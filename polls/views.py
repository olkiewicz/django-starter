from django.http import HttpResponse, Http404
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def lotto(request, num, max2 = 49):
    if num > max2:
        raise Http404('Too high number')
    return HttpResponse("Congratulations, pal. You're won on the lottery.")


def square(request, num):
    showTemplate = True
    resultText = f"{num} * {num} = {num * num}",
    numList = range(num)
    context = {
        'showTemplate': showTemplate,
        'resultText': resultText,
        'num': num,
        'numList': numList
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)