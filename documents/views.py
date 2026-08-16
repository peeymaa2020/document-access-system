from django.http import FileResponse
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Document
from .serializers import DocumentSerializer

from users.permissions import IsAdmin
from audit.models import AuditLog


class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.filter(is_active=True)
    serializer_class = DocumentSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]

    filterset_fields = [
        "category"
    ]

    search_fields = [
        "title",
        "description"
    ]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdmin()]

        return [IsAuthenticated()]

    def perform_create(self, serializer):
        document = serializer.save(
            uploaded_by=self.request.user
        )

        AuditLog.objects.create(
            user=self.request.user,
            action="UPLOAD",
            document=document,
            description=f"Uploaded document: {document.title}",
            ip_address=self.request.META.get("REMOTE_ADDR"),
        )


class DownloadDocumentView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        document = get_object_or_404(
            Document,
            pk=pk,
            is_active=True
        )

        AuditLog.objects.create(
            user=request.user,
            action="DOWNLOAD",
            document=document,
            description=f"Downloaded document: {document.title}",
            ip_address=request.META.get("REMOTE_ADDR"),
        )

        return FileResponse(
            document.file.open("rb"),
            as_attachment=True,
            filename=document.file.name.split("/")[-1]
        )