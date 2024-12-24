class Person2:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person2("Harry", "Developer")
b = Person2("Divya", "HR")
a.info()
b.info()
print(a.name)
a.name = "Divya"
a.occ = "HR"
a.info()