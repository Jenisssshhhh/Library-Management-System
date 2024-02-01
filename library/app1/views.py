
from rest_framework import  status,viewsets,permissions
from rest_framework.response import Response
from .models import Book, BorrowedBooks,CustomUser,BookDetails
from .serializers import BookSerializer,CustomUserSerializer,BorrowedBooksSerializer






class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []  # Specify other permissions for different actions if needed
        return [permission() for permission in permission_classes]

    

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []  # Specify other permissions for different actions if needed
        return [permission() for permission in permission_classes]


class BorrowedBooksViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []  # Specify other permissions for different actions if needed
        return [permission() for permission in permission_classes]
