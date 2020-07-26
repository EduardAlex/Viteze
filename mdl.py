class UnitConversion:
	def __init__(self, sX, sXU, sTU, rXU, rTU, tC):

		self.tmunits = ["ms", "cs", "ds", "s", "min", "h"]
		self.time = [10, 10, 10, 60, 60, 0]
		self.unt = {}
		self.sXU = sXU  # Input unit for dx
		self.sTU = sTU  # Input unit for time
		self.rXU = rXU  # Result unit for dx
		self.rTU = rTU  # Result unit for time
		self.Speed = sX
		self.Result = sX
		self.sX = sX  # Input value for dx		
		with open("units\\"+tC) as f:
			a = f.readlines()
			for e, i in enumerate(a):
				a[e] = i[:-1]
			for i in a:
				b = i.split(" ")
				self.unt[b[0]] = float(b[1])
		self.convertTime()
		self.convertUnit()

	def convertTime(self):
		lR = self.listLocator(self.tmunits, self.rTU)
		lS = self.listLocator(self.tmunits, self.sTU)
		deltaU = lR - lS
		while deltaU > 0:
			self.Result *= self.time[lS]
			lS += 1
			deltaU = lR - lS
		while deltaU < 0:
			self.Result /= self.time[lS - 1]
			lS -= 1
			deltaU = lR - lS

	def convertUnit(self):
		self.Result *= self.unt[self.sXU] / self.unt[self.rXU]

	def listLocator(self, listtl, lt):
		for i, j in enumerate(listtl):
			if j == lt:
				return i
		return None
