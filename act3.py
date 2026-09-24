class india:
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is a developing country")
class USA:
    def capital(self):
        print("Washington, D.C. is the capital of the USA")
    def language(self):
        print("English is the most widely spoken language of the USA")
    def type(self):
        print("USA is a developed country")
objind = india()
objusa = USA()

for country in (objind, objusa):
    country.capital()
    country.language()
    country.type()