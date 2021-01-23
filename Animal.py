class Animal:
    name = 'Snow'
    color = 'White'
    age = 1
    gender = 'male'
    def __init__(self):
        self.name = 'Snow'
        self.color = 'white'
        self.age = 1
        self.gender = 'male'
        print (f"Animal's name is {self.name},color is {self.color},age is {self.age},gender is {self.gender}")
    def sing(self):
        print (f"It can sing")
    def run(self):
        print ("It can run fast")
if __name__=='__main__':
    animal = Animal()
    animal.sing()
    animal.run()



