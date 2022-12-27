from django.urls import path

from . import views

urlpatterns = [
    # Categorie's urls
    path('category-list', views.CategoryList.as_view(), name='category-list'),
    path('category/<slug:slug>', views.CategoryRetrieveView.as_view(),
         name='category-detail'),
    # Author's urls
    path('author-list', views.AuthorList.as_view(), name='author-list'),
    path('admin-authors/<int:pk>',
         views.AdminAuthorsList.as_view(), name='admin-authors'),
    # Post's urls
    path('post-list', views.PostList.as_view(), name='post-list'),
    path('post/<int:pk>', views.PostRetrieveView.as_view(), name='post-detail'),
    path('admin-post/<int:pk>',
         views.AdminDestroyPostView.as_view(), name='admin-post'),
]
