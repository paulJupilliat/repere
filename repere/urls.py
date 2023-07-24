
from django.contrib import admin
from django.urls import path
from accounts.views import logout_user, signup, login_user
from store.views import index, product_detail
from django.conf.urls.static import static 
from repere import settings
urlpatterns = [
    path('', index, name='index'), 
    path('admin/', admin.site.urls),
    path('signup/', signup, name = "signup"),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('product/<str:slug>/', product_detail, name='product'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

