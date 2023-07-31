
from django.contrib import admin
from django.urls import path
from accounts.views import logout_user, signup, login_user
from store.views import index, product_detail, add_to_cart, cart, delete_cart, payment_page
from django.conf.urls.static import static 
from repere import settings
urlpatterns = [
    path('', index, name='index'), 
    path('admin/', admin.site.urls),
    path('signup/', signup, name = "signup"),
    path('logout/', logout_user, name='logout'),
    path('cart/',cart, name='cart'),
    path('cart/delete/', delete_cart, name='delete_cart'),
    path('login/', login_user, name='login'),
    path('paiement/', payment_page, name='payment_page'),
    
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart', add_to_cart, name='add_to_cart'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

