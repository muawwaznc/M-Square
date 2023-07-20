from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import buyer, product, seller, cart, orders
from PIL import Image
from django.utils import timezone



def getBuyerData(request):
    try:
        fname = request.POST.get('first-name')
        lname = request.POST.get('last-name')
        phone = request.POST.get('contact')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        data = buyer(fname = fname, lname = lname, phone = phone, email = email, password = password)
        data.save()

        global buyerUser
        buyerUser = data
        return HttpResponseRedirect('/')
    except:
        pass

def getProductData(request):
    try:
        category = request.POST.get('category')
        name = request.POST.get('product-name')
        quantity = int(request.POST.get('quantity'))
        price = float(request.POST.get('price'))
        description = request.POST.get('description')
        image = request.FILES.get('image')  
        sellerID = getMuser()

        data = product(category = category, name = name, quantity = quantity, price = price, description = description, image = image, sellerID = sellerID )
        data.save()

        img = Image.open(data.image.path)
        img.thumbnail((300, 300))
        img.save(data.image.path)

        return HttpResponseRedirect('/add-new-product')
    except Exception as error:
        return HttpResponse(error)

def GetSellerData(request):
    try:
        fname = request.POST.get('first-name')
        lname = request.POST.get('last-name')
        phone = request.POST.get('contact')
        email = request.POST.get('email')
        password = request.POST.get('password')
        storename = request.POST.get('store-name')
        
        data = seller(fname = fname, lname = lname, phone = phone, email = email, password = password, storename = storename)
        data.save()
        global muser
        muser = data
        return HttpResponseRedirect('/seller-dashboard')
    except:
        pass

def CheckLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        usersData = seller.objects.all()
        for user in usersData:
            if user.email == email and user.password == password:
                global muser
                muser = user
                return HttpResponseRedirect('/seller-dashboard')
        
        usersData = buyer.objects.all()
        for user in usersData:
            if user.email == email and user.password == password:
                global buyerUser
                buyerUser = user
                return HttpResponseRedirect('/')
        
        return HttpResponseRedirect('/login')

def Logout():
    muser = None
    buyerUser = None

def getMuser():
    return muser

def getBuyerUser():
    return buyerUser

def updateProduct(request):
    ID = request.POST.get('updated-ID')
    pName = request.POST.get('updated-name')
    pQuantity = int(request.POST.get('updated-quantity'))
    pPrice = float(request.POST.get('updated-price'))

    data = product.objects.get(id = ID)
    data.name = pName
    data.quantity = pQuantity
    data.price = pPrice
    data.save()

    return HttpResponseRedirect('/remove-product')

def removeProduct(request):
    ID = request.POST.get('updated-ID')
    p = product.objects.get(id = ID)
    p.delete()

    return HttpResponseRedirect('/remove-product')

def addToCart(request):    
    buyerID = getBuyerUser()

    productID = request.POST.get('product-id')
    p = product.objects.get(id = productID)
    
    quantity = int(request.POST.get('quantity'))

    addedProduct = cart(buyerID = buyerID, productID = p, quantity = quantity)
    addedProduct.save()


    return HttpResponseRedirect('/')

def delFromCart(request):
    cartID = request.POST.get('cart-ID');
    cartProduct = cart.objects.get(id = cartID)
    cartProduct.delete()
    return HttpResponseRedirect('/cart')

def buyCartProduct(request):
    cartID = request.POST.get('cart-ID')
    cartProduct = cart.objects.get(id = cartID)
    cartProductQuantity = int(request.POST.get('cart-quantity'))

    p = product.objects.get(id = cartProduct.productID.id)
    p.quantity -= cartProductQuantity
    p.save()

    s = p.sellerID
    b = getBuyerUser()
    q = cartProductQuantity
    pr = p.price * q
    AddToOrderDataBase(p, s, b, q, pr)

    cartProduct.delete()
    return HttpResponseRedirect('/cart')

def AddToOrderDataBase(product, seller, buyer, quantity, price):
    data = orders(productID= product, sellerID= seller, buyerID= buyer, quantity= quantity, price= price)
    data.save()

def deliverOrder(request):
    orderID = request.POST.get('order-ID')
    o = orders.objects.get(id = orderID)
    o.isDeliver = True
    o.save()

    return HttpResponseRedirect('/manage-orders')