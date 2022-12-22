'''This program prompt the year and return the name of
the year.
'''

# Path: src/Chinese_Years.py
# Name the writer:
__author__ = "Adrian Lozada", "Jiahui Dang"
# Name the program:
__program__ = "Chinese Years"
# Name the version:
__version__ = "1.0.0"
# Name the date:
__date__ = "2021/02/09"
# Name the description:
__description__ = "This program prompt the year and return the name of the year."
# Name the license:
__license__ = "MIT"

# Write a dictionary that stores the names of the years:
chinese_year_names = {
                    1:'Rat', 2:'Ox', 3:'Tiger', 4:'Rabbit', 
                    5:'Dragon', 6:'Snake', 7:'Horse', 8:'Goat', 
                    9:'Monkey', 10:'Rooster', 11:'Dog', 12:'Pig'
                    }

# The function determines the name of the year:
def chinese_zodiac(year) -> str:
    '''This function takes a year as input and returns the sign of the
     Chinese zodiac for that year.'''
    return chinese_year_names[(year - 3) % 12]

# The function driver:
def main(chinese_year_names) -> str:
    '''This function takes a dictionary as input and calls chinese_zodiac
    and returns the name of the year as a string.'''
    year = int(input('Enter the year: '))
    name = chinese_year_names[(year - 3) % 12]
    return name