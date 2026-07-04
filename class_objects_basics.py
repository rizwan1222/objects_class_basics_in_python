print("****** This is my first program in oops ******")
class student:
 def __init__(self,fullname):
    self.name=fullname


s1=student("rizwan")
print(s1.name)
s2=student("rizwan")
print(s2.name)


print("\nQ1 :-  Create a class student with two attributes name and marks. Create a method to calculate the average marks of the student and print it. Create an object of the class and call the method.\n")
print("****** This is my second program in oops ******")
class student :
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks

    def method(self):
        sum=0
        for i in self.marks:
            sum = sum + i

        print("HI " , self.name, "Your avg score is ", sum/3)


s1=student("Rizwan" , [98,99,98])
print(s1.name,s1.marks)
s1.method()

print("\nQ2 :- Create a class car with two attributes model and year. Create a method to print the details of the car. Create another class german which inherits the car class and has an additional attribute price. Override the method to print the details of the german car including its price. Create an object of the german class and call the method.\n")

class car:
    def __init__(self,model,year):
        self.model=model
        self.year=year

    def car_details(self):
        print("Car model is ",self.model)
        print("Car year is ",self.year)

class german(car):
    def __init__(self,model,year,price):
        super().__init__(model,year)
        self.price=price

    def car_details(self):
        print("Car model is ",self.model)
        print("Car year is ",self.year)
        print("Car price is ",self.price)


    
    
    
c1 = german("Corolla",2020,20000)
c1.car_details()
c2 = car("Honda",2019)
c2.car_details()

print("\nClass method\n")

class student:
    grade= "D"
    name="Riz"

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    @classmethod
    def college(cls,name,grade):
        cls.name=name   
        cls.grade=grade


c1=student("Rizwan","A-" )
print(c1.name, c1.grade)
print(student.name,student.grade)
