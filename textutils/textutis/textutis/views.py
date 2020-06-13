# I have created this file


from django.http import HttpResponse
from django.shortcuts import render



# Code for video 6 (Views_Urls in Django)

# def index(request):
#     return HttpResponse("<h1>Hello Ravin</h1>")
#
# def about(request):
#     return HttpResponse("about Ravin")
#
# def readtext(request):
#     with open('one.txt', 'r') as rf:
#         x = rf.read()
#     return HttpResponse(x)



# # Code for video 8(Laying the Pipeline)
# def index(request):
#     return HttpResponse("Home")
#
# def removepunc(request):
#     return HttpResponse("Remove Punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("character counter  <a href='/'>back</a>")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")


#
#
# # # Code for video 9(Template)
#
# # firstly  do from django.shortcuts import render
#
# def index(request):
#     return render(request,'index.html')
#
# def removepunc(request):
#     params={'name':'Ravin', 'place':'Liliya'}
#     return render(request, 'index2.html', params)              # we can pass thirdparameter in render wich shold be dictionary
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("character counter  <a href='/'>back</a>")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")









#
#
# # # Code for video 10(Creating Homepage)
#
# def index(request):
#     return render(request,'index.html')
#
# def removepunc(request):
#     # Get the text
#     # print(request.GET.get('text','default'))    # if text is empty we wil get default    # this line will return text which is in textare(in templet of index.html)
#     djtext=request.GET.get('text','default')
#     print(djtext)
#
#     # Analyz the text
#
#     params={'name':'Ravin', 'place':'Liliya'}
#     return render(request, 'index2.html', params)              # we can pass thirdparameter in render wich shold be dictionary
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("character counter  <a href='/'>back</a>")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")










#
# # # Code for video 11(Coding the backend)
#
# def index(request):
#     return render(request,'index.html')
#
# def analyze(request):
#     # Get the text
#     # print(request.GET.get('text','default'))    # if text is empty we wil get default    # this line will return text which is in textare(in templet of index.html)
#     djtext=request.GET.get('text','default')
#     removepunc=request.GET.get('removepunc', 'off')             # checkbox has off as default value
#     print(djtext)
#     print((removepunc))
#     # Analyz the text
#     if removepunc == "on":
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed=""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed=analyzed+char
#         params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
#         return render(request, 'analyze.html', params)              # we can pass thirdparameter in render wich shold be dictionary
#     else:
#         return HttpResponse("Error")
#











#
# # # Code for video 13(Coding the backend(adding more feaatures)
#
# def index(request):
#     return render(request,'index.html')
#
# def analyze(request):
#     # Get the text
#     # print(request.GET.get('text','default'))    # if text is empty we wil get default    # this line will return text which is in textare(in templet of index.html)
#     djtext=request.GET.get('text','default')
#
#     # Check checkbox values
#     removepunc=request.GET.get('removepunc', 'off')             # checkbox has off as default value
#     fullcaps=request.GET.get('fullcaps', 'off')
#     newlineremover=request.GET.get('newlineremover', 'off')
#     extraspaceremover=request.GET.get('extraspaceremover','off')
#     charcount=request.GET.get('charcount','off')
#
#
#     # Analyz the text
#
#     # check with checkbox is on
#     if removepunc == "on":
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed=""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed=analyzed+char
#         params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
#         return render(request, 'analyze.html', params)              # we can pass thirdparameter in render wich shold be dictionary
#
#     if fullcaps == 'on':
#         analyzed=''
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#         params={'purpose':'Changed to upper case','analyzed_text':analyzed}
#         return render(request, 'analyze.html', params)
#
#     elif newlineremover == 'on':
#         analyzed=''
#         for char in djtext:
#             if char != '\n':
#                 analyzed=analyzed+char
#         params={'purpose':'Removed New Lines','analyzed_text':analyzed}
#         return render(request,'analyze.html',params)
#
#     elif extraspaceremover == 'on':
#         analyzed=''
#         for index, char in enumerate(djtext):
#             if djtext[index] == " " and djtext[index+1] == " ":
#                 pass
#             else:
#                 analyzed=analyzed+char
#         params={'purpose':'Removed Extra Space', 'analyzed_text':analyzed}
#         return render(request, 'analyze.html', params)
#
#     elif charcount == 'on':
#         l=len(djtext)
#         temp_var=''
#         count=0
#         while count<l:
#             if djtext[count] not in temp_var:
#                 s=djtext.count(djtext[count])
#                 temp_var+=djtext[count]
#                 count+=1
#         params={'purpose':'Character Counter','count':count}
#         return render(request, 'charcount.html', params)
#
#     else:
#         return HttpResponse("Error")













# # Code for video 15(adding bootstrap to our django site)

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    # print(request.GET.get('text','default'))    # if text is empty we wil get default    # this line will return text which is in textare(in templet of index.html)
    # djtext=request.GET.get('text','default')    # for get method
    djtext=request.POST.get('text','default')     # for post method


    # Check checkbox values
    removepunc=request.POST.get('removepunc', 'off')             # checkbox has off as default value
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')


    # Analyz the text

    # check with checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:                                  # here is a bug i  our website like when we entered text which has lot of spaceline in our text area and we choosed
                analyzed=analyzed+char                                    # removepuctuation option, and we get output with removed new lines, but this is a bug beacuse we called only removed punctuations
                # print(analyzed)                                           # we got this bug just because of html, because html bydefault remove new lines from our text, we can overcome this problem using <pre> tag in html.
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        # print(params)
        return render(request, 'analyze.html', params)              # we can pass thirdparameter in render wich shold be dictionary

    if fullcaps == 'on':
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'Changed to upper case','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed=''
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'Removed New Lines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif extraspaceremover == 'on':
        analyzed=''
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed=analyzed+char
        params={'purpose':'Removed Extra Space', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif charcount == 'on':
        l=len(djtext)
        temp_var=''
        count=0
        while count<l:
            if djtext[count] not in temp_var:
                s=djtext.count(djtext[count])
                temp_var+=djtext[count]
                count+=1
        params={'purpose':'Character Counter','count':count}
        return render(request, 'charcount.html', params)

    else:
        return HttpResponse("Error")



# Difference between get request and post request
# GET ---> default behaviour of form(it shows on url)
# Post ----> for send password(it send also additional msges with password)(not shows on url(it means our sended password will not show on url)

# We should use post request because if we will use get request and out text is too too long then some servers return error like url is too long because get send data in url, so we have to  use post method to overcome this problem.
# But in Post method, django provide CSRF(Cross Site Request Forgery) mechanism for security, for this we have to write {% csrf_token %} after form tag in form