from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),

    path('register/', views.register, name='register'),
    
    path('login/user/', views.user_login, name='user_login'),
    path('logout/user/', views.user_logout, name='user_logout'),
    path('user/<str:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('update/user/<str:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('delete/user/<str:pk>/', views.UserDeleteView.as_view(), name='user_delete'),

    path('page_list/', views.PageListView.as_view(), name='page_list'),
    path('delete/page/<str:pk>/', views.PageDeleteView.as_view(), name='page_delete'),
    path('update/page/<str:pk>/', views.PageUpdateView.as_view(), name='page_update'),
    path('create/page/', views.PageCreateView.as_view(), name='page_create'),

    path('create/section/page/<str:page_pk>/', views.SectionCreateView.as_view(), name='section_create'),
    path('update/section/<str:pk>/page/<str:page_pk>/', views.SectionUpdateView.as_view(), name='section_update'),
    path('delete/section/<str:pk>/', views.SectionDeleteView.as_view(), name='section_delete'),
    path('updating/', views.update_info, name='update_info'),

    path('create/place/page/<str:page_pk>/', views.PlaceCreateView.as_view(), name='place_create'),
    path('update/place/<str:pk>/page/<str:page_pk>/', views.PlaceUpdateView.as_view(), name='place_update'),
    path('delete/place/<str:pk>/', views.PlaceDeleteView.as_view(), name='place_delete'),
    path('liking/', views.like, name='like'),
  
    path('exploración/', views.ExplorationView.as_view(), name='exploración'),

]