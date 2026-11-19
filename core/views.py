from django.shortcuts import render
from .Product import Product

def home(request):
    return render(request, 'home.html', {'title': 'Головна'})

def news(request):
    return render(request, 'news.html', {'title': 'Новини'})

def management(request):
    return render(request, 'management.html', {'title': 'Керівництво компанії'})

def about(request):
    return render(request, 'about.html', {'title': 'Про компанію'})

def contacts(request):
    return render(request, 'contacts.html', {'title': 'Контакти'})

def products(request):
    products = [
        Product("MacBook Pro 14", 6000, 0.10, "Electronics","https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/mbp14-spaceblack-cto-hero-202410?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1761936377425"),
        Product("iPhone 16", 999, 0.05, "Electronics","https://theapplewiki.com/images/applewiki/thumb/7/7c/IPhone_16.png/977px-IPhone_16.png.webp"),
        Product("Sony WH-1000XM5", 349, 0.15, "Electronics","https://media.sweetwater.com/m/products/image/8823f6e96149BJkTLHbzXMQ5saAqGciHWl2mGY0l.jpg?ha=8823f6e9619d569d4d29b49f50fc06c0641595c2&quality=82&width=1200&height=630&canvas=1200%2C630&bg-color=ffffff&fit=bounds"),
        Product("Nike Air Max 90", 130, 0.20, "Shoes","https://static.nike.com/a/images/t_default/u_9ddf04c7-2a9a-4d76-add1-d15af8f0263d,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/6d08d117-7829-462c-bdb0-4d195b894fcc/AIR+MAX+90.png"),
        Product("Levi's 501 Jeans", 89, 0.10, "Clothing","https://slimages.macysassets.com/is/image/MCY/products/0/optimized/3536140_fpx.tif?$$filterlrg$$&wid=327"),
        Product("The Alchemist", 15, 0.00, "Books","https://cdn.waterstones.com/bookjackets/large/9780/7225/9780722532935.jpg"),
        Product("Instant Pot Duo", 99, 0.25, "Home","http://instantpot.com/cdn/shop/files/112-0170-01_Duo_6_Qt_Silo_01_ATF.png?v=1752158152"),
        Product("Dyson V15", 649, 0.12, "Home","https://slimages.macysassets.com/is/image/MCY/products/7/optimized/35104667_fpx.tif?$$filterlrg$$&wid=327"),
        Product("Adidas Ultraboost", 180, 0.18, "Shoes","https://slimages.macysassets.com/is/image/MCY/products/3/optimized/25195603_fpx.tif?$$filterlrg$$&wid=327"),
        Product("Kindle Paperwhite", 140, 0.08, "Electronics","https://cdn.mos.cms.futurecdn.net/VQy5gsPsA7P5q47i6pSZan-2000-80.jpg"),
    ]
    context={
        'page_title':'Каталог товарів',
        'branches':products,
        'quantity':len(products)
        }
    return render(request,'products.html',context)