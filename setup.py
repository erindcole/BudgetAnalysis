python-dateutil, pandas, pytest

from setuptools import setup, find_packages

# TODO:
# See http://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
#  add author, license, keywords, description, name, classifiers, url, entry_points
setup(
    name='BudgetAnalyzer',
    version='0.0.1',
    description="See how bad you are at spendin teh moneyz",
    classifiers=[
                      'Development Status :: 3 - Alpha',
                      'Environment :: Console',
                      'Intended Audience :: Developers',
                      'Programming Language :: Python',
                ],
    keywords='budget moneyz money finance',
    author=['M. Sandan', 'Erin Cole']
    packages = find_packages('budgetlib'),
    package_dir = {'': 'budgetlib'},
    include_package_data = True,
    tests_require=['pytest >= 2.5.2'],
    install_requires=['py-dateutil']
)
