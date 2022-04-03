class SecurityClearance:
	def __init__(self, name, level=0):
		self.name = name
		self.level = level 
		self._clearance = {0:'0', 1:'1', 2:'2', 3:'3', 4:'All'}

	# changing what is displayed when the class is printed by overriding the __str__ dunder
	def __str__(self):
		return f"{self.name}, your clearance level is {self.__showLevel()}"

	# private method
	def __showLevel(self):
		return self._clearance.get(self.level)

class CleanDocument:

	@staticmethod
	def getSalary(salary, sec_level):
		# if the sec_level is 0, that is the same as it being false...
		# if it is false (aka 0) blank all the numbers and prepend a '$'
		sec_level=int(sec_level)
		if not sec_level: return '$' + 'X' * len(str(salary))

		# if sec_level is a 4 (all permissions) just prepend a '$' and return
		elif sec_level == 4: return '$' + str(salary)
		
		# if the sec_level is anything else, hide the appropriate number of
		#  digits starting at the front of the number, then prepend a '$'
		test = '$' + 'X' * (4-sec_level) + str(salary)[4-sec_level:]
		return test


person = SecurityClearance('Jimbo',1)
print(person)
doc = CleanDocument.getSalary(22500, person._showLevel())
print(doc)
