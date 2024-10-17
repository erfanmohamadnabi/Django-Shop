from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #! APP URLS

    path('',include('login.urls')),
    path('',include('about.urls')),
    path('',include('contact.urls')),
    path('',include('weblog.urls')),
    path('',include('questions.urls')),
    path('',include('user_account.urls')),
    path('',include('products.urls')),
    path('',include('index.urls')),

    #! APP URLS

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
