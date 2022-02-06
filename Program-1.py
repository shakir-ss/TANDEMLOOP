'''
Problem-1: Create a small calculator which performs operations 
such as Addition, Subtraction, Multiplication and Division using class.

Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’

Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string '''

class Calculator():
    def __init__(self,a,b,operation):
        self.a = a
        self.b = b
        self.operation = operation
    
    def calculate(self):
        if  self.operation == "+":
            print(self.a + self.b) 

        if self.operation == "-":
            print(self.a - self.b)

        if self.operation == "*":
            print(self.a * self.b)

        if self.operation == "/":
            print(self.a / self.b)



obj=Calculator(20,10,"+")   #OUTPUT = 30 , BY CHANGING THE OPERATION WE CAN CALCULATE ACCORDINGLY

obj.calculate()

Calculator(20,2,"*").calculate() #OUTPUT = 40   #WE CAN ALSO CALL THE calculate funtion like this
