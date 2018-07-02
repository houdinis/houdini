from django.urls import path
import blog.views as bv

app_name = 'blog'
urlpatterns = [
    path(r'index/', bv.index),
    path(r'article/<int:article_id>/', bv.article_page,name='article_page'),
    path(r'edit/<int:article_id>/', bv.edit_page,name='edit_page'),
    path(r'edit/active/',bv.edit_active,name='edit_active'),

]
