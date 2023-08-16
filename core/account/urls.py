from django.urls import path,include
from account import views


app_name ='accounts'

urlpatterns = [
   path('logout/', views.logout_view.as_view(), name="logout"),
   path('',views.signup_user.as_view(),name='signup'),
   path('login/',views.LoginFormView.as_view(),name='login'),
   
   
]