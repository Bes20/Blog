from django.urls import path
from .views import ArticleCreateView, ArticleAddCommentView, ArticleView, CommentsView

urlpatterns = [
    path('create', ArticleCreateView.as_view(), name='create_article'),
    path('view/<int:pk>', ArticleView.as_view(), name='view_article'),
    path('add_comment', ArticleAddCommentView.as_view(), name='add_comment'),
    path('view_comment', CommentsView.as_view(), name='view_comment')
]
