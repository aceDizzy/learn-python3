formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# True and False are keywords (boolean), magiging string
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "I love you",
        "Ian Joshua love pogi",
        "I miss you",
        "Everyday"
    ))
