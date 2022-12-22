'''This program prompt the year and return the name of
the year.
'''
# Import the random module:
import random

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

# Facts about the Chinese zodiacs:
# Convert each line into a string stored in a list:
chinese_zodiac_facts = """
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
   """

# Chinese zodiacs names:
chinese_year_names = {
                    0:"Rat", 1:"Ox", 2:"Tiger", 3:"Rabbit", 
                    4:"Dragon", 5:"Snake", 6:"Horse", 7:"Goat", 
                    8:"Monkey", 9:"Rooster", 10:"Dog", 11:"Pig"
                    }

# Chinese zodiacs emojis:
chinese_year_emojis = {
                    1:'🐀', 2:'🐂', 3:'🐅', 4:'🐇', 
                    5:'🐉', 6:'🐍', 7:'🐎', 8:'🐐', 
                    9:'🐒', 10:'🐓', 11:'🐕', 12:'🐖'
                    }   
    
# The function determines the name of the year:
def chinese_zodiac(year):
    '''This function takes a year as input and returns the sign of the
     Chinese zodiac for that year.'''
    # The function returns the sign of the Chinese zodiac for that year:
    return chinese_year_names[(year + 4) % 12]

# The function returns a random line from the string:
def random_line():
    '''This function takes a string as input and returns a random line from the string.'''
    random_line = random.choice(chinese_zodiac_facts.splitlines()).strip()
    return random_line

# The function driver:
def main( inputs ):
    '''This function takes a dictionary as input and calls chinese_zodiac
    and returns the name of the year as a string.'''
    year = inputs['year'] # Gets the year from the dictionary.
    name = chinese_zodiac(year) # Gets the name of the year.
    # return name as a dictionary:
    return {'year':year, 'name':name} # Returns the name of the year.

# Run the program:
if __name__ == "__main__":
    pass