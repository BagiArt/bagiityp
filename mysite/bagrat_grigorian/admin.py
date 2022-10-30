from django import urls
from django.contrib import admin
from .models import PortfolioTmp, PortfolioImg

# admin.site.register(PortfolioTmp)

class ImagePortfolioAdmin(admin.ModelAdmin):
    pass

class ImageInline(admin.StackedInline):
    model = PortfolioImg
    max_num = 30
    extra = 0

class ImagePortfolio(admin.ModelAdmin):
    inlines = [ImageInline,]

admin.site.register(PortfolioImg, ImagePortfolioAdmin)
admin.site.register(PortfolioTmp, ImagePortfolio)