from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('/vote', views.vote, name='vote'),
    path('/detail/',views.detail, name='detail'),
    path('/<int:article_id>/result', views.result, name='result'),
    path('/<int:article_id>/delete', views.delete, name ='delete'),
    path('/<int:article_id>/reply', views.reply, name='reply'),
    path('/<int:article_id>/edit', views.edit, name='edit'),
    path('/<int:article_id>/save_again', views.save_again, name='save_again'),
]

