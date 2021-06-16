from django.urls import path
from accounts.views import editProfile, login, logout, register, showOtherProfile, showProfile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', showProfile, name='profile'),
    path('profile/other/<str:user_pk>/', showOtherProfile, name='profile-other'),
    path('profile/create/', editProfile, name='profile-edit')
]
