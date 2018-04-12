import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from inspect import getfullargspec
from ..build import q06_stationarity
import pandas as pd
import numpy as np

stat, pval = q06_stationarity('data/bitcoin.csv')


class TestRead_csv_data_to_df(TestCase):

    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q06_stationarity).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_stats_type(self):
        self.assertIsInstance(stat, float,
                              "Expected data type for 'test statistic' is float you are returning %s" % (type(stat)))

    def test_pval_type(self):
        self.assertIsInstance(pval, float,
                              "Expected data type for 'p - value' is float you are returning %s" % (type(pval)))

    def test_stat_value(self):
        self.assertAlmostEqual(stat, -1.2913031353276294, 2,
                               "The Expected values of test statistic does not match with the given return value")

    def test_pval_value(self):
        self.assertAlmostEqual(pval, 0.6331416877788254, 2,
                               "The Expected values of 'p - value' does not match with the given return value")
