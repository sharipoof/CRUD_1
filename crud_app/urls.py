from django.urls import path
from crud_app.views import home, article_delete, shop_edit

urlpatterns = [
    path('', home, name='home'),
    path('<int:id>/delete', article_delete, name='article_delete'),
    path('<int:id>/edit', shop_edit, name='shop_edit'),
    

 
]