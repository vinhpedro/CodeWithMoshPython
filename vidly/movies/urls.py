from django.urls import path
from . import views
# movies/--root--''
urlpatterns = [
    path('', views.index, name="index")

]
