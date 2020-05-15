from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    # print(request.GET.get('text','default'))    # if text is empty we wil get default    # this line will return text which is in textare(in templet of index.html)
    djtext=request.GET.get('text','default')

    # Check checkbox values
    removepunc=request.GET.get('removepunc', 'off')             # checkbox has off as default value
    fullcaps=request.GET.get('fullcaps', 'off')
    newlineremover=request.GET.get('newlineremover', 'off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')


    # Analyz the text
    analyzed = ""

    # check with checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        djtext=analyzed
        analyzed=""

        # params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        # return render(request, 'analyze.html', params)              # we can pass thirdparameter in render wich shold be dictionary

    if fullcaps == 'on':
        print(f"Entered in fullcaps----->{djtext}")
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        analyzed = ""
        # params={'purpose':'Changed to upper case','analyzed_text':analyzed}
        # return render(request, 'analyze.html', params)

    if newlineremover == 'on':
        analyzed=''
        for char in djtext:
            if char != '\n':
                analyzed=analyzed+char
        djtext = analyzed
        analyzed = ""
        # params={'purpose':'Removed New Lines','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)

    if extraspaceremover == 'on':
        analyzed=''
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed=analyzed+char
        djtext = analyzed
        analyzed = ""
        # params={'purpose':'Removed Extra Space', 'analyzed_text':analyzed}
        # return render(request, 'analyze.html', params)

    params={'purpose':'Analyzed Text ','analyzed_text':f'{djtext}'}
    return render(request, 'analyze.html',params)