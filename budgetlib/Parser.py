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

  def parse(self, line):
    """
      line is a list of entries to process from a file
    """
    time_t, desc, change, amt = line

    try:
      dt = parser.parse(time_t)
      ch = float(change.strip('" \n')) if len(change) > 0 else 0.0
      am = float(amt.strip('" \n'))

      if self.prev_date == dt:
        self.seqno += 1
      else:
        self.seqno = 0

      self.prev_date = dt

    except:
      raise

    return (dt, self.seqno, desc, ch, am)

class PandasParser(Parser):
  pass
