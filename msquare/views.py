from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from app.models import seller, buyer, product, cart, orders
from app.views import getMuser, getBuyerUser

def HomePage(request):
    latest = product.objects.order_by('-createdAt')
    fashion = product.objects.filter(category = 'option1')
    jewellery = product.objects.filter(category = 'option2')
    electronics = product.objects.filter(category = 'option3')

    data = {
        'category0': "Latest Products",
        'category1': "Fashion",
        'category2': "Jewellery",
        'category3': "Electronics",
        'latest': latest,
        'fashion': fashion,
        'jewellery': jewellery,
        'electronics': electronics
    }
    return render(request, "index.html", data)

def BecomeSeller(request):
    return render(request, "becomeSeller.html")

def TrackMyOrder(request):
    try:
        user = getBuyerUser()
        orderList = orders.objects.filter(buyerID= user)
        data = {
            'product' : orderList
        }
        return render(request, "trackMyOrder.html", data)
    except:
        return HttpResponseRedirect('/login')

def BestSeller(request):
    sortedSeller = seller.objects.order_by('-earning')
    data = {
        'seller': sortedSeller
    }
    return render(request, "bestSeller.html", data)

def Login(request):
    return render(request, "sellerSignin.html")

def Signup(request):
    return render(request, "signup.html")

def Cart(request):
    try:
        user = getBuyerUser()
        cartProducts = cart.objects.filter(buyerID=user)
        data = {
            'product': cartProducts
        }
        return render(request, "cart.html", data)
    except:
        return HttpResponseRedirect('/login')

def Fashion(request):
    fashion = product.objects.filter(category = 'option1')
    data = {
        'category1': "Fashion",
        'fashion': fashion
    }
    return render(request, "fashion.html", data)

def Jewellery(request):
    jewellery = product.objects.filter(category = 'option2')
    data = {
        'category2': "Jewellery",
        'jewellery': jewellery
    }
    return render(request, "jewellery.html", data)
    
def Electronics(request):
    electronics = product.objects.filter(category = 'option3')
    data = {
        'category3': "Electronics",
        'electronics': electronics
    }
    return render(request, "electronics.html", data)

def ProductDetails(request, pID):
    p = get_object_or_404(product, id=pID)
    data = {
        'product': p
    }
    return render(request, 'product.html', data)


def sellerDashboard(request):
    try:
        user = getMuser()
        userProducts = product.objects.filter(sellerID= user)
        opt1, opt2, opt3 = 0, 0, 0
        for x in userProducts:
            if x.category == 'option1':
                opt1 += 1
            elif x.category == 'option2':
                opt2 += 1
            elif x.category == 'option3':
                opt3 += 1
        items=[ opt1, opt2, opt3 ]

        opt1, opt2, opt3 = 0, 0, 0
        userOrders = orders.objects.filter(sellerID= user)
        for x in userOrders:
            if x.productID.category == 'option1':
                opt1 += 1
            elif x.productID.category == 'option2':
                opt2 += 1
            elif x.productID.category == 'option3':
                opt3 += 1
        sItems=[ opt1, opt2, opt3 ]

        data = {
            'storeName' : user.storename,
            'items' : items,
            'sItem' : sItems

        }
        return render(request, "sellerDashboard.html", data)
    except:
        return HttpResponseRedirect('/login')

def addNewProduct(request):
    try:
        data = {'storeName' : getMuser().storename}
        return render(request, "addProduct.html", data)
    except:
        return HttpResponseRedirect('/login')

def removeProduct(request):
    try:
        user = getMuser()
        allproducts = product.objects.filter(sellerID= user)
        data = {
            'storeName' : user.storename,
            'product': allproducts
        }
        return render(request, "removeProduct.html", data)
    except:
        return HttpResponseRedirect('/login')

def manageOrders(request):
    try:
        user = getMuser()
        orderList = orders.objects.filter(sellerID= user)
        data = {
            'storeName' : user.storename,
            'product' : orderList
        }
        return render(request, "manageOrders.html", data)
    except:
        return HttpResponseRedirect('/login')

def Check(request):
    return render(request, "check.html")

def earnings(request):
    try:
        user = getMuser()
        opt1, opt2, opt3 = 0, 0, 0
        e1, e2, e3 = 0, 0, 0
        userOrders = orders.objects.filter(sellerID= user)
        for x in userOrders:
            if x.productID.category == 'option1':
                opt1 += x.quantity
                e1 += x.price
            elif x.productID.category == 'option2':
                opt2 += x.quantity
                e2 += x.price
            elif x.productID.category == 'option3':
                opt3 += x.quantity
                e3 += x.price
        sItems=[ opt1, opt2, opt3 ]
        earning=[e1, e2, e3]
        data = {
            'storeName' : user.storename,
            'sItem' : sItems,
            'earning': earning
        }
        return render(request, "withdraw.html", data)
    except:
        return HttpResponseRedirect('/login')