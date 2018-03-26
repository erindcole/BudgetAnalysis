from abc import abstractmethod, ABCMeta
from dateutil import parser

class Format(object):

  @abstractmethod
  def __init__(self, *args, **kw):
    pass


class BOAFormat(Format):
  """
    Defines and parses BOA format
    Ex.
          time              desc               change     amt
      09/01/2016, "BKOFAMERICA ATM WITHDRWL", "-7.00", "99999.99"
  """
  def format(self, line):
    """
      Validate and format data from input
    """
    if type(line) != tuple and len(line) != 5:
      raise ValueError('[Unexpected Input]\n{}'.format(str(line)))

    dt, seqno, desc, ch, amt = line
    key = (dt, seqno)
    val = (desc, ch, amt)

    return (key, val)
