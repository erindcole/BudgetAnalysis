from abc import abstractmethod, ABCMeta
from pandas import DataFrame
from dateutils import parse

class Parser(object, metaclass = ABCMeta):
  def __init__(self, *args, **kw):
    pass

  def parse(self, *args, **kw):
    pass

class PandasParser(Parser):

  def __init__(self, *args, **kw)
