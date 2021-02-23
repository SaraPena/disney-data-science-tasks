'''
TODO

Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value

money_conversion("$12.2 million") --> 12200000
money_conversion("$790,000") --> 790000

use test_money_conversion.py to test your solution
'''
def money_conversion(money):
    try:
        budget = float(money.strip('$').split(' million', 1)[0].replace(',',"").split('–',1)[0].split('-')[0])
            
        if budget < 500.0:
            budget =budget * (1000000)
    
    except Exception as e:
            print(e, money)
            continue

    return budget

        
    