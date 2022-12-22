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

# Create a dictionary with a images of each chinese zodiac animal in jpg format:
chinese_zodiac_images = {    "Rat 🐀" : "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Chinese_zodiac_rat.svg/1200px-Chinese_zodiac_rat.svg.png",
                                "Ox 🐂" : "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Chinese_zodiac_ox.svg/1200px-Chinese_zodiac_ox.svg.png",   
                                "Tiger 🐅" : "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Chinese_zodiac_tiger.svg/1200px-Chinese_zodiac_tiger.svg.png",
                                "Rabbit 🐇" : "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Chinese_zodiac_rabbit.svg/1200px-Chinese_zodiac_rabbit.svg.png",
                                "Dragon 🐉" : "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Chinese_zodiac_dragon.svg/1200px-Chinese_zodiac_dragon.svg.png",
                                "Snake 🐍" : "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Chinese_zodiac_snake.svg/1200px-Chinese_zodiac_snake.svg.png",
                                "Horse 🐎" : "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Chinese_zodiac_horse.svg/1200px-Chinese_zodiac_horse.svg.png",
                                "Goat 🐐" : "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Chinese_zodiac_goat.svg/1200px-Chinese_zodiac_goat.svg.png",
                                "Monkey 🐒" : "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Chinese_zodiac_monkey.svg/1200px-Chinese_zodiac_monkey.svg.png",
                                "Rooster 🐓" : "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chinese_zodiac_rooster.svg/1200px-Chinese_zodiac_rooster.svg.png",
                                "Dog 🐕" : "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Chinese_zodiac_dog.svg/1200px-Chinese_zodiac_dog.svg.png",
                                "Pig 🐖" : "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Chinese_zodiac_pig.svg/1200px-Chinese_zodiac_pig.svg.png"   }

# Facts about the Chinese zodiacs:
chinese_zodiac_facts = """  The Chinese zodiac is a cycle of 12 years, with each year being represented by an animal.
                            The 12 animals are: Rat 🐀, Ox 🐂, Tiger 🐅, Rabbit 🐇, Dragon 🐉, Snake 🐍,  Horse 🐎  Goat 🐐  Monkey 🐒  Rooster 🐓  Dog 🐕  Pig 🐖.
                            The cycle repeats every 12 years. The years of the Chinese zodiac are determined by the Chinese calendar.
                            The Chinese calendar is based on the cycles of the moon, and each month begins on the day of the new moon.
                            The Chinese zodiac is based on a 12-year cycle, with each year in that cycle related to an animal sign.
                            The 12-year cycle is an approximation of the 11.86-year orbital period of Jupiter around the sun.
                            The 12-year cycle is also related to the 12 signs of the zodiac in Western astrology.
                            The Chinese zodiac is used to represent years, months, days, and hours.
                            The Chinese zodiac is also used to represent people born in a particular year, month, or day.
                            The Chinese zodiac is used to determine a person's personality, compatibility with others, and fortune for the year.
                            The Chinese zodiac is also used to predict the luck of a person or a business.
                            The most popular Chinese zodiac is the Rat 🐀 because it is the first animal in the Chinese zodiac cycle. """

# Facts about the Chinese zodiacs:
chinese_zodiac_facts_dict = {    "Rat 🐀" : "People born in the year of the Rat are quick-witted and clever.",
                                 "Ox 🐂" : "People born in the year of the Ox are hardworking and reliable.",
                                 "Tiger 🐅" : "People born in the year of the Tiger are courageous and competitive.",
                                 "Rabbit 🐇" : "People born in the year of the Rabbit are kind and considerate.",
                                 "Dragon 🐉" : "People born in the year of the Dragon are ambitious and confident.",
                                 "Snake 🐍" : "People born in the year of the Snake are wise and analytical.",
                                 "Horse 🐎" : "People born in the year of the Horse are friendly and energetic.",
                                 "Goat 🐐" : "People born in the year of the Goat are kind and gentle.",
                                 "Monkey 🐒" : "People born in the year of the Monkey are intelligent and resourceful.",
                                 "Rooster 🐓" : "People born in the year of the Rooster are honest and diligent.",
                                 "Dog 🐕" : "People born in the year of the Dog are faithful and loyal.",
                                 "Pig 🐖" : "People born in the year of the Pig are honest and hardworking."   }

# Chinese zodiacs names:
chinese_year_names = {
                    0:"Rat", 1:"Ox", 2:"Tiger", 3:"Rabbit", 
                    4:"Dragon", 5:"Snake", 6:"Horse", 7:"Goat", 
                    8:"Monkey", 9:"Rooster", 10:"Dog", 11:"Pig"
                    }

# Chinese zodiacs emojis:
chinese_year_emojis = {
                    0:'🐀', 1:'🐂', 2:'🐅', 3:'🐇', 
                    4:'🐉', 5:'🐍', 6:'🐎', 7:'🐐', 
                    8:'🐒', 9:'🐓', 10:'🐕', 11:'🐖'
                    }   
    
# The function determines the name of the year:
def chinese_zodiac(year):
    '''This function takes a year as input and returns the sign of the
     Chinese zodiac for that year.'''
    # The function returns the sign of the Chinese zodiac for that year:
    return chinese_year_names[(year - 4) % 12]

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
    emoji = chinese_year_emojis[(year - 4) % 12] # Gets the emoji of the year.
    fact = random_line() # Gets a random line from the string.
    zodiac_fact = chinese_zodiac_facts_dict[name + " " + emoji] # Gets the fact of the year.
    # return name as a dictionary:
    return {'year':year, 'name':name, 'emoji' : emoji, 'fact' : fact, 'zodiac_fact' : zodiac_fact} # Returns the name of the year.

# Run the program:
if __author__ == "__main__":
    pass