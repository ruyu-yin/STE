from Animal import Animal
class Cat(Animal):
    hair = "short hair"
    def __init__(self):
        self.name = 'Snow'
        self.color = 'white'
        self.age = 1
        self.gender = 'male'
        self.hair = "short hair"
        print(f"Name is {self.name},color is {self.color},"
              f"age is {self.age},gender is {self.gender},hair is {self.hair}")

    def sing(self):
        print("It can 喵喵叫")
    def run(self):
        print("It can run fast")
    def skill(self):
        print ("It can catch mouse")
if __name__ == '__main__':
    cat = Cat()
    cat.sing()
    cat.run()
    cat.skill()



