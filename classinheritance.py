#class inheritance 

class Parent: #define parent first 
	parentAttr = 100 
	def __init__(self):
		print "Calling parent constructor"
		
	def parentMethod(self):
		print 'calling parent method'
		
	def setAttr(self, attr):
		Parent.parentAttr = attr
		
	def getAttr(self):
		print "Parent attribute: ", Parent.parentAttr
		
class Child(Parent): #define child class with parent attr?
	def __init__(self):
		print "Calling child constructor"
		
	def childMethod(self):
		print "Calling child method"
		
c = Child() #Child instance
c.childMethod() #child calls its method
c.parentMethod() #calls parents method
c.setAttr(200)  #call parents method (of set attr) 
c.getAttr()  #same thing

