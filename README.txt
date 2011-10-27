django-naturalsortfield: Better ordering for CharFields. Ignores spaces at
the start of a string, does the right thing with integers, scorns the word
"the".

Example:
    >>> from django.db import models
    >>> from naturalsortfield import NaturalSortField
    ...
    >>> class MyModel(models.Model):
    ...     title = models.CharField(max_length=255)
    ...     title_sort = NaturalSortField()
    ...
    >>> MyModel.objects.create(title='ABC')
    >>> MyModel.objects.create(title='XYZ 1')
    >>> MyModel.objects.create(title='The XYZ 2')
    >>> MyModel.objects.create(title='XYZ 10')
    >>> [obj.title for obj.title in MyModel.objects.order_by('title_sort')
    ['ABC', 'XYZ 1', 'The XYZ 2', 'XYZ 10']
