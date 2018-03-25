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

  @absractmethod
  def __init__(self, time_t, desc, change, amt):

    try:
      dt = parser.parse(time_t)
      ch = float(change)
      am = float(amt)

    except:
      return ()

    return (dt, desc, ch, am)

