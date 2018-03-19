from pandas import DataFrame
from abc import ABCMeta, abstractmethod

class Budget(object, metaclass=ABCMeta):
  """
    A Budget is a time series with multiple index hierarchies
    [Year][Month][Day][SeqNo]
    Each transaction has a year, month, day, and sequence number
  """

  @abstractmethod
  def __init__(self, *args, **kw):
    pass

  @abstractmethod
  def __getitem__(self, x):
    pass

  @abstractmethod
  def __iter__(self):
    pass

  @abstractmethod
  def __len__(self):
    pass

  @abstractmethod
  def __setitem__(self, key, value):
    pass

  @abstractmethod
  def __repr__(self):
    pass

  @abstractmethod
  def __str__(self):
    pass

  @abstractmethod
  def values(self):
    pass

  @abstractmethod
  def keys(self):
    pass

  @abstractmethod
  def items(self):
    pass

class DefaultBudget(Budget):
  """
    DefaultBudget uses dictionaries to implement Budget
      This class is implemented using the datetime module.
      Keys are tuples of (datetime instances, seqno (ints))
  """
  pass

class TimeIndexKeyBudget(Budget):
  """
  TimeIndexKeyBudget uses a TimeIndexKey to implement Budget.
  """
  pass

class TimeIndexKeyRangeBudget(Budget):
  """
  TimeIndexKeyRangeBudget is optimized for range type queries on a Budget.
  """
  pass
