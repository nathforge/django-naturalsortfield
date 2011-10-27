from testproject.testapp.models import TestModel
import unittest


class TestNaturalSortField(unittest.TestCase):
    def test(self):
        TestModel.objects.create(title='The XYZ 3')
        TestModel.objects.create(title='XYZ 1')
        TestModel.objects.create(title='XYZ 10')
        TestModel.objects.create(title='XYZ 2')
        
        self.assertEqual(
            [obj.title for obj in TestModel.objects.order_by('title_sort')],
            ['XYZ 1', 'XYZ 2', 'The XYZ 3', 'XYZ 10']
        )
