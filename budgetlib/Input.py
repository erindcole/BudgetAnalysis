#
# This module handles inputs to the budget analyzer
#

from pandas import DataFrame, read_csv

class CSVInput(object):

  def __init__(self, path, **kwargs):
    res = read_csv(path, **kwargs)
