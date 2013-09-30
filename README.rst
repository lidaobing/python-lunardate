A Chinese Calendar Library in Pure Python
=========================================

.. image:: https://travis-ci.org/lidaobing/python-lunardate.png?branch=master   :target: https://travis-ci.org/lidaobing/python-lunardate

Chinese Calendar: http://en.wikipedia.org/wiki/Chinese_calendar

Usage
-----
        >>> LunarDate.fromSolarDate(1976, 10, 1)
        LunarDate(1976, 8, 8, 1)
        >>> LunarDate(1976, 8, 8, 1).toSolarDate()
        datetime.date(1976, 10, 1)
        >>> LunarDate(1976, 8, 8, 1).year
        1976
        >>> LunarDate(1976, 8, 8, 1).month
        8
        >>> LunarDate(1976, 8, 8, 1).day
        8
        >>> LunarDate(1976, 8, 8, 1).isLeapMonth
        True

        >>> today = LunarDate.today()
        >>> type(today).__name__
        'LunarDate'

        >>> # support '+' and '-' between datetime.date and datetime.timedelta
        >>> ld = LunarDate(1976,8,8)
        >>> sd = datetime.date(2008,1,1)
        >>> td = datetime.timedelta(days=10)
        >>> ld-ld
        datetime.timedelta(0)
        >>> ld-sd
        datetime.timedelta(-11444)
        >>> ld-td
        LunarDate(1976, 7, 27, 0)
        >>> sd-ld
        datetime.timedelta(11444)
        >>> ld+td
        LunarDate(1976, 8, 18, 0)
        >>> td+ld
        LunarDate(1976, 8, 18, 0)
        >>> ld2 = LunarDate.today()
        >>> ld < ld2
        True
        >>> ld <= ld2
        True
        >>> ld > ld2
        False
        >>> ld >= ld2
        False
        >>> ld == ld2
        False
        >>> ld != ld2
        True
        >>> ld == ld
        True

News
----

* 0.1.4: support '+', '-' and compare, fix bug in year 2050
* 0.1.3: support python 3.0

Limits
------

this library can only deal with year from 1900 to 2049 (in chinese calendar).

See also
--------

* lunar: http://packages.qa.debian.org/l/lunar.html,
  A converter written in C, this program is derived from it.
* python-lunar: http://code.google.com/p/liblunar/
  Another library written in C, including a python binding.
