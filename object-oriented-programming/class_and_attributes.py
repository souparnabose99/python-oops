

class ProgrammingLanguages:

    def __init__(self, language):
        self.language = language


# pl = ProgrammingLanguages()
# TypeError: ProgrammingLanguages.__init__() missing 1 required positional argument: 'language'
pl = ProgrammingLanguages("Java")
print(type(pl))
print(pl.language)

# ----- @TODO Console Output -----

# <class '__main__.ProgrammingLanguages'>
# Java


