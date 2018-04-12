import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from inspect import getfullargspec
from ..build import q09_macd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = q09_macd('data/bitcoin.csv')


class TestRead_csv_data_to_df(TestCase):

    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q09_macd).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_df_type(self):
        self.assertIsInstance(df, pd.DataFrame,
                              "Expected to return a DataFrame, you are returning %s" % (type(df)))

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(df.shape, (456, 10), "The Expected return shape does not match with the given return shape")

    def test_values(self):
        self.assertAlmostEqual(df.iloc[100,6], 1152.0,2, "The Expected return value does not match with the given return value")

    def test_values(self):
        self.assertAlmostEqual(df.iloc[100,8], 1164.0,2, "The Expected return value does not match with the given return value")