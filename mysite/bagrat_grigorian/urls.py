from django.urls import path
from . import views
from bagrat_grigorian.views import portfolio_tmp_view, PortfolioImgView, portfolios


urlpatterns = [
    path('', views.about, name='about'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('portfolios', views.portfolios, name='portfolios'),
    path('<str:portfolio_name>', views.portfolio_tmp_view, name='portfolio'),
    path('portfolio_img', PortfolioImgView.as_view()),
]
