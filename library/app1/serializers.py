from rest_framework import serializers
from .models import Book, BorrowedBooks,CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password','email','Phone_number','Address','MembershipDate']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    




class BookSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Book
        fields = '__all__'



class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['User', 'Book', 'Borrow_date', 'Return_date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_username'] = instance.User.username
        representation['book_title'] = instance.Book.Title
        return representation
