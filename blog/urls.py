from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('index/', views.index),
    path('page_content/<int:article_id>', views.page_content, name='page_content'),
    path('edit_page/<int:article_id>', views.edit_page, name='edit_page'),
    path('edit_action/', views.edit_action, name='edit_action')
]
