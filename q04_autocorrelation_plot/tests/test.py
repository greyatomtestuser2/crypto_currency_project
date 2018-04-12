import sys, os
from pandas.plotting import lag_plot, autocorrelation_plot
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q04_autocorrelation_plot
import matplotlib.pyplot as plt
from inspect import getfullargspec
import pandas

path = './data/bitcoin.csv'
q04_autocorrelation_plot(path)

class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q04_autocorrelation_plot).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

