from django.urls import path
from.import views


urlpatterns = [
    path('',views.ownproject),
    path('home',views.HomePage),
    # practicing the database concepts like fetch,insert,orm,etc
    path('fetch',views.fetchdata),
    path('insert',views.insertdata),
    path('orminsert',views.orminsertdata,name='orm'),
    path('ormfetch',views.ormfetchdata),
    
]



