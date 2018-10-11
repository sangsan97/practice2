from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.SlideView.as_view(), name='slide'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('login/', views.Signin, name='login'),
    path('logout/', views.Signout, name='logout'),
    path('join/', views.Signup, name='join'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/', views.CreatePostView.as_view(), name='post_form'),
    path('post/<pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)