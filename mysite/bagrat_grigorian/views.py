from typing import List
from black import re
from django.forms import models
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.template import context
from .models import PortfolioTmp, PortfolioImg, PageMeta, Skills
from django.views.generic import ListView

def get_context(request):
    meta: PageMeta = PageMeta.objects.filter(url=request.path.lower()).first()
    if meta is None:
        meta = PageMeta.objects.filter(url="/").first()
    
    return {
        "meta_title": meta.title if meta else "",
        "meta_description": meta.description if meta else "",
    }

def base(request):
    return render(request, 'bagrat_grigorian/base.html', {})

def about(request):
    data = Skills.data
    data["image"] = { 'img': PortfolioTmp.objects.all() }
    return render(request, 'bagrat_grigorian/about.html', data)

def contact(request):
    return render(request, 'bagrat_grigorian/contact.html')

def portfolio_tmp_view(request, portfolio_id: int = None, portfolio_name: str = None):
    if portfolio_id:
        item: PortfolioTmp = get_object_or_404(PortfolioTmp, id=portfolio_id)
    else:
        item: PortfolioTmp = get_object_or_404(PortfolioTmp, name__iexact=portfolio_name)
    context = get_context(request)
    context = { 'portfolios': PortfolioTmp.objects.all() }
    context['portfolio'] = item
    context['images'] = { 'all_images': PortfolioImgView.model.objects.all() }
    return render(request, 'bagrat_grigorian/portfolio_tmp.html', context)

def portfolios(request):
    context = get_context(request)
    context["portfolios"] = PortfolioTmp.objects.order_by("id")
    return render(request, "bagrat_grigorian/portfolio.html", context)

class PortfolioImgView(ListView):
    model = PortfolioImg
    products = PortfolioImg.product
    template_name = 'bagrat_grigorian/portfolio_tmp.html'

