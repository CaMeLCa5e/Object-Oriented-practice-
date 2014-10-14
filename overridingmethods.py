#overriding methods

class Parent:
	def myMethod(self):
		print "Calling parent method"
		
class Child(Parent): #define child class
	def myMethod(self):
		print "Calling child method"
		
c = Child() # Child instance
c.myMethod() # calls overridden method- gotta put that "c" in the beginning!