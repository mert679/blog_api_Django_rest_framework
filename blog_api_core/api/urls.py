from django.urls import path
from . import views

urlpatterns =[
    path("", views.ApiOverview, name="home"),
    path("create/", views.add_blog,name="add-blog"),
    path("all/",views.list_blog, name="view_blogs"),
    path('update/<int:pk>/', views.update_blog, name='update_blog'),
    path('blog/<int:pk>/delete', views.delete_blog, name='delete_blog'),
    path('detail/<int:pk>/', views.get_detail, name='detail_blog'),
    
]