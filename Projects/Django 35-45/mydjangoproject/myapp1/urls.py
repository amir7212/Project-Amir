from django.contrib import admin
from django.urls import path
from myapp1.views import index_page
from myapp1 import views
from myapp1 import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('777',index_page),
    path('in',views.index),
    path("postuser/", views.postuser),
    path('products/', views.products_view),
    path('bootstrap_page/', views.bootstrap_test),
    path('test/', views.test)
]