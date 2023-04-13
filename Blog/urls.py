from django.urls import path
from Blog import views

from . views import PostDetailView
urlpatterns = [

    path('index/',views.index,name='index'),

    path('', views.loginpg,name='loginpg'),
    path('adminlog/' ,views.adminlog,name='adminlog'),

    path('addpost/',views.addpost,name='addpost'),
    path('addpostsave/',views.addpostsave,name='addpostsave'),
    
    path('article/<int:pk>',PostDetailView.as_view(),name='post_detail'),

    path('adminlogout/',views.adminlogout,name='adminlogout')
   
]

