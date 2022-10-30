from distutils.command.upload import upload
from operator import mod
from unicodedata import category
from django.db import models
from numpy import save, var

class PageMeta(models.Model):
    url = models.TextField(null=False, blank=True, unique=True)
    title = models.TextField(null=False, blank=True)
    description = models.TextField(null=False, blank=True)

    def __str__(self) -> str:
        return '"' + self.url + '" - ' + self.title
    
    def save(self, *args, **kwargs):
        self.url = self.url.lower()
        if self.url == '': self.url = '/'
        if self.url[0] != '/': self.url = '/'
        if self.url[-1] != '/': self.url = self.url + '/'

        super(PageMeta, self).save(*args, **kwargs)

class Skills():
    data = {
        'Skills': {
            'python': ['Python Django', 40],
            'java': ['Java Script', 20],
            'html': ['HTML 5', 60],
            'css': ['CSS 3', 50],
            'bottstrap': ['BootStrap', 60],
            'git': ['GIT', 30],
        },
    }

# class Tiles(models.Model):
#     title = models.TextField()
#     cover = models.ImageField(upload_to = 'images/')

#     def __str__(self):
#         return self.title

class PortfolioTmp(models.Model):
    title_img = models.ImageField(upload_to = 'images/portfolio_tmp', null=False, blank=False)
    title = models.TextField(null=False, blank=False)
    date = models.TextField(null=False, blank=False)
    client = models.TextField(null=False, blank=False)
    category = models.TextField(null=False, blank=False)
    progect_url = models.URLField(null=False, blank=True)
    description = models.TextField(null=False, blank=False)
    description_numiration = models.TextField(null=False, blank=False)
    description_futter = models.TextField(null=False, blank=True)
    name = models.TextField(null=True, blank=False, unique=True)
    def url(self):
        return format_str_to_url(self.title)
    
    def __str__(self) -> str:
        return self.title

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.title.replace("/", " ").replace(" ", "_").lower(),
            "title_img_url": self.title_img.url,
            "title": self.title,
            "date": self.date,
            "client": self.client,
            "category": self.category,
            "project_url": self.progect_url,
            "description": self.description,
            "description_numiration": self.description_numiration,
            "description_futter": self.description_futter,
        }

class PortfolioImg(models.Model):
    cover = models.ImageField(upload_to = 'images/portfolio_tmp')
    product = models.ForeignKey(PortfolioTmp, on_delete = models.CASCADE, related_name='image')

#helpers

def format_str_to_url(input: str) -> str:
    return input.replace("/", " ").replace(" ", "_").lower()

