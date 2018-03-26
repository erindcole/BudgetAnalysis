from abc import abstractmethod, ABCMeta
from dateutil import parser

class Parser(object, metaclass = ABCMeta):

  @abstractmethod
  def __init__(self, *args, **kw):
    pass

  @abstractmethod
  def parse(self, *args, **kw):
    pass

class BOAParser(Parser):

  def __init__(self, *args, **kw):
    """
      seqno keeps track of order of input read
      prev_date holds the previous date parsed
    """

    self.seqno = 0
    self.prev_date = None

  def parse(self, seqno, line):
    """
      line is a line of entry to process from a file
    """
    time_t, desc, change, amt = line.split(',')

    try:

      dt = parser.parse(time_t)
      ch = float(change)
      am = float(amt)

      if self.prev_date == dt:
        self.seqno += 1
      else:
        self.seqno = 0

      self.prev_date = dt

    except:
      return ()

    return (dt, self.seqno, desc, ch, am)

class PandasParser(Parser):
  pass
