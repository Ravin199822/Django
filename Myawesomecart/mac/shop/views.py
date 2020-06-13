from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
# def index(request):
#     all_products=Product.objects.all()
#
#     # print(all_products)   # o/p: <QuerySet [<Product: Titan watch>, <Product: Levis Jeans>, <Product: Lancer Shoes (Red/Black)>, <Product: Mi phone 8 GB RAM, 128 GB ROM>, <Product: Usha Mixer Grinder (White)>, <Product: iball 100000 maph Power Bank (White)>, <Product: John Player T-shirt>]>
#
#     # for no of slides
#     n=len(all_products)
#     nslides=n//4+ceil((n/4)-(n//4))
#     params={'no_of_slides':nslides,'range':range(1,nslides),'products':all_products}
#     return render(request,'shop/index.html', params)
#
# def about(request):
#     return render(request,'shop/about.html')
#
# def contact(request):
#     return HttpResponse("We are at contact...")
#
# def tracker(request):
#     return HttpResponse("We are at tracker...")
#
# def search(request):
#     return HttpResponse("We are at search...")
#
# def productView(request):
#     return HttpResponse("We are at productview...")
#
# def checkout(request):
#     return HttpResponse("We are at checkout...")





#
#
# # Creating multiple product slides
# def index(request):
#     all_products=Product.objects.all()
#
#     # print(all_products)   # o/p: <QuerySet [<Product: Titan watch>, <Product: Levis Jeans>, <Product: Lancer Shoes (Red/Black)>, <Product: Mi phone 8 GB RAM, 128 GB ROM>, <Product: Usha Mixer Grinder (White)>, <Product: iball 100000 maph Power Bank (White)>, <Product: John Player T-shirt>]>
#
#     # for no of slides
#     n=len(all_products)
#     nslides=n//4+ceil((n/4)-(n//4))
#     # params={'no_of_slides':nslides,'range':range(1,nslides),'products':all_products}
#     allprods=[[all_products,range(1,nslides),nslides],
#               [all_products,range(1,nslides),nslides]]
#     params={'all_prods':allprods}
#     return render(request,'shop/index.html', params)
#
# def about(request):
#     return render(request,'shop/about.html')
#
# def contact(request):
#     return HttpResponse("We are at contact...")
#
# def tracker(request):
#     return HttpResponse("We are at tracker...")
#
# def search(request):
#     return HttpResponse("We are at search...")
#
# def productView(request):
#     return HttpResponse("We are at productview...")
#
# def checkout(request):
#     return HttpResponse("We are at checkout...")









# Creating multiple product slides
def index(request):
    allprods=[]
    catprods=Product.objects.values('category','id')  # this will return set of category and id of all products
    print(f"----catprods----{catprods}")
    cats={item['category'] for item in catprods}    # this will return the all category
    print(f"----cats----{cats}")
    for cat in cats:
        prod=Product.objects.filter(category=cat)   # this will return list of products of same category
        print(f"----prods----{prod}")
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod, range(1,nslides),nslides])
    params={'all_prods':allprods}
    return render(request,'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact...")

def tracker(request):
    return HttpResponse("We are at tracker...")

def search(request):
    return HttpResponse("We are at search...")

def productView(request):
    return HttpResponse("We are at productview...")

def checkout(request):
    return HttpResponse("We are at checkout...")
