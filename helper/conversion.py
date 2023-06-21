import re
# Finds digits with pattern ###,###,###.XX
number = r"\d+(,\d{3})*\.*\d*" 
amounts = r"thousand|million|billion"

value_re = rf"\${number}"
word_re = rf"\${number}(-|\sto\s)?({number})?\s({amounts})"



'''
TODO
Goal: Capture the pattern in 'Budget', each quantifier follows '$'
Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value



test_money_conversion.py to test my solution
'''

def word_to_value(word):
	value_dict = {"thousand":1000, "million": 1000000, "billion":1000000000}
	return value_dict[word]

def parse_word_syntax(string):
	value_string = re.search(number, string).group()
	value = float(re.sub(",", "", value_string))
	word = re.search(amounts, string, flags=re.I).group().lower() #re.I ignores Million vs million
	word_value = word_to_value(word)
	return value * word_value


def parse_value_syntax(string):
	value_string = re.search(number, string).group()
	value = float(re.sub(",", "", value_string)) 	# Strip commas
	return value

# money_conversion("$12.2 million") --> 12200000 ## Word Syntax
# money_conversion("$790,000") --> 790000  ## Value Syntax

def money_conversion(money):
	if isinstance(money,list):
		money = money[0]
	value_syntax = re.search(value_re, money, flags=re.I)
	word_syntax = re.search(word_re, money)

	if word_syntax:
		return parse_word_syntax(word_syntax.group())
	elif value_syntax:
		return parse_value_syntax(value_syntax.group())

print(money_conversion("$12.2 billion"))