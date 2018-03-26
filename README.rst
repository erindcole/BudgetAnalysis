This project allows a user to set up and analyze a budget.

Budget Analyzer
===============
Have no idea where your money is going? Always feel like you should have more money?
Does it suck to be you? Well you are not alone! Budget Analyzer is here to help you map out your day to day
expenses and help you to become more aware of your financial activity.

See how saving some money consistently and spending money
can add up over time. Plan for the future, play around with the numbers, set goals.

See all gas purchases in a certain time period, edit descriptions of purchases,
tag purchases, see the 10 most expensive transaction, the 10 highest deposists.
Analyze correlations in purchases. If I buy x how likely am I to buy Y?
See hidden trends in spending habits.

Get involved with the community. 

Answer the really deep questions in life:
- Can I afford to buy a dog? For how long?
- Can I afford to 
- Why do I suck?

Don't suck, make it easier with Budget Analyzer

Development
===============
Don't suck. Contribute.

Dev Guidelines
====

Testing
====
We use pytest.

Typical usage:

.. code:: python

    # test all the things! 
    py.test -s tests/*

    # run tests in this file
    py.test -s tests/budgetlib/test_suite.py

    # run TestClass in the the file
    py.test -s tests/budgetlib/test_suite.py::TestClass

    # just run a specific method in TestClass
    py.test -s test/budgetlib/test_suite.py::TestClass::test_func

see the `pytest docs`_ for more info


.. _pytest docs: http://pytest.org/latest/contents.html#toc
