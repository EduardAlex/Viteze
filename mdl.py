class UnitConversion:
	def __init__(self, sX, sT=1, sXU, sTU, rXU, rTU):

		self.tmunits = ["ms","cs","ds","s","min","h"]
		self.time = [10,10,10,60,60,0]
		
		self.sX  = sX  # Input value for dx
		self.sT  = sT  # Input value for time
		self.sXU = sXU # Input unit for dx
		self.sTU = sTU # Input unit for time
		self.rXU = rXU # Result unit for dx
		self.rTU = rTU # Result unit for time
		self.Speed = sU/sT
		self.Result = sU/sT

		self.convertTime()

	def convertTime(self):
		lR = self.listLocator(self.tmunits, self.rTU)
		lS = self.listLocator(self.tmunits, self.sTU)
		deltaU = lR - lS
		while deltaU > 0:
			self.Result / self.time[lS]
			lS += 1
			deltaU = lR - lS
		while deltaU < 0:
			self.Result * self.time[lS-1]
			lS -= 1
			deltaU = lR - lS

		
	def listLocator(self, listtl, lt):
		for i, j in enumerate(self.listtl):
			if j == lt:
				return i
		return None
		