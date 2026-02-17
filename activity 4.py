class India():
    def capital(self):
        print("new delhi is the capital of india.")

    def language(self):
        print("hindi is the most widely spoken language in india.")

    def type(self):
        print("india is a developing country.")

class USA():
    def capital(self):
        print("washington dc is the capital of usa.")

    def language(self):
        print("english is the primary language of usa.")

    def type(self):
        print("usa is a developed country.")

obj_ind = india()
obj_usa = usa()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

