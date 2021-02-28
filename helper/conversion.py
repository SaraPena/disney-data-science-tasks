'''
TODO

Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value

money_conversion("$12.2 million") --> 12200000 ## Word syntax
money_conversion("$790,000") --> 790000 ## value syntax

use test_money_conversion.py to test your solution
'''
## Try to get as many cases as possible first and continue to build from there.
## In many examples there is '$' before the number.

## Seems to be looking for many patters...makes us think regex.

import re

## First looking at the number pattern
number_pattern = r"\d+(,\d{3})*\.*\d*"

## another pattern we see is amounts such as million, billion, etc.

amounts_pattern = r"thousand|million|billion"

def parse_value_syntax(string):
    number_pattern = r"\d+(,\d{3})*\.*\d*"
    value_string = re.search(number_pattern,string).group()
    value = float(value_string.replace(",",""))


    # strip out commas before solution
    return value


def money_conversion(money):
    number_pattern = r"\d+(,\d{3})*\.*\d*"
    amounts_pattern = r"thousand|million|billion"

    word_pattern = rf"\$(?P<number>{number_pattern})\s(?P<amount>{amounts_pattern})?"
    value=re.search(word_pattern,money)

    return value

### testing 
money_conversion("$790,000") 
parse_value_syntax("$790,000")   