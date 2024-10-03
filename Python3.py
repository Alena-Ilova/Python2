class Animal:
    def __init__(self, genus, name, year_of_birth, color="unknown"):
        self.genus = genus
        self.name = name
        self.year_of_birth = year_of_birth
        self.color = color

    def get_age(self, year):
        return year - self.year_of_birth

    def get_info(self):
        print(f"{self.name} is a {self.genus}")