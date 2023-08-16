from django.urls import path,include
from task import views


app_name ='tasks'

urlpatterns = [
   path('',views.TaskCreate.as_view(),name='create'),
   path('edit/<int:pk>/',views.TaskUpdateView.as_view(),name='edit'),
   path('todo/', views.TaskList.as_view(), name="list"),
   path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name="delete"),
   path("complete/<int:pk>/", views.TaskComplete.as_view(), name="complete"),

   
]