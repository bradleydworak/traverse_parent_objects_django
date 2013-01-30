# Suppose for example your database consists of a collection of articles written by various authors published in numerous newspapers. You need to gather a list of all authors who published in a particular newspaper title called "The Chronicle". This search query/filter requires traversing the author|article|newspaper parent object relationships in Django. Assume you have a model where each Article has a foreign key to a certain newspaper and many-to-many relationships exist from authors to articles. Below is some example code on how to accomplish this.
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