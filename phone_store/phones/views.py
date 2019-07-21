from django.shortcuts import render
from django.views.generic import DetailView
from phones.models import Phone


class PhoneDetail(DetailView):
    model = Phone
