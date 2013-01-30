# Copyright 2013
# Author: Brad Dworak

# models.py

from django.db import models

class Author(models.Model):
    articles = models.ManyToManyField("Article")
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    def __unicode__(self):
        return '{} {}'.format(self.first_name,self.last_name)

class Article(models.Model)
    newspapers = models.ForeignKey("Newspaper")
    title = models.CharField(max_length=256)
    def __unicode__(self):
        return '{}'.format(self.title)

class Newspaper(models.Model)
    title = models.CharField(max_length=256)
    def __unicode__(self):
        return '{}'.format(self.title)

# views.py

from django.template import Template, Context, RequestContext
from django.shortcuts import render_to_response

def get_authors(request):
    author_list = Author.objects.filter(articles__newspapers__title="The Chronicle")
# there are two underscores between the keywords above
    return render_to_response('author_listing.html',
            { 'author_list' : author_list }, context_instance=RequestContext(request))

# author_list.html {Django template}

{% for author in author_list %}
    {{ author.last_name }}, {{ author.first_name }}
{% endfor %}
