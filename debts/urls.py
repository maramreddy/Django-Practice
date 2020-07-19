from django.urls import path,re_path
from . import views
app_name = 'debts_app'
urlpatterns = [
    path('',views.debts_home,name='debts_home'),
    path('persons/',views.debts_persons, name='debts_persons' ),
    path('register_debts/',views.register_debts, name="register_debts"),
    path('register/',views.register, name='register'),
    path('login/',views.user_login,name="user_login"),
    path('logout/',views.user_logout,name="user_logout"),
    # re_path('^$',views.debts_home,name='debts_home'),  # for regex url patterns
]