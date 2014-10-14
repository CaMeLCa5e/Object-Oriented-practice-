
class Employee:
	"comon attributes"
	empCount = 0
	
	def __init__ (self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		
	def displayCount (self):
		print "Total employee %d" % Employee.empCount
		
	def displayEmployee(self):
		print "Name:", self.name, ", Salary: ", self.salary
		
		
#creating instance objects uses __init__ method

"first object"
emp1 =  Employee("Zara", 2000)

'second object'
emp2 = Employee("Manni", 5000)

#access attributes

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount


	