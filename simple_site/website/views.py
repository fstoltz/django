from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem, Article
# Create your views here.

#It retrieves the menu list once and then sends it to all the other views


def index(req):
	menu_item_with_article_fk = MenuItem.objects.get(name="Home")
	context = {
		"menu_items_list" : getMenuItems(),
		"article" : menu_item_with_article_fk
	}
	return render(req, 'website/index.html', context)

def about(req):
	menu_item_with_article_fk = MenuItem.objects.get(name="About")
	context = {
		"menu_items_list" : getMenuItems(),
		"article" : menu_item_with_article_fk #menu_item has foreign key to the article
	}
	return render(req, 'website/about.html', context)


def getMenuItems():
	return MenuItem.objects.filter(lang="en").order_by('display_order')