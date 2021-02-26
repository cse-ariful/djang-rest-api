from django.urls import path, include
from .views import article_list, article_detail, ArticlesApiView, ArticleDetails,GenericApiView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticlesApiView.as_view()),
    path('generic/article/', GenericApiView.as_view()),
    # path('article/detail/<int:pk>', article_detail),
    path('article/<int:pk>/', ArticleDetails.as_view())
]
