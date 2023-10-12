class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()

class employee():
  name="shiavni"
  company= "google"
  salary=55000
  doj="11/7/2022"
  address="uttarkhand"
  def job_des(self):
    print("my name is", self.name , "working in the company" , self.company , "as a programmer")

first_emp=employee()
second_emp=employee()
third_emp=employee()
first_emp.name="shiv"
second_emp.name="neha"
first_emp.company="colab"
second_emp.company="slides"
third_emp.company="inspector"



print(first_emp.company)
print(second_emp.company)
print(second_emp.doj)
first_emp.job_des()
third_emp.job_des()