"""This is test module for crudatalab client (Upload)"""
"""Works only with special credentials"""

import unittest
import datetime
import crudatalab
import urllib
import pandas
import os
import numpy

class TestKnoemaClient(unittest.TestCase):
    """This is class with crudatalab client unit tests (Upload)"""

    base_host = 'datalab.crugroup.com'

    def setUp(self):
        apicfg = crudatalab.ApiConfig()
        apicfg.host = os.environ['BASE_HOST'] if 'BASE_HOST' in os.environ else self.base_host
        apicfg.app_id = os.environ['KNOEMA_APP_ID'] if 'KNOEMA_APP_ID' in os.environ else ''
        apicfg.app_secret = os.environ['KNOEMA_APP_SECRET'] if 'KNOEMA_APP_SECRET' in os.environ else ''

    def test_delete_dataset_negative(self):
        """The method is negative test on dataset deletion"""
         
        with self.assertRaises(urllib.error.HTTPError) as context:
            crudatalab.delete('non_existing_id')
        self.assertTrue('HTTP Error 400: Bad Request' in str(context.exception))

    def test_verify_dataset_negative(self):
        """The method is negative test on dataset verification"""

        with self.assertRaises(ValueError) as context:
            crudatalab.verify('non_existing_id', datetime.date.today(), 'IMF', 'http://datalab.crugroup.com/')
        self.assertTrue("Dataset has not been verified, because of the following error(s): Requested dataset doesn't exist or you don't have access to it." in str(context.exception))

    def test_incorrect_host_delete_dataset(self):
        """The method is negative test on delete dataset with incorrect host"""

        with self.assertRaises(ValueError) as context:
            apicfg = crudatalab.ApiConfig()
            apicfg.host = 'crudatalab_incorect.com'
            crudatalab.delete('dataset')
        self.assertTrue("The specified host crudatalab_incorect.com does not exist" in str(context.exception))

    def test_incorrect_host_verify_dataset(self):
        """The method is negative test on verify dataset with incorrect host"""

        with self.assertRaises(ValueError) as context:
            apicfg = crudatalab.ApiConfig()
            apicfg.host = 'crudatalab_incorect.com'
            crudatalab.verify('non_existing_id', datetime.date.today(), 'IMF', 'http://datalab.crugroup.com')
        self.assertTrue("The specified host crudatalab_incorect.com does not exist" in str(context.exception))    

    def test_upload_generated_frames(self):
        tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
        index = pandas.MultiIndex.from_tuples(tuples, names=['first', 'second'])
        dates = pandas.date_range('1/1/2000', periods=8)
        frame = pandas.DataFrame(numpy.random.randn(8, 8), index=dates, columns=index)
        res = crudatalab.upload(frame, name = 'Test dataset')
        self.assertIs(type(res), str)
        self.assertEqual(len(res), 7)

        frame = pandas.DataFrame(numpy.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
        res = crudatalab.upload(frame, name = 'Test dataset')
        self.assertIs(type(res), str)
        self.assertEqual(len(res), 7)

    def test_upload_frames_from_existing_datasets(self):
        frame = crudatalab.get('xmhdwqf', company='UBER', indicator='Annual', frequency='A', timerange='2018-2020')
        res = crudatalab.upload(frame, name = 'Test dataset')

        self.assertIs(type(res), str)
        self.assertEqual(len(res), 7)