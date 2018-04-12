import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from inspect import getfullargspec
from ..build import q10_predict_using_fbprophet
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from fbprophet import Prophet


df = q10_predict_using_fbprophet('data/bitcoin.csv')


class TestRead_csv_data_to_df(TestCase):

    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q10_predict_using_fbprophet).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_df_type(self):
        self.assertIsInstance(df, pd.Series,
                              "Expected to return a Series, you are returning %s" % (type(df)))

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(df.shape, (463, ), "The Expected return shape does not match with the given return shape")

    def test_values(self):
        self.assertAlmostEqual(df.iloc[100,], 1434.5491041514808,2, "The Expected return value does not match with the given return value")

    def test_values(self):
        self.assertAlmostEqual(df.iloc[456,], 7442.609681789451,2, "The Expected return value does not match with the given return value")