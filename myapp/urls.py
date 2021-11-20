from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [

    path('students', views.StudentsView.as_view(), name='students'),
    path('student-create', views.StudentCreateView.as_view(), name='student-create'),
    path('student-edit/<int:id>', views.StudentEditView.as_view(), name='student-edit'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name='students_detail'),
    path('add-sponsor/<int:id>', views.AddSponsorView.as_view(), name='add-sponsor'),

    path('sponsors', views.SponsorsView.as_view(), name='sponsors'),
    path('sponsors-create', views.SponsorCreateView.as_view(), name='sponsors-create'),
    path('sponsors/<int:pk>', views.SponsorDetailView.as_view(), name='spondors_detail'),
    path('sponsors-edit/<int:pk>', views.SponsorEditView.as_view(), name='spondors_edit'),

    path('list', views.LstView.as_view(), name='list'),

    path('dashboard', views.DashboardView.as_view(), name='dashboard'),

    path('login', views.MyObtainTokePairListApiView.as_view()),


]


