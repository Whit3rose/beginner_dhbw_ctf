from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.register,name="register"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
    path('notes/',views.notes,name='notes'),
    path('notes/<int:id>/',views.note_details,name='note_details'),
    path('notes/create/', views.create_note, name='create_note'),
]
