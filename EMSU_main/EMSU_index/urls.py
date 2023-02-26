
from django.urls import path
from .views import indexPage
app_name = "EMSU_index"
urlpatterns = [
    path("", indexPage, name="Электронная система местного самоуправления"),

]