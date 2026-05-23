from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Delivery, Product, AdminUser
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.


def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = User.objects.create(
            fname=fname, lname=lname, email=email, password=password
        )
        data.save()
        messages.success(request, "Account created successfully!")
        return redirect(signin)
    return render(request, "signup.html")


def adminlogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = AdminUser.objects.get(email=email, password=password)
            request.session["user_id"] = user.id

            return redirect(adminpage)
        except AdminUser.DoesNotExist:
            messages.error(request, "Invalid Email or Password")
            return redirect(adminlogin)
    return render(request, "adminlogin.html")


def adminpage(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        product_name = request.POST.get("product_name")
        description = request.POST.get("description")
        price = request.POST.get("price")

        Product.objects.create(
            image=image, product_name=product_name, description=description, price=price
        )
        return redirect(adminpage)

    products = Product.objects.all()
    return render(request, "adminpage.html", {"products": products})


def delete(request, id):
    item = get_object_or_404(Product, id=id)
    item.delete()
    return redirect("adminpage")


def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email, password=password)
            request.session["user_id"] = user.id

            return redirect(home)
        except User.DoesNotExist:
            messages.error(request, "Invalid Email or Password")
            return redirect(signin)
    return render(request, "signin.html")


def home(request):
    if "user_id" not in request.session:
        return redirect("signin")
    user = get_object_or_404(User, id=request.session["user_id"])
    products = Product.objects.all()
    return render(request, "home.html", {"products": products, "user": user})


def profile(request):
    if "user_id" not in request.session:
        return redirect("signin")
    user = get_object_or_404(User, id=request.session["user_id"])
    return render(request, "profile.html", {"user": user})


def add_cart(request, product_id):
    if "user_id" not in request.session:
        return redirect("signin")
    product = get_object_or_404(Product, id=product_id)
    request.session["cart"] = request.session.get("cart", []) + [product.id]
    return redirect("cart")


def increment_cart(request, product_id):
    cart = request.session.get("cart", [])
    cart.append(product_id)
    request.session["cart"] = cart
    return redirect("cart")


def decrement_cart(request, product_id):
    cart = request.session.get("cart", [])
    if product_id in cart:
        cart.remove(product_id)
        request.session["cart"] = cart
    return redirect("cart")


def remove_cart(request, product_id):
    cart = request.session.get("cart", [])
    cart = [item for item in cart if item != product_id]
    request.session["cart"] = cart
    return redirect("cart")


def collection(request):
    if "user_id" not in request.session:
        return redirect("signin")
    user = get_object_or_404(User, id=request.session["user_id"])
    products = Product.objects.all()
    return render(request, "collection.html", {"products": products, "user": user})


def cart(request):
    cart = request.session.get("cart", [])
    quantities = {}
    for product_id in cart:
        quantities[product_id] = quantities.get(product_id, 0) + 1

    products = Product.objects.filter(id__in=quantities.keys())
    cart_items = [
        {"product": product, "quantity": quantities[product.id]} for product in products
    ]
    subtotal = sum([item["product"].price * item["quantity"] for item in cart_items])
    return render(
        request, "cart.html", {"cart_items": cart_items, "subtotal": subtotal}
    )


def shipping(request):
    if request.method == "POST":
        address = request.POST.get("address")
        zip = request.POST.get("zip")
        del_time = request.POST.get("del_time")

        data = Delivery.objects.create(address=address, zip=zip, del_time=del_time)

        data.save()
        return redirect(order)
    return render(request, "shipping.html")


def order(request):
    return render(request, "order.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect("signup")
