class Contact():
    def __init__(self, id, first_name, last_name, day, month, year, profession):
        self.id = id 
        self.first_name = first_name
        self.last_name = last_name
        self.day = day
        self.month = month
        self.year = year
        self.profession = profession

    def get_information(self):
        print (f' ID - {self.id}\n Full name - {self.first_name} {self.last_name}\n Birth Date - {self.day}.{self.month}.{self.year} \n Profession - {self.profession} \n')

c = Contact("1", "John", "Dow", "21", "04", "1996", "Python developer")
c.get_information()


new_contact = Contact("2", "Mary", "Jason", "26", "01", "1999", "Nurse")
c.get_information()
                                                          