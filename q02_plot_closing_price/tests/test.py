import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_plot_closing_price
import matplotlib.pyplot as plt
from inspect import getfullargspec
import pandas

path = './data/bitcoin.csv'
q02_plot_closing_price(path)

class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q02_plot_closing_price).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

