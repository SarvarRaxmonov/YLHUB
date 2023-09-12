from django.urls import path

from apps.vebinar.views import (ComplainCreateView,
                                UserVebinarSearchHistoryDeleteView,
                                UserVebinarSearchHistoryView,
                                VebinarDetailView, VebinarListView)

urlpatterns = [
    path("vebinars/", VebinarListView.as_view(), name="vebinar-list"),
    path("vebinar-detail/<int:pk>/", VebinarDetailView.as_view(), name="vebinar-detail"),
    path("complain-create/", ComplainCreateView.as_view(), name="complain-create"),
    path(
        "search-history/<int:user_id>/",
        UserVebinarSearchHistoryView.as_view(),
        name="search-history",
    ),
    path(
        "search-history-delete/<int:user_id>/",
        UserVebinarSearchHistoryDeleteView.as_view(),
        name="search-history-delete",
    ),
]
