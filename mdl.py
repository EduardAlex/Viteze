import os

def getUn(tC):
	with open(tC) as f:
		a = f.readlines()
		for e, i in enumerate(a):
			a[e] = i[:-1]
		for i, j in enumerate(a):
			a[i] = j.split(" ")
			a[i][2].replace("-", " ")
		return a

def listLocator(listtl, lt):
	for i, j in enumerate(listtl):
		if j == lt:
			return i
	return None

def joinall(*df):
	a = os.getcwd()
	for dorf in df:
		a = os.path.join(a,df)
	return a

class UnitConversion:
	def __init__(self, sX, sXU, sTU, rXU, rTU, tC):

		self.time = {}
		self.unt = {}
		self.sX = sX  # Input value for dx
		self.sXU = sXU  # Input unit for dx
		self.sTU = sTU  # Input unit for time
		self.rXU = rXU  # Result unit for dx
		self.rTU = rTU  # Result unit for time
		self.Speed = sX
		self.Result = sX
		# with open("units\\" + tC) as f:
		#     a = f.readlines()
		#     for e, i in enumerate(a):
		#         a[e] = i[:-1]
		#     for i in a:
		#         b = i.split(" ")
		#         self.unt[b[0]] = float(b[1])
		h = getUn(joinall("units", tC))
		for i in h:
			self.unt[i[0]] = float(i[1])

		# with open("time") as f:
		#     a = f.readlines()
		#     for e, i in enumerate(a):
		#         a[e] = i[:-1]
		#     for i in a:
		#         b = i.split(" ")
		#         self.time[b[0]] = float(b[1])
		h = getUn(joinall("time"))
		for i in h:
			self.time[i[0]] = float(i[1])

		self.convertTime()
		self.convertUnit()

	def convertTime(self):
		self.Result /= self.time[self.sTU] / self.time[self.rTU]

	def convertUnit(self):
		self.Result *= self.unt[self.sXU] / self.unt[self.rXU]

