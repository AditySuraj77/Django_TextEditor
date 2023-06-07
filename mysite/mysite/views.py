from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    return HttpResponse('''<h1> Hay i am Index </h1> <a href="https://unsplash.com/"> Unplash </a>''')


def index(request):
    #params = {'name':'Aditya','Date':'06/06/2023','Course':'Django_Course'} # Variables
    return render(request,'index.html')


def about(request):
    return HttpResponse('<h1> Hay i am About </h1>')


#def action(request):
     #djtext = request.GET.get('text','default')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('punction','off')
    newlinerem = request.POST.get('newlinerem','off')
    extraspacerem = request.POST.get('extraspacerem','off')
    wordcount = request.POST.get('wordcount','off')
    #print(removepunc)
    #print(djtext)
    if removepunc == 'on':
        analyzed = ''
        capi_result = djtext.upper()
        analyzed = analyzed + capi_result
        params = {'analysis':analyzed}
        return render(request,'analyze.html',params)

    elif (newlinerem == 'on'):
        analyzed = ''
        if djtext != '\n':
            analyzed = analyzed + djtext
            params = {'analysis': analyzed}
            return render(request, 'analyze.html', params)
    elif (extraspacerem == 'on'):
        analyzed = ''
        #for index ,char in enumerate(djtext):
        if not( djtext[0] == ' ' and djtext[0+1] == ' '):
            analyzed = analyzed + djtext
            params = {'analysis': analyzed}
            return render(request, 'analyze.html', params)
    elif (wordcount == 'on'):
        analyzed = len(djtext)
        params = {'analysis': analyzed}
        return render(request, 'analyze.html', params)



    else:
        return HttpResponse('ERROR')



