from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request,'products/home.html')
# def product_list(request):
#     products = Product.objects.all()
#     context={
#         "products":products
#     }
#     return render(request,'products/products_list.html',context)

def product_list(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request, 'products/products_list.html',context)
# def product_detail(request,pk):
#     product = Product.objects.get(id=pk)
#     context = {
#         "product":product
#     }
#     return render(request,'products/product_detail.html',context)
def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    context = {
        "product":product
    }
    return render(request,'products/product_detail.html',context)
def create_product(request):
    form = ProductForm()
    if request.method =="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/products")
    context = {
        "form":form
    }
    return render(request,'products/product_form.html',context)
# def product_create(request):
#     form = ProductForm()
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/products")
#         context = {
#             "form":form
#         }
#         return render(request,'products/product_form.html',context)
def update_product(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(request.POST or None,instance=product)
    if request.method=="POST":
        if form.is_valid:
            form.save()
            return redirect("/products")
    context = {
        "form":form
    }
    return render(request,'products/product_form.html',context)
def delete_product(request,pk):
    if request.method=="POST":
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('/products')
    return render(request,'products/confirm_delete.html')
