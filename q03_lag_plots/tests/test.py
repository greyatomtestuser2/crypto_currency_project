import sys, os
from pandas.plotting import lag_plot, autocorrelation_plot
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q03_lag_plots
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from inspect import getfullargspec
import pandas

path = './data/bitcoin.csv'
q03_lag_plots(path,4)

class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q03_lag_plots).args
        self.assertEqual(len(arg), 2, "Expected argument(s) %d, Given %d" % (1, len(arg)))

