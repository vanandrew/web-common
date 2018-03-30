from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .models import (lab_member, publication, news_item, job_listing,
    current_study, data_listing, software_listing)
from datetime import datetime
import json
import os

# homepage
def home_page(request):
    return render(request, 'common/home.html')

# index homepage
def index_page(request):
    return render(request, 'common/index.html')

# lab member page
def people_page(request):
    # Get all lab members
    members = lab_member.objects.all().order_by('last_name')
    return render(request, 'common/people.html', {'members': members})

# research
def research_page(request):
    return render(request, 'common/research.html')

# publications
def publications_page(request):
    publications = publication.objects.all().order_by('-date')
    dateobjs = publication.objects.dates('date','year',order='DESC')
    years = [date.year for date in dateobjs]
    return render(request, 'common/publications.html', {'publications': publications, 'years': years})

# news
def news_page(request):
    news = news_item.objects.all()
    return render(request, 'common/news.html',{'news': news})

# data
def data_page(request):
    data = data_listing.objects.all().order_by('title')
    return render(request, 'common/data.html', {'data': data})

# software
def software_page(request):
    software = software_listing.objects.all().order_by('title')
    return render(request, 'common/software.html', {'software': software})

# directions
def directions_page(request):
    return render(request, 'common/directions.html')

# participate
def participate_page(request):
    currentstudies = current_study.objects.all().order_by('title')
    return render(request, 'common/participate.html', {'currentstudies': currentstudies})

# careers
def careers_page(request):
    jobpostings = job_listing.objects.all().order_by('-post_date')
    return render(request, 'common/careers.html', {'jobpostings': jobpostings})

# contact
def contact_page(request):
    return render(request, 'common/contact.html')
