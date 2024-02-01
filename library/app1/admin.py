from django.contrib import admin
from .models import CustomUser,Book,BookDetails,BorrowedBooks
from django.contrib.auth.admin import UserAdmin
from django import forms



class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'Phone_number', 'Address', 'MembershipDate', 'password')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'Phone_number', 'Address', 'MembershipDate', 'password'),
        }),
    )

    list_display = ('username', 'email', 'Phone_number', 'Address', 'MembershipDate')
    search_fields = ('username', 'email')



    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('Phone_number', 'Address', 'MembershipDate')}),
      
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)




class BorrowedBooksAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'book_title', 'Borrow_date', 'Return_date')

    def user_name(self, obj):
        return obj.User.username

    def book_title(self, obj):
        return obj.Book.Title

    user_name.short_description = 'User'
    book_title.short_description = 'Borrowed Book Title'

admin.site.register(BorrowedBooks, BorrowedBooksAdmin)




admin.site.register([Book,BookDetails])