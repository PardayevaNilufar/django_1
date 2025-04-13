from django.urls import path


from .views import home_page, fan_page, detail_page, addarticle, delarticle, update_article, addcategoriya,detaile_page

urlpatterns=[
    path('',home_page,name="home"),
    path('fan/',fan_page,name="fan"),
    path('detail/<int:id>/',detail_page,name="detail"),
    path('detaile/<int:id>/',detaile_page,name="detaile"),
    path('articleadd/',addarticle,name="qoshish"),
    path('categoriya/',addcategoriya,name="categoriya"),
    path('delete/<int:id>/',delarticle,name="ochirish"),
    path('update/<int:id>/',update_article,name="yangilash"),
]