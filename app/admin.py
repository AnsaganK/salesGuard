from django.contrib import admin

from app.models import Category, Subcategory, Profile


class SubCategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    inlines = [SubCategoryInline]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('category',)


admin.site.register(Profile)
