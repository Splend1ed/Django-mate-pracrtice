from django.urls import path
from app.views import (
    MainPage,
    TagsListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagCreateView,
    status_task_redirect,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path("", MainPage.as_view(), name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/status-change/", status_task_redirect, name="task-redirect")
]

app_name = "app"
