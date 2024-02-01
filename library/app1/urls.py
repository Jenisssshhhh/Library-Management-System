# app1/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, BookViewSet, BorrowedBooksViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowed-books', BorrowedBooksViewSet)

app_name = 'app1'



urlpatterns = router.urls
