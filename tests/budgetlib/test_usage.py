#
#  Test Usage and Examples
#

from budgetlib import DefaultBudget, BOAFormat, BOAParser
from datetime import datetime
import csv

def mock_input(formatter, parser):
    reader = csv.reader(data, delimiter=',')
    for lines in reader:
      yield formatter.format(parser.parse(lines))

data = ['09/01/2016,Beginning balance as of 09/01/2016,,"4015.67"',
        '09/01/2016,"ATM 09/01 Withdrawal ,CA","-700.00","3315.67"',
        '09/02/2016,"PAYROLL","1697.38","5013.05"',
        '09/02/2016,"Bill Payment","-350.00","4663.05"',
        '09/08/2016,"Bill Payment","-500.00","4163.05"',
        '09/12/2016,"AHFC PMT","-246.29","3916.76"']

def test_load_csv_data():

    # instantiate parser and formatter
    formatter = BOAFormat()
    parser = BOAParser()

    # instantiate a budget
    budget = DefaultBudget('test_user')
    assert budget.name == 'test_user'

    # the real Input class calls with/open
    # so this mock mimics the behavior
    # A real implementation would be like:
    # in = BOAInput('./budget.csv')
    # and then iterate over in
    for entries in mock_input(formatter, parser):

      assert type(entries) == tuple
      assert len(entries) == 2

      budget[entries[0]] = entries[1]

    assert len(budget) == len(data)

    its  = budget.items()
    for key, vals in its:
      # test key structure
      #   (dt, seqno)

      assert len(key) == 2
      assert type(key[0]) == datetime
      assert type(key[1]) == int

      # test value structure
      #   (desc, ch, amt)

      assert len(vals) == 3
      assert type(vals[0]) == str
      assert type(vals[1]) == float
      assert type(vals[2]) == float
