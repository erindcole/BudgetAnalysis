#
# Best Practices:
#  Code must not rely on correctness of data
#  Validation must occur to ensure integrity of results
#  This implementation has the validation logic baked into each class
#
from datetime import datetime
class TimeIndexKey(object):
  """
  TimeIndexKey is the hierarchical index used to index entries in the budget
  A TimeIndexKey is then a list of Years

  [
   (2017,
     (1,
       (22, ((1, val), (2, val), (3, val))),
       (23, ((1, val), (2, val), (3, val)))),
     (2,
       (1, ((1, val), (2, val), (3, val))),
       (2, ((1, val), (2, val), (3, val)))),
   )
   .
   .
   .
   (2018, (12, (30, ((1, val), (2, val), (3, val)))))
  ]
  """
  def __init__(self, *args, **kw):
    """
    Data isn't expected to come in sorted.
    We should sort the Year objects given deeply.
    This should help for doing range type queries
    """
    self.values = list(args)

  @property
  def values(self):
    return self.__value

  @values.setter
  def values(self, val):
     isYear = lambda x: isinstance(x, Year)
     res = {isYear(x) for x in val}

     if len(res) !=1 or False in res:
      raise ValueError("TimeIndexKey must be instantiated with Year objects")

    self.__value = val

  def get(self, month=1, day=1, seqno=1):
    """
    return the value associated with the time given
    TODO: consider making this a generator to yield
          the next month's values after a subsequent
          call to get(), or perhaps move it to a method called next()
    """
    isMonth = lambda m: m.key == month
    isDay = lambda d: d.key == day
    isSeqNo = lambda s: s.key == seqno

    return filter(isSeqNo, filter(isDay, filter(isMonth, self.value.months)))

class Year(object):
  """
  Year is a representation of the year of a transaction
    This class contains Month objects and is the highest granularity

    Year
      Month
        Day
          SeqNo 1: val
          SeqNo 2: val
          SeqNo 3: val
  (2017, (1, (22, ((1, val), (2, val), (3, val)))))

  An instance of Year represents all the transactions
  in a single year.

  Attributes:
    - key: The year as a string
    - value: tuple of Month objects
  """
  def __init__(self, yr, *args, **kw):
    """
    yr : numeric representing the year
    *args : Month objects
    """
    self.key = yr
    self.months = args

  @property
  def key(self):
    """
    Returns the year
    """
    return self.__key

  @key.setter
  def key(self, yr):
    """
    Sets the year
    """
    try:
      # TODO: add more validation
      int(yr)
    except:
      raise ValueError("invalid year: {}".format(str(yr)))
    self.__key = yr

  @property
  def months(self, year):
    """
    Returns a tuple of Month objects for the given year
    """
    return self.__value

  @months.setter
  def months(self, m):
    # make sure the input given is of Month type
    # each Month is self-validated

    isMonth = lambda x: isinstance(x, Month)
    x = {isMonth(month) for month in m}

    if len(x) != 1 or False in x:
      raise ValueError("Invalid months given. Use Time.Month objects.")

    self.__value = m

  def __len__(self):
    return len(self.months)

  def __iter__(self):
    return iter(self.months)

  def __str__(self):
    return str(self.key)

  def __repr__(self):
    return self.key

#  TODO: move to Budget
#  def get(self, value = None):
#    if value is None:
#      return self.months
#
#    else:
#      result = list(filter(lambda x: x.key == value, self.months))
#      return result or None

class Month(object):
  """
  Month is a representation of the month of a transaction
    This class contains Day objects

  An instance of Month represents all the transactions
  in a single month of a given year.
  """

  month_names = {1: 'january',
                 2: 'february',
                 3: 'march',
                 4: 'april',
                 5: 'may',
                 6: 'june',
                 7: 'july',
                 8: 'august',
                 9: 'september',
                10: 'october',
                11: 'november',
                12: 'december'}

  def __init__(self, mo, *args, **kw):
    """
      - mo: the month as a numeric
      - *args: the Day objects associated with this Month
    """
    self.key = mo
    self.days = args

  @property
  def key(self):
    """
    Returns the month
    """
    return self.__key

  @key.setter
  def key(self, month):
    """
    Sets the month
    """
    try:
      # TODO: add more validation
      int(month)
      month_names[month]
    except:
      raise ValueError("invalid month: {}".format(month))
    self.__key = month

  @property
  def days(self):
    return self.__value

  @days.setter
  def days(self, d):

    isDay = lambda x: isinstance(d, Day)
    x = {isDay(day) for day in d}

    if len(x) != 1 or False in x:
      raise ValueError("Invalid days given. Use Time.Day objects.")

    self.__value = d

  def __len__(self):
    return len(self.days)

  def __iter__(self):
    return iter(self.days)

  def __str__(self):
    return str(self.key)

  def __repr__(self):
    return month_names[self.key]

class Day(object):
  """
  Day is a representation of the day of a transaction
    This class contains SequenceNo objects

  An instance of Day represents all the transactions
  in a single day of a given month and a given year.
  """
  day_names = ['monday', 'tuesday', 'wednesday', 'thursday',
               'friday', 'saturday', 'sunday']

  def __init__(self, day, *args, **kw):
    self.key = day
    self.seqno = args

  @property
  def key(self):
    return self.__key

  @key.setter
  def key(self, day):
    # TODO: add more validation
    if (type(day) != int or (day < 0 or day > 31)):
      raise ValueError("Invalid Day: {}".format(str(day)))
    self.__key = seqno

  @property
  def seqno(self):
    return self.__value

  @seqno.setteer
  def seqno(self, no):

    isSeqNo = lambda x: isinstance(x, SequenceNo)
    x = {isSeqNo(s) for s in no}

    if len(x) != 1 or False in x:
      raise ValueError("Invalid Sequence number given. Use Time.SequenceNo objects.")

    self.__value = no

  def __len__(self):
    return len(self.seqno)

  def __str__(self):
    return str(self.key)

  def __repr__(self):
    # TODO: map these to the day of the year
    return self.key

  def __iter__(self):
    return iter(self.seqno)

class SequenceNo(object):
  """
  SequenceNo is simply the order in which transactions
  take place for the same day of the month of the year.
  """
  def __init__(self, num, value, **kw):
    self.key = int(num)
    self.value = float(value)

  def __str__(self):
    return str((self.key, self.value))

  def __repr__(self):
    return (self.key, self.value)
