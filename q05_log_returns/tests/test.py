import sys, os
from pandas.plotting import lag_plot, autocorrelation_plot
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q05_log_returns
import matplotlib.pyplot as plt
from inspect import getfullargspec
import pandas as pd
import numpy as np

path = './data/bitcoin.csv'
df_ret = q05_log_returns(path)

class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q05_log_returns).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_stats_type(self):
        self.assertIsInstance(df_ret, pd.DataFrame,
                              "Expected data type for 'return value' is float you are returning %s" % (type(df_ret)))

    def test_value(self):
        self.assertAlmostEqual(df_ret.iloc[3,2], 0.9802491874707792, 2,
                               "The Expected return value does not match with the given return value")