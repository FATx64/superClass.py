class Hero :

	def __init__(self,name,power):
		self.name = name
		self.power = power

	def showInfo(self):
		print("{} with power : {}".format(self.name,self.power))

class Hero_ability(Hero):
	def __init__(self,name):
		super().__init__(name,300)
		super().showInfo()

Hero = Hero_ability('klee')