from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static



urlpatterns = [
    path('ex/', views.homePage, name="homePage"),
    path('', views.home, name="home"),
    path('members/', views.members, name="members"),
    path('profile/<str:pk_test>/', views.profile, name="profile"),

    path('create_tier/<str:pk>/',views.createTier, name="create_tier"),
    path('update_tier/<str:pk_tier>/',views.updateTier, name="update_tier"),
    path('delete_tier/<str:pk_item>/',views.deleteTier, name="delete_tier"),

    path('add_game/',views.newGame, name="add_game"),
    path('add_member/',views.newMember, name="add_member"),
    path('delete_member/<str:pk_member>/',views.deleteMember, name="delete_member"),

    path('register/', views.registerPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),

    path('hierarchy/', views.hierarchy, name="hierarchy"),
    path('userprofile/<str:pk_test>/', views.userprofile, name="userprofile"),
    path('updateuser/<str:pk_test>/', views.updateuser, name="updateuser"),

    path('teamlist/', views.teamlist, name="teamlist"),
    path('addteam/', views.addTeam, name="addteam"),
    path('team/<str:pk>/', views.team, name="team"),
    path('deletefromteam/<str:pk>/',views.deleteTeamMember, name="deleteTeamMember"),

    path('addtournament/', views.addTournament, name="addtournament"),

    url(r'^apply/$', views.ajax, name='ajax_apply'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)