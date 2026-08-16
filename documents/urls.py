from django.urls import path
from .views import (
    DocumentListCreateView,
    DownloadDocumentView,
)

urlpatterns = [
    path(
        '',
        DocumentListCreateView.as_view(),
        name='documents'
    ),

    path(
        '<int:pk>/download/',
        DownloadDocumentView.as_view(),
        name='download-document'
    ),
]