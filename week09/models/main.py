class Dog:
    def __inti__(self, name, age):
        self.name = name
        self.age = age

   def info(self):
        print(f"{self.name} is {self.age} years old")

    def __str__(self):
        return(f"{self.name} is {self.age} years old")

#def main():
   # my_dog = Dog("Buddy", 3)
   # my_dog.info()
   # your_dog = Dog("Paulie", 2)
   # your_dog.info()

def main():
    my_dog = Dog("Buddy", 3)
    your_dog = Dog("Paulie", 2)
    print(my_dog)
    print(your_dog)

#if __name__ == "__main__":
    #main()
