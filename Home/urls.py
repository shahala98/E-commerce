from django.conf import settings
from django.urls import path
from .views import home, add_product ,edit_product, delete_product
from django.conf.urls.static import static

# direct of path in app 

urlpatterns = [
    path('', home, name='Home'),
    path('add_product/' ,add_product, name='add_product'),
    path('edit_product/<int:product_id>' , edit_product , name='edit_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    
]

# if photo upload 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
