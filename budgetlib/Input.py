#
# This module handles inputs to the budget analyzer
#
from abc import ABCMeta, abstractmethod
from Format import BOAFormat
from Parser import BOAParser
from Budget import DefaultBudget
from collections import defaultdict

#
# Input and Parser are identified by where the data is coming from
# This is more useful than using types such as DateParser, MoneyParser
#  since if it fails, we'll know who changed their input data's format
#  and who uses similar data formats
# Keeping a history of changes, we can expect (hopefully) to anticipate
# change from who and when
#

class Input(object, metaclass=ABCMeta):
  """
  Input objects refer to input data
  for constructing a budget.

  The input is instantiated with
  an optional Format and Parser

  lines can then be read from the input
  data, formatted, and parsed into
  output data suitable for a Budget.
  """

  @abstractmethod
  def __init__(self, path, **kwargs):
    """
    path denotes the path to the input source to be read
    currently there is only support for reading files
    on disk.
    """
    pass

  @abstractmethod
  def readlines(self, **kw):
    """
    Read lines from the input
    the output is expected to be a formatted
    and parsed structure of data suitable
    for an implementation of a Budget
    """
    pass


class BOAInput(Input):
  """
   Processes CSV files from BOA
  """

  def __init__(self, path, **kwargs):

    self.fmt  = kwargs['format'] if 'format' in kwargs else BOAFormat()
    self.pars = kwargs['parser'] if 'parser' in kwargs else BOAParser()
    self.__path = path

  def __iter__(self):
    return self.readlines()

  def readlines(self):
    """
    A coroutine for reading a line at a time
    """

    with open(self.__path, 'r') as f:
      for line in f:
        yield self.fmt.format(self.pars.parse(line))

class RawUserInput(Input):
  pass

class StreamingInput(Input):
  pass

class RESTInput(Input):
  pass


