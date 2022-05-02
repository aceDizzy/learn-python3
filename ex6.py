# variable named types_of_people tapos sinet as equal to 10
types_of_people = 10
# x is equals to an f-string (f"There are {types_of_people} types of people.")
# sa loob ng {} andun 'yung variable'
x = f"There are {types_of_people} types of people."

# naggagawa lang ng variable
binary = "binary"
do_not = "don't"
# parang 'yung sa taas sa x
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
#dito na naprint 'yung There are 10 types.... who don't

# dito nagset lang ng format string tapos dineclare 'yung x at y para maikli
print(f"I said: {x}")
print(f"I also said: '{y}'")

# boolean
# evaluation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# another kind of formatting using the .format() syntax
print(joke_evaluation.format(hilarious))

# concat
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
