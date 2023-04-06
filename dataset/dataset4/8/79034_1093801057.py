from rest_framework import generics
from django.shortcuts import get_object_or_404
from .jsonserializer import GroupSerializer, SubgroupSerializer, ProductsSerializer
from .models import pGroups, pSubgroups, Products
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)