from django.urls import path, include

from . import views
app_name='movieapp'


urlpatterns = [
    path('', views.index, name="index"),
    path('movie/<int:movid>/',views.details,name="detail"),
    path('movieapp/add_movie/', views.add_movie, name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),


]

