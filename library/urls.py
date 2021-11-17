from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings


app_name='library'
urlpatterns = [
    path('', views.main, name='main'),
    path('addBook/', views.addBook, name='addBook'),
    path('displayBook/', views.displayBook, name='displayBook'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete_book/<int:id>/',views.delete_book, name="delete_book"),
    path('registerUser/',views.registerUser, name="registerUser"), 
    path('displayUser/',views.displayUser, name="displayUser"),
    path('displaybookUser/',views.displaybookUser, name="displaybookUser"),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)