from django import forms
from django.contrib import admin
from .models import *
from django_ckeditor_5.widgets import CKEditor5Widget
from django.utils.safestring import mark_safe



# Register your models here.

class PostAdminForm(forms.ModelForm):
      content = forms.CharField(widget=CKEditor5Widget())

      

      class Meta:
          model = Post
          fields = '__all__'
          widgets = {
              "text": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="post"
              )
          }




class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    form = PostAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'
    
    get_photo.short_description = 'Photo'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)