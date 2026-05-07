from django.urls import path
from App import views

urlpatterns = [
    path("", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    path("adminpage/", views.adminpage, name="adminpage"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("collection/", views.collection, name="collection"),
    path("cart/", views.cart, name="cart"),
    path("add_cart/<int:product_id>/", views.add_cart, name="add_cart"),
    path("remove_cart/<int:product_id>/", views.remove_cart, name="remove_cart"),
    path(
        "increment_cart/<int:product_id>/", views.increment_cart, name="increment_cart"
    ),
    path(
        "decrement_cart/<int:product_id>/", views.decrement_cart, name="decrement_cart"
    ),
    path("shipping/", views.shipping, name="shipping"),
    path("order", views.order, name="order"),
    path("logout/", views.logout_view, name="logout"),
]
