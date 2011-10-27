import os
import sys

sys.path = [
    os.path.join(os.path.dirname(__file__), '../../src'),
] + sys.path

from django.db import models
from naturalsortfield import NaturalSortField


class TestModel(models.Model):
    title = models.CharField(max_length=255)
    title_sort = NaturalSortField('title')
