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

# Write a string with information about each chinese zodiac:
chinese_zodiac = """    
    The Chinese zodiac is a cycle of 12 years, with each year being represented by an animal.
    The 12 animals are: Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, and Pig.
    The cycle repeats every 12 years. The years of the Chinese zodiac are determined by the Chinese calendar.
    The Chinese calendar is based on the cycles of the moon, and each month begins on the day of the new moon.
    The Chinese zodiac is based on a 12-year cycle, with each year in that cycle related to an animal sign.
    The 12-year cycle is an approximation of the 11.86-year orbital period of Jupiter around the sun.
    The 12-year cycle is also related to the 12 signs of the zodiac in Western astrology.
    The Chinese zodiac is used to represent years, months, days, and hours.
    The Chinese zodiac is also used to represent people born in a particular year, month, or day.
    The Chinese zodiac is used to determine a person's personality, compatibility with others, and fortune for the year.
    The Chinese zodiac is also used to predict the luck of a person or a business.
    The Chinese zodiac is based on a 12-year cycle, with each year in that cycle related to an animal sign.
    The 12-year cycle is an approximation of the 11.86-year orbital period of Jupiter around the sun.
    The 12-year cycle is also related to the 12 signs of the zodiac in Western astrology.
   """



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