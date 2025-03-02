"""This is test module for crudatalab client with test credentials"""

import unittest
import crudatalab
import os

class TestKnoemaClient(unittest.TestCase):
    """This is class with crudatalab client unit tests with test credentials"""

    base_host = 'datalab.crugroup.com'

    def setUp(self):
        apicfg = crudatalab.ApiConfig()
        apicfg.host = os.environ['BASE_HOST'] if 'BASE_HOST' in os.environ else self.base_host
        apicfg.app_id = os.environ['KNOEMA_APP_ID'] if 'KNOEMA_APP_ID' in os.environ else ''
        apicfg.app_secret = os.environ['KNOEMA_APP_SECRET'] if 'KNOEMA_APP_SECRET' in os.environ else ''

    def test_getdata_by_TransformationDataReader_timemembers(self):
        """The method is testing getting single series by dimension member ids"""

        data_frame = crudatalab.get('IMFWEO2021Apr', Country='614', Subject='BCA', timemembers='1980;2002;2023')
        self.assertEqual(data_frame.shape[0], 3)
        self.assertEqual(data_frame.shape[1], 1)

        self.assertEqual(['Country', 'Subject', 'Frequency'], data_frame.columns.names)

        indx = data_frame.first_valid_index()
        sname = ('Angola', 'Current account balance (U.S. dollars)', 'A')
        value = data_frame.at[indx, sname]
        self.assertEqual(value, 0.07)

        indx = data_frame.index[2]
        value = data_frame.at[indx, sname]
        self.assertEqual(value, -0.154)

    def test_getdata_by_TransformationDataReader_timesince(self):
        """The method is testing getting single series by dimension member ids"""

        data_frame = crudatalab.get('IMFWEO2021Apr', Country='614', Subject='BCA', timesince='2013')
        self.assertEqual(data_frame.shape[0], 14)
        self.assertEqual(data_frame.shape[1], 1)

        self.assertEqual(['Country', 'Subject', 'Frequency'], data_frame.columns.names)

        indx = data_frame.first_valid_index()
        sname = ('Angola', 'Current account balance (U.S. dollars)', 'A')
        value = data_frame.at[indx, sname]
        self.assertEqual(value, 8.348)

        indx = data_frame.index[13]
        value = data_frame.at[indx, sname]
        self.assertEqual(value, -0.457)

    def test_getdata_by_TransformationDataReader_timelast1(self):
        """The method is testing getting multiple series by dimension member ids and time range"""

        data_frame = crudatalab.get('IMFDOT2017', **{'Country': 'Algeria;Angola', 'Indicator': 'TXG_FOB_USD', 'Counterpart Country': '622', 'frequency': 'A;Q', 'timelast': '1'})

        self.assertEqual(data_frame.shape[0], 4)
        self.assertEqual(data_frame.shape[1], 4)
