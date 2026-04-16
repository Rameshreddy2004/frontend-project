from django.urls import path
from . import views

urlpatterns = [
    path('', views.prompt_list),
    path('<uuid:id>/', views.prompt_detail),
    path('<uuid:id>/delete/', views.delete_prompt),
]