from django.urls import path


from .views import home_page,fan_page,detail_page

urlpatterns=[
    path('',home_page,name="home"),
    path('fan/',fan_page,name="fan"),
    path('detail/<int:id>/',detail_page,name="detail"),
]