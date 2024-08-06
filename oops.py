class Animal:
    def __init__(self,a,b):
        self.height=a
        self.weight=b
    def display(self):
        print(self.height,self.weight)
dog=Animal(2,100)
dog.display()


cat=Animal(9,40)
cat.display()

