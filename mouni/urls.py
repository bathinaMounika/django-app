from django.urls import path, include
from mouni import views
from mouni.views import (
	ExamListView,
	ExamDetailView, 
	MessageCreateView, 
	MessageUpdateView, 
	MessageDeleteView, 
	MessageDetailView
	)
from django.contrib.auth.decorators import login_required

app_name = 'mouni'

urlpatterns = [
    path('', ExamListView.as_view(), name='exam-list'),
    path("exam/<int:pk>/", login_required(ExamDetailView.as_view()), name="exam-detail"),
    path("create_exam/", views.create_exam, name="create-exam"),
    path('message/<int:pk>/detail/', login_required(MessageDetailView.as_view()), name='msg-detail'),
    path("message/", login_required(MessageCreateView.as_view()), name='msg'),
    path("message/<int:pk>/update/", MessageUpdateView.as_view(), name='msg-update'),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name='msg-delete'),
    path("display_results/", views.display_results, name="display-results"),
]

