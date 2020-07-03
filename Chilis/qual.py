import os, sys, math
import copy, random
import pygame
import pygame.surfarray as surfarray
import pygame.draw as draw
import numpy as N

from pygame.locals import *

global mainFont


currFrameNum = 0


def InitGfx():
	pygame.init()

	screen = pygame.display.set_mode((1024, 768))
	pygame.display.set_caption('Daniel Wilhelm :: Qual Exam - Stage Two')
	pygame.mouse.set_visible(0)

	backbuf = pygame.Surface(screen.get_size())
	backbuf = backbuf.convert()
	backbuf.set_clip(None)
	backbuf.fill((0, 0, 0))
	
	return [screen, backbuf]


def GenStatic(filename):
	backstatic = pygame.Surface(screen.get_size())
	staticarray = N.zeros((1024, 768, 3))

	for i in range(0,1024):
		for j in range(0,768):
			a = random.randint(0, 255)
			staticarray[i,j] = (a,a,a)

	surfarray.blit_array(backstatic, staticarray)

	pygame.image.save(backstatic, filename)


class PrintLine:

	def __init__(self, rows, cols):
		self.toWrite = list()
		self.toImage = list()
		
		self.startx = 50
		self.starty = 50
		self.size = 30
		
		self.fontsize = 40
		self.fonty = self.fontsize + 5
			
		self.nextReady = False
		self.currRow = 0
		self.cursorTick = 0
		
		self.isRenderDone = False
	
	
	def Clear(self):
	
		self.currRow = 0
		self.toWrite = list()
		self.toImage = list()
	
	
	def IsRenderDone(self):
		return self.isRenderDone
	
	
	def Append(self, text, center = False, mouseReq = False, isVisible = False):

		start = -1
		if (isVisible == True):
			start = len(text)
		
		self.toWrite.append([self.currRow, text, start, center, mouseReq])
		self.currRow += 1
	
	
	def Write(self, row, text, center = False, mouseReq = False, isVisible = False):
		for r in self.toWrite:
			if (r[0] == row):
				self.toWrite.remove(r)
				break
		
		start = -1
		if (isVisible == True):
			start = len(text)

		self.toWrite.append([self.currRow, text, start, center, mouseReq])
	
	
	def AppendImage(self, filename, x,y, center):
		
		image = pygame.image.load(filename)
		
		if (center == True):
			width = image.get_size()[0]
			self.toImage.append([image, 1024/2 - width/2,y])
		else:
			self.toImage.append([image, x,y])
		
	
	def Render(self, surface, frameNum = 0):
		lastRow = None
		
		# Render frame number
		if (frameNum > 0):
			strFrameNum = bigFont.render(str(frameNum), True, (200, 200, 200))
			surface.blit(strFrameNum, (960,720))
		
		for img in self.toImage:
			surface.blit(img[0], (img[1],img[2]))
		
		self.isRenderDone = True
		for row in self.toWrite:
			if (row[2] == -1):
				self.isRenderDone = False
				if (lastRow == None):
					row[2] = 0
				else:
					
					if (lastRow[2] >= len(lastRow[1]) - 1):
						row[2] = 0
					else:
						break
			
			if (row[2] < len(row[1]) + 1):
				text = bigFont.render(row[1][:row[2]], True, (200, 200, 200))
				row[2] += 1
				
				startCursor = (self.startx + row[2]*13, self.starty + row[0]*self.fonty + 15)
				endCursor   = (startCursor[0] + 10, startCursor[1])
				#draw.line(surface, (255,255,255), startCursor, endCursor, 5)
			else:
				text = bigFont.render(row[1], True, (200, 200, 200))
			
			textx = self.startx
			if (row[3] == True):
				textwidth = text.get_size()[0]
				textx = 1024 / 2 - textwidth / 2
			
			surface.blit(text, (textx, self.starty + row[0] * self.fonty))
			
			lastRow = row

		# Draw static cursor
		if (lastRow != None):
			if (self.cursorTick < 20):
				if (self.cursorTick > 10):
					if (lastRow[3] == False):
						startCursor = (self.startx, self.starty + lastRow[0]*self.fonty + self.fonty)
					else:
						startCursor = (1024/2 - 5, self.starty + lastRow[0]*self.fonty + self.fonty)
					
					endCursor   = (startCursor[0] + 10, startCursor[1])
					draw.line(surface, (255,255,255), startCursor, endCursor, 10)
				
				self.cursorTick += 1
			else:
				self.cursorTick = 0


# x,y is the CENTER of the pswitch
def DrawPSwitch(surface, x,y, width, text = '', isDet = False):
	
	color = (255,255,255)
	if (isDet == False):
		color = (200, 200, 200)
	
	half = width/2
	draw.aaline(surface, color, (x-half,y-half), (x+half,y+half))
	draw.aaline(surface, color, (x+half,y-half), (x-half,y+half))

	extra = 0
	if (isDet == False):
		draw.circle(surface, color, (x,y), width, 2)
		extra = 5
	
	if (text != ''):
		strLabel = mainFont.render(str(text), True, (200, 200, 200))
		surface.blit(strLabel, (x+2*width/3 + extra,y+2*width/3 + extra))
	




# (x,y) are the terminal start
def DrawCircuit(surface, sspString, x,y, width,height, lastSeries = 0, lastParallel = 0):

	#draw.aaline(surface, (255,0,0), (x,0), (x, 768))
	#draw.aaline(surface, (255,0,0), (0,y), (1024, y))
	
	swSize = 20

	isDet = False
	if (sspString[0] == '~'):
		isDet = True
		sspString = sspString[1:]
	
	text = ''
	while (sspString[0] != 's' and sspString[0] != 'p'):
		text += sspString[0]
		sspString = sspString[1:]

	# Count the num parallel in a row
	if (lastParallel == 0):
		np = 0
		for index,c in enumerate(sspString):
			if (c == 'p' or index == len(sspString) - 1):
				np += 1
			elif (c == 's'):
				break
		
		if (np > 1):
			if (index < len(sspString) - 1):
				lastParallel = (2*height/3) / (np+1)
			else:
				lastParallel = height / (np+1)
	
	# Count the num series in a row
	if (lastSeries == 0):
		ns = 0
		for index,c in enumerate(sspString):
			if (c == 's' or index == len(sspString) - 1):
				ns += 1
			elif (c == 'p'):
				break
		
		if (ns > 1):
			if (index < len(sspString) - 1):
				lastSeries = (2*width/3) / ns
			else:
				lastSeries = width / ns

	isLastParallel = False
	if (lastSeries == 0):
		isLastParallel = True
		lastSeries = width / 5

	
	if (lastParallel == 0):
		lastParallel = height / 5
	
	# Base case -- one pswitch
	if (len(sspString) <= 1):
		draw.aaline(surface, (255,255,255), (x,y), (x+width, y))
		DrawPSwitch(surface, x + width / 2, y, swSize, text, isDet)
		return
	
	
	if (sspString[0] == 's'):
		newx = x+lastSeries
		# new pswitch wire
		draw.aaline(surface, (255,255,255), (x,y), (newx, y))
		
		DrawPSwitch(surface, x + lastSeries / 2, y, swSize, text, isDet)
		DrawCircuit(surface, sspString[1:], newx,y, width - lastSeries,height, lastSeries, 0)
	else:		
		thirdh = lastParallel
		firstx = x
		lastx = x + width
		newwidth = width
		
		endy = y+lastParallel
		
		if (len(sspString) == 2):
			# Two parallel pswitches after a series, special case
			if (lastSeries != width/5):
				#draw.aaline(surface, (255,0,0), (x,y), (0,0))
				thirdh = lastParallel/2
				endy = y + lastParallel/2
			else:
				endy = y

		
		draw.aaline(surface, (255,255,255), (firstx,y-thirdh), (firstx, endy)) #Left Up/Down
		draw.aaline(surface, (255,255,255), (lastx,y-thirdh), (lastx, endy)) #Rt Up/Down
		
		draw.aaline(surface, (255,255,255), (firstx,y-thirdh), (lastx, y-thirdh)) #Top pswitch		
		DrawPSwitch(surface, x + width/2, y-thirdh, swSize, text, isDet)
		
		DrawCircuit(surface, sspString[1:], firstx,endy, newwidth, 2*height/3, 0 , lastParallel)
	

def DrawCircuitDS(surface, sspString, r,c, ds, text=None):
	DrawCircuit(surface, sspString, ds.GetUL(r,c)[0],ds.GetCenter(r,c)[1], ds.GetWidth(),ds.GetHeight())
	
	if (text != None):
		strText = bigFont.render(str(text), True, (200, 200, 200))
		
		centerx = ds.GetCenter(r,c)[0] - strText.get_size()[0]/2
		centery = ds.GetUL(r,c)[1] - 25
		surface.blit(strText, (centerx, centery))


class FrameManager:
	def __init__(self):
		self.currIndex = -1
		self.maxFrameNum = -1
		self.Frames = list()
	
	
	def NewFrame(self):
		self.maxFrameNum = self.maxFrameNum + 1
	
		# If not, create a new frame
		self.Frames.append([self.maxFrameNum, PrintLine(40,20), None])
		self.currIndex = len(self.Frames) - 1
		return self.Frames[len(self.Frames) - 1][1]
	
	def LoadFrame(self, frameNum = None):
	
		if (frameNum != None):
			# Is the frame already in memory?
			for index,frame in enumerate(self.Frames):
				if (frame[0] == frameNum):
					self.currIndex = index
					return self.Frames[index][1]
		
		# If not, create a new frame
		self.currIndex = len(self.Frames) - 1
		return self.NewFrame()
		
		#self.Frames.append([frameNum, PrintLine(40,20), None])
		#self.currIndex = len(self.Frames) - 1
		#return self.Frames[len(self.Frames) - 1][1]
		
	
	def SaveFrame(self, newFrame, func = None, frameNum = None):
		if (frameNum == None):
			frameNum = self.currIndex
		
		for index,frame in enumerate(self.Frames):
			if (frame[0] == frameNum):
				self.Frames[index][1] = newFrame
				self.Frames[index][2] = func

	
	def CurrFrame(self):
		return self.Frames[self.currIndex][1]
	
	
	def Render(self, surface):
		self.Frames[self.currIndex][1].Render(surface, self.Frames[self.currIndex][0])
		
		if (self.Frames[self.currIndex][2] != None):
			self.Frames[self.currIndex][2](surface)
	
	

class DivScreen:
	def __init__(self, rows, cols, outborder = 0, inborder = 0):
		self.rows = rows
		self.cols = cols
		self.outborder = outborder
		self.inborder = inborder
		self.cellwidth = (1024 - outborder*2) / cols
		self.cellheight = (768 - outborder*2) / rows
		self.width = self.cellwidth - inborder*2
		self.height = self.cellheight - inborder*2
	
	def GetUL(self, r, c):
		totalBorder = self.outborder + self.inborder
		return [totalBorder + c * self.cellwidth, totalBorder + r * self.cellheight]
	
	def GetCenter(self, r, c):
		totalBorder = self.outborder + self.inborder
		return [totalBorder + self.cellwidth * c + self.width/2, totalBorder + self.cellheight * r + self.height/2]
	
	def GetWidth(self):
		return self.width
	
	def GetHeight(self):
		return self.height



def DrawPrCircuit(surface, a, nswitches, x,y, ds, showStr = True):
	
	# Convert to binary
	binaryStr = ''
	curra = a
	currsw = nswitches
	while (currsw > 0):
		binaryStr = str(curra % 2) + binaryStr
		curra = int(curra / 2)
		currsw -= 1
	
	# Convert to ssp string
	sspStr = ''
	for index,c in enumerate(binaryStr):
		if (c == '0' or index == len(binaryStr) - 1):
			sspStr += str(nswitches - index) + 's'
		else:
			sspStr += str(nswitches - index) + 'p'
	
	if (showStr):
		binaryStr = str(a) + '/' + str(int(math.pow(2, nswitches))) + ' = ' + '0.' + binaryStr
	else:
		binaryStr = ''
	
	DrawCircuitDS(surface, sspStr, x,y, ds, binaryStr)
	




# Title Screen
ticks0 = 0
curr_a00 = 0
curr_a10 = 0
curr_a20 = 0
curr_a30 = 0

def Init0(fm):
	frame = fm.NewFrame()
	
	frame.Append('"Stochastic Switching Circuit Synthesis"', True)
	#frame.Append('daniel wilhelm', True)
	
	fm.SaveFrame(frame, Render0)



def Render0(surface):
	global ticks0
	global curr_a00
	global curr_a10
	global curr_a20
	global curr_a30
	
	ds = DivScreen(2,2, 50, 50)
	
	if (ticks0 >= 5):
		ticks0 = 0
		curr_a00 = random.randint(0,128)
		curr_a10 = random.randint(0,128)
		curr_a20 = random.randint(0,128)
		curr_a30 = random.randint(0,128)
	else:
		ticks0 += 1
	
	DrawPrCircuit(surface, curr_a00, 7, 0,0, ds, False)
	DrawPrCircuit(surface, curr_a10, 7, 0,1, ds, False)
	DrawPrCircuit(surface, curr_a20, 7, 1,0, ds, False)
	DrawPrCircuit(surface, curr_a30, 7, 1,1, ds, False)


# Special Thanks
def InitIntro(fm):
	frame = fm.NewFrame()
	for i in range(0,4):	frame.Append('')

	frame.Append('Stochastic Switching Circuit Synthesis', True)
	frame.Append('')
	frame.Append('Daniel Wilhelm', True)
	frame.Append('ADVISOR: Prof. Jehoshua Bruck', True)
	frame.Append('')
	frame.Append('')
	frame.Append('CNS Qualifying Exam', True)
	frame.Append('December 15, 2008', True)

	fm.SaveFrame(frame)


# Accomplishments
def InitAccomp1(fm):
	frame = fm.NewFrame()
	frame.Append('CNS Accomplishments', True)
	frame.Append('+ Completed three rotations & summer in bioinformatics')
	frame.Append('+ Completed coursework requirements')
	frame.Append('+ ISIT 2008 presentation: "Stochastic Switching Circuit Synthesis"')
	frame.Append('+ Submission to IEEE Transactions on IT forthcoming')
	frame.Append('+ IST 4 Head TA, Spring 2008')
	frame.Append('+ Two NESS Talks, CNS Journal Club presentation')
	
	frame.AppendImage('paper_title.png', 0,425, True)
	
	fm.SaveFrame(frame)
	

# Outline
def InitOutline(fm):
	frame = fm.NewFrame()
	frame.Append("Chapters", True)
	frame.Append('')
	frame.Append('I. A bit of background: genteel discourse')
	frame.Append('II. The B-algorithm: toward an A')
	frame.Append('III. Duality: to the death')
	frame.Append("IV. The Universal Probability Generator: UPGs and You")
	frame.Append('V. Future directions: reflections')
	frame.Append('(X. Better vibrations through representations)')

	#frame.AppendImage('paper_title.png', 0,350, True)

	fm.SaveFrame(frame)


def InitPartI(fm):
	frame = fm.NewFrame()
	for i in range(0, 7): frame.Append('')
	frame.Append('I. A bit of background: genteel discourse', True)

	fm.SaveFrame(frame)

def InitPartII(fm):
	frame = fm.NewFrame()
	for i in range(0, 7): frame.Append('')
	frame.Append('II. The B-algorithm: toward an A', True)

	fm.SaveFrame(frame)

def InitPartIII(fm):
	frame = fm.NewFrame()
	for i in range(0, 7): frame.Append('')
	frame.Append('III. Duality: to the death', True)

	fm.SaveFrame(frame)

def InitPartIV(fm):
	frame = fm.NewFrame()
	for i in range(0, 7): frame.Append('')
	frame.Append("IV. The Universal Probability Generator: UPGs and You", True)

	fm.SaveFrame(frame)

def InitPartV(fm):
	frame = fm.NewFrame()
	for i in range(0, 7): frame.Append('')
	frame.Append('V. Future directions: reflections', True)

	fm.SaveFrame(frame)

def InitPartX(fm):
	frame = fm.NewFrame()
	for i in range(0, 7): frame.Append('')
	frame.Append('X. Better vibrations through representations', True)

	fm.SaveFrame(frame)

def InitQuestions(fm):
	frame = fm.NewFrame()
	for i in range(0, 7): frame.Append('')
	frame.Append('Q. Questions?', True)

	fm.SaveFrame(frame)



def InitPaperDates(fm):
	frame = fm.NewFrame()
	frame.Append("References", True)
	frame.Append('1847.', True)
	frame.Append('1892.', True)
	frame.Append('1919.', True)
	frame.Append('1934.', True)
	frame.Append('1938.', True)
	frame.Append('1940.', True)
	frame.Append('1942.', True)
	frame.Append('1961.', True)
	frame.Append('1963.', True)
	frame.Append('1965.', True)
	frame.Append('1971.', True)
	frame.Append('1987.', True)
	frame.Append('1998.', True)
	frame.Append('2006.', True)

	fm.SaveFrame(frame)


def InitPaperDates2(fm):
	frame = fm.NewFrame()
	frame.Append("References", True)
	frame.Append('1847. Boole.')
	frame.Append('1892. Macmahon.')
	frame.Append('1919. Ramanujan.')
	frame.Append('1934. Erdos (sic).')
	frame.Append('1938. Shannon.')
	frame.Append('1940. Tellegen.')
	frame.Append('1942. Riordan and Shannon.')
	frame.Append('1961. Whitesitt.')
	frame.Append('1963. Gill.')
	frame.Append('1965. Duffin.')
	frame.Append('1971. Lechner.')
	frame.Append('1987. Colbourn.')
	frame.Append('1998. Meinel.')
	frame.Append('2006. Heling-Tveretina and Provan.')

	fm.SaveFrame(frame)



# Associate vars w/ switches
def InitSwitches(fm):
	frame = fm.NewFrame()
	frame.Append("Deterministic Switches", True)
	frame.Append('')
	frame.Append('+ Every switch is either closed or open.')
	frame.Append('+ Boole showed a mapping between logic and physics (1847).')
	frame.Append('+ A Boolean variable is implicitly associated with each switch.')

	fm.SaveFrame(frame, RenderSwitches)
	
def RenderSwitches(s):
	ds = DivScreen(2,2, 50, 15)
	
	DrawCircuitDS(s, '~B={0,1}s', 1,0, ds, 'deterministic switch')
	DrawCircuitDS(s, '~Bs~As', 1,1, ds, '(A AND B)')

# Associate vars w/ switches
def InitSwitches2(fm):
	frame = fm.NewFrame()
	frame.Append("Probabilistic Switches", True)
	frame.Append('')
	frame.Append('+ Here, we associate random variables with switches.')
	frame.Append('+ We define these as *pswitches* -- probabilistic switches.')
	frame.Append('+ In this presentation, we use Bernoulli random variables.')

	fm.SaveFrame(frame, RenderSwitches2)


def RenderSwitches2(s):
	ds = DivScreen(2,2, 50, 15)
	
	DrawCircuitDS(s, '~B={0,1}s', 1,0, ds, 'deterministic switch')
	DrawCircuitDS(s, 'x=[0,1]s', 1,1, ds, 'probabilistic switch (pswitch)')
	

# Series and parallel
def InitSeriesParallel(fm):
	frame = fm.NewFrame()
	frame.Append("Series and Parallel", True)
	frame.Append('')
	frame.Append('Pr (pswitch) = x')
	
	for i in range(0,4):	frame.Append('')
	frame.Append('Pr (series) = xy')
	
	for i in range(0,3):	frame.Append('')
	frame.Append('Pr (parallel) ')
	frame.Append('  = 1 - (1-x)(1-y)')
	frame.Append('  = x+y-xy')


	fm.SaveFrame(frame, RenderSeriesParallel)
	
def RenderSeriesParallel(s):
	ds = DivScreen(3,2, 50, 15)
	
	DrawCircuitDS(s, 'xs', 0,1, ds)
	DrawCircuitDS(s, 'xsys', 1,1, ds)
	DrawCircuitDS(s, 'xpys', 2,1, ds)


# Compose switches to form circuits
def InitSPCircuits(fm):
	frame = fm.NewFrame()
	frame.Append("Series-Parallel Circuits", True)
	frame.Append('')
	frame.Append('+ We compose switches to form circuits.')
	frame.Append('+ A circuit is Series-Parallel (sp) iff it is:')
	frame.Append('   (1) A single switch, or')
	frame.Append('   (2) A series or parallel composition of two sp circuits.')

	fm.SaveFrame(frame, RenderSPCircuits)
	
def RenderSPCircuits(s):
	ds = DivScreen(2,3, 50, 15)
	
	DrawCircuitDS(s, '~s', 1,0, ds)
	DrawCircuitDS(s, '~p~p~s~p~s', 1,1, ds)

	w = ds.GetWidth()
	h = ds.GetHeight()
	DrawCircuit(s, '~p~s', ds.GetUL(1,2)[0],ds.GetCenter(1,2)[1], w/2,h)
	DrawCircuit(s, '~p~s', ds.GetUL(1,2)[0] + w/2,ds.GetCenter(1,2)[1], w/2,h)



# Is bridge circuit series-parallel?
def InitBridgeSP(fm):
	frame = fm.NewFrame()
	frame.Append("Is this bridge circuit sp?", True)

	for i in range(0,12):	frame.Append('')
	frame.Append("Duffin showed that ALL non-sp circuits", True)
	frame.Append("contain a Wheatstone bridge (1965).", True)

	fm.SaveFrame(frame, RenderBridgeSP)


def RenderBridgeSP(surface):
	ds = DivScreen(1,1, 50, 25)
	w = ds.GetWidth()
	h = ds.GetHeight()
	
	DrawCircuit(surface, '~p~s', ds.GetUL(0,0)[0],ds.GetCenter(0,0)[1], w/2,h)
	DrawCircuit(surface, '~p~s', ds.GetUL(0,0)[0] + w/2,ds.GetCenter(0,0)[1], w/2,h)
	DrawPSwitch(surface, 1024/2,768/2, 20, '(the bridge!)', True)


def InitBAlgo(fm):
	frame = fm.NewFrame()
	frame.Append("The B-Algorithm", True)
	frame.Append('')
	frame.Append('1) Begin with a single pswitch. (pswitch #1 below)')
	frame.Append('2) From the ith least-sig. bit of the n-bit binary frac. (i = 2 to n):')
	frame.Append("    a) If '1', add a pswitch in parallel.")
	frame.Append("    b) If '0', add a pswitch in series.")
	
	fm.SaveFrame(frame, RenderBAlgo)


def RenderBAlgo(surface):
	ds = DivScreen(2,2, 50, 25)
	
	DrawPrCircuit(surface, 37,7, 1,0, ds)
	DrawPrCircuit(surface, 121,8, 1,1, ds)


# Series and parallel
def InitSeriesParallelBPf(fm):
	frame = fm.NewFrame()
	frame.Append("Proof of B-Algorithm", True)
	frame.Append('')
	frame.Append('Pr (pswitch) = Pr(C)')
	
	for i in range(0,4):	frame.Append('')
	frame.Append('Pr (series) = Pr(C)/2')
	frame.Append('  (right shift w/o replacement)')
	
	for i in range(0,2):	frame.Append('')
	frame.Append('Pr (parallel) ')
	frame.Append('  = 1/2 + Pr(C) - Pr(C)/2')
	frame.Append('  = 1/2 + Pr(C)/2')
	frame.Append('  (right shift w/ replacement)')


	fm.SaveFrame(frame, RenderSeriesParallelBPf)
	
def RenderSeriesParallelBPf(s):
	ds = DivScreen(3,2, 50, 15)
	
	DrawCircuitDS(s, 'Pr(C)s', 0,1, ds)
	DrawCircuitDS(s, '1/2sPr(C)s', 1,1, ds)
	DrawCircuitDS(s, '1/2pPr(C)s', 2,1, ds)
	

def InitBAlgoOptimal(fm):
	frame = fm.NewFrame()
	frame.Append("Shocking News", True)
	frame.Append('')
	frame.Append('Theorem. The B-Algorithm is optimal in terms of pswitches.')
	frame.Append('   + i.e. NO switching circuit exists -- sp or non-sp -- ')
	frame.Append('     which realizes the fraction using fewer pswitches.')
	frame.Append('')
	frame.Append('')
	frame.Append('')
	frame.Append('Fun Fact: With all pswitches closed with probability 1/2, the', True)
	frame.Append('    Wheatstone bridge is closed with probability 1/2.', True)
	
	fm.SaveFrame(frame)


def InitProofTech(fm):
	frame = fm.NewFrame()
	frame.Append("Toward a Proof Technique", True)
	frame.Append('')
	frame.Append("By adding an pswitch 'x' to ANY ")
	frame.Append("  stochastic switching circuit M to form M':")
	frame.Append('')
	frame.Append("Pr(M') = xC + (1-x)O,", True)
	frame.Append('')
	frame.Append("C = Pr(M'|x closed)", True)
	frame.Append("O = Pr(M'|x open)", True)
	frame.Append('')
	frame.Append('')
	frame.Append('(From basic probability. Either one or the other occurs.)', True)
	
	fm.SaveFrame(frame)

def InitProofExample(fm):
	frame = fm.NewFrame()
	frame.Append("An Example.", True)
	frame.Append('')
	frame.Append("Suppose we are forming the middle circuit M' below.", True)
	frame.Append('')
	frame.Append("Then, Pr(M') = xC + (1-x)O = 5/16 + 3/8 = 11/16.", True)
	frame.Append('(This can be verified via the B-algorithm.)', True)
	
	fm.SaveFrame(frame, RenderProofExample)


def RenderProofExample(s):
	ds = DivScreen(2,3, 50, 15)
	
	DrawCircuitDS(s, 'pss', 1,0, ds, "O = Pr(M'|x open) = 5/8")
	DrawCircuitDS(s, 'psxps', 1,1, ds, "M'")
	DrawCircuitDS(s, 'ps', 1,2, ds, "C = Pr(M'|x closed) = 3/4")


def InitProofExample2(fm):
	frame = fm.NewFrame()
	frame.Append("Proof of B-algorithm Optimality.", True)
	frame.Append('')
	frame.Append('+ Suppose circuit M_i s.t. Pr(M_i) is an i-bit fraction.')
	frame.Append('+ Main Idea: Contradiction.')
	frame.Append('   + Take away one pswitch at a time using previous formula.')
	frame.Append('   + Show that this results in a >= (i-1)-bit fraction.')
	frame.Append('   + Apply (n-1) times, and contradiction.')
	fm.SaveFrame(frame)


def InitProofExample3(fm):
	frame = fm.NewFrame()
	frame.Append('Proof of B-algorithm Optimality.', True)
	frame.Append('')
	frame.Append("Pr(M_i) = xC + (1-x)O = a/2^i, for some a.", True)
	frame.Append("So, a/2^{i-1} = C + O.", True)
	frame.Append('')
	frame.Append('Example. Pr(M_4) = 3/16 = C/2 + O/2 ')
	frame.Append('                            --->  3/8 = C + O.')
	frame.Append('')
	frame.Append('a must be odd since in lowest terms.', True)
	frame.Append('Hence, either C or O is at least i-1 bits long.', True)
	frame.Append('Also has a non-zero least-sig bit.', True)
	frame.Append('')
	frame.Append('Example. 3/8 = 1/4 + *1/8*.')
	frame.Append('')
	frame.Append('Contradiction if apply (n-1) times.', True)
	
	fm.SaveFrame(frame)


def InitDuality(fm):
	frame = fm.NewFrame()
	frame.Append("Duality", True)
	frame.Append("(a) De Morgan's Law", True)
	frame.Append("(b) Macmahon's resistances      (c) Our stochastic switching circuits", True)

	frame.AppendImage('duality.png', 0,200, True)

	fm.SaveFrame(frame)

def InitDualExamples(fm):
	frame = fm.NewFrame()
	frame.Append("Duality Examples", True)

	fm.SaveFrame(frame, RenderDualExamples)

def RenderDualExamples(s):
	ds = DivScreen(2,3, 50, 15)
	
	DrawCircuitDS(s, '2/3s1/4s', 0,0, ds)
	DrawCircuitDS(s, '1/3p3/4s', 1,0, ds)
	DrawCircuitDS(s, '1/2p3/8s1/2p2/3s', 0,1, ds)
	DrawCircuitDS(s, '1/2s5/8p1/2s1/3s', 1,1, ds)
	DrawCircuitDS(s, '1/2p1/2p1/2s1/2s', 0,2, ds)
	DrawCircuitDS(s, '1/2s1/2s1/2p1/2s', 1,2, ds)


def InitDualTheorem(fm):
	frame = fm.NewFrame()
	frame.Append("Duality Theorem", True)
	
	frame.Append('')
	frame.Append('Theorem. Given sp circuit C and its dual C*, Pr(C) + Pr(C*) = 1')
	frame.Append('Proof. Induction on definition of sp.')

	fm.SaveFrame(frame, RenderDualTheorem)


def RenderDualTheorem(s):
	ds = DivScreen(3,2, 50, 15)
	
	DrawPrCircuit(s, 35,6, 1,0, ds)
	DrawPrCircuit(s, 29,6, 2,0, ds)
	DrawPrCircuit(s, 11,4, 1,1, ds)
	DrawPrCircuit(s, 5,4, 2,1, ds)


def InitDualTheorem2(fm):
	frame = fm.NewFrame()
	frame.Append("Can we generate all binary fractions?", True)
	frame.Append('')
	frame.Append('1) Base: Can generate 1/2 with one pswitch.')
	frame.Append('2) Inductive: Given all n-bit fractions,')
	frame.Append('    a) Add a 1/2 in series with each to gen. lower half.')
	frame.Append('    b) The dual of these gen. the upper half.')
	frame.Append('    c) Hence, can generate all (n+1)-bit fractions.')

	frame.AppendImage('duality_half.png', 0,500, True)

	fm.SaveFrame(frame)


def InitDualTheorem3(fm):
	frame = fm.NewFrame()
	frame.Append("Can we generate all trinary fractions?", True)
	frame.Append('')
	frame.Append('1) Base: Can generate 1/3,2/3 with one pswitch.')
	frame.Append('2) Inductive: Given all n-trit fractions,')
	frame.Append('    a) Add a 1/3 in series with each. (Dual gen. upper-third.)')
	frame.Append('    b) Add a 2/3 in series with each. (Gen. all evens in middle.)')
	frame.Append('    c) The dual of (b) gen. all odds in middle.')
	frame.Append('    d) Hence, can generate all (n+1)-trit fractions.')
	frame.Append('')
	frame.Append('This is optimal.', True)
	

	frame.AppendImage('duality_third.png', 0,500, True)

	fm.SaveFrame(frame)


def InitDualTheorem3b(fm):
	frame = fm.NewFrame()
	frame.Append("Example - Trinary Fractions", True)
	frame.Append('')
	frame.Append('We are given 1/3, 2/3.')
	frame.Append(' Lower Third   ...   Upper Third')
	frame.Append('1/3 x 1/3 = 1/9 ... dual = 8/9')
	frame.Append('2/3 x 1/3 = 2/9 ... dual = 7/9')
	frame.Append('')
	frame.Append('Middle Evens  ...   Middle Odds')
	frame.Append('2/3 x 2/3 = 4/9 ... dual = 5/9')

	frame.AppendImage('duality_third.png', 0,500, True)

	fm.SaveFrame(frame)


def InitBertrand(fm):
	frame = fm.NewFrame()
	frame.Append("Can this trend continue?", True)
	frame.Append('')
	frame.Append('Theorem. Given all rationals with denominator q (s.t. q > 3), there')
	frame.Append('       exist rational probabilities a/q^2 which cannot be realized')
	frame.Append('       by any two-pswitch circuit.')
	frame.Append('')
	frame.Append('Proof. In parallel: Smallest odd realizable is by 1/q||1/q = (2q-1)/q^2.')
	frame.Append('In series: Can only realize composites larger than q/q^2.')
	frame.Append('')
	frame.Append("Hence, we cannot realize any prime 'a' in q < a <= 2q-2")
	frame.Append("By Bertrand's Postulate, a prime is guaranteed to exist.")

	fm.SaveFrame(frame)


def InitDualTheorem4(fm):
	frame = fm.NewFrame()
	frame.Append("What about all 4-ary fractions?", True)
	frame.Append('')
	frame.Append('+ A similar approach yields all evens but no middle odds.')
	frame.Append('+ Hence, can only do it with at most 2n pswitches.')
	frame.Append("   + Want an odd 'o'? o/4^n = (2o)/4^n x 1/2.")

	frame.AppendImage('duality_fourth.png', 0,450, True)

	fm.SaveFrame(frame)


def InitUPG1(fm):
	frame = fm.NewFrame()
	frame.Append("UPG Construction", True)
	frame.Append('')
	frame.Append('+ A Universal Probability Generator maps n deterministic input bits')
	frame.Append('    to all 2^n n-bit binary fractions, in increasing order.')
	frame.Append('+ Can easily construct using an exponential number of switches.')
	frame.Append('+ Here, we show how to do it using 4n - 2.')

	frame.AppendImage('upg1.png', 0,400, True)

	fm.SaveFrame(frame)


def InitUPG2(fm):
	frame = fm.NewFrame()
	frame.Append("UPG Construction: Explained", True)

	frame.AppendImage('upg2.png', 0,200, True)

	fm.SaveFrame(frame)


def InitUPG3(fm):
	frame = fm.NewFrame()
	frame.Append("UPG Construction: Example", True)

	frame.AppendImage('upg1.png', 0, 100, True)

	frame.AppendImage('upg3.png', 0,400, True)

	fm.SaveFrame(frame)


def InitFuture1(fm):
	frame = fm.NewFrame()
	frame.Append("Possible Extensions of the Work", True)

	frame.Append('')
	frame.Append('+ Non-Bernoulli rvs')
	frame.Append('+ Further explore SSP/SP/non-SP spaces')
	frame.Append('+ Optimal algorithms for more non-complete pswitch sets')
	frame.Append('+ Tolerance to error (Po-Ling)')
	frame.Append('+ Tighten bounds on current algorithms')

	fm.SaveFrame(frame)


def InitFuture2(fm):
	frame = fm.NewFrame()
	frame.Append("Applications of the Work", True)

	frame.Append('')
	frame.Append('+ Modeling:')
	frame.Append('   + Probability of neuron firing dependent on input noise')
	frame.Append('   + Given experimental measurements, infer the network')
	frame.Append('   + Neural spiking prediction')
	frame.Append('   + Chemical reaction networks')
	frame.Append('')
	frame.Append('+ System reliability')
	frame.Append('')
	frame.Append('NOTE: Many applications may require non-Bernoulli rvs', True)
	frame.Append('Recall that pswitches, rvs can represent capacity or rate', True)

	fm.SaveFrame(frame)


def InitFuture3(fm):
	frame = fm.NewFrame()
	frame.Append("Additional directions", True)

	frame.Append('')
	frame.Append('+ Implement other CS structures efficiently/novelly?')
	frame.Append('   + Probabilistic Markov Chains/State Machines')
	frame.Append('   + Bayesian Networks')
	frame.Append('')
	frame.Append('+ Probabilistic Learning Systems')

	fm.SaveFrame(frame)


def InitBDD(fm):
	frame = fm.NewFrame()
	frame.Append('Representations and the B-Algorithm.', True)
	
	frame.AppendImage('bdd.png', 0,150, True)
	fm.SaveFrame(frame)


[screen, backbuf] = InitGfx()

mainFont = pygame.font.Font(None, 25)
bigFont = pygame.font.Font(None, 40)

fm = FrameManager()

clock = pygame.time.Clock()

# Create a font

pygame.display.update()

screen.blit(backbuf, (0, 0))
pygame.display.flip()

backstatic = list()

backstatic.append(pygame.image.load('static1.jpeg'))
backstatic.append(pygame.image.load('static2.jpeg'))
backstatic.append(pygame.image.load('static3.jpeg'))

# I. INTRODUCTION
Init0(fm)
InitIntro(fm)
InitAccomp1(fm)

InitPaperDates(fm)
InitPaperDates2(fm)

# I. BACKGROUND
InitPartI(fm)
InitSwitches(fm)
InitSwitches2(fm)
InitSeriesParallel(fm)
InitSPCircuits(fm)
InitBridgeSP(fm)


InitOutline(fm)

# II. B-Algorithm
InitPartII(fm)
InitBAlgo(fm)
InitSeriesParallelBPf(fm)
InitBAlgoOptimal(fm)
InitProofTech(fm)
InitProofExample(fm)
InitProofExample2(fm)
InitProofExample3(fm)
InitBDD(fm)

# III. Duality
InitPartIII(fm)
InitDuality(fm)
InitDualExamples(fm)
InitDualTheorem(fm)
InitDualTheorem2(fm)
InitDualTheorem3(fm)
InitDualTheorem3b(fm)
InitBertrand(fm)
InitDualTheorem4(fm)

# IV. The UPG
InitPartIV(fm)
InitUPG1(fm)
InitUPG2(fm)
InitUPG3(fm)

# V. Future Work
InitPartV(fm)
InitFuture1(fm)
InitFuture2(fm)
InitFuture3(fm)
InitQuestions(fm)

# X. Representations
InitPartX(fm)

staticpos = 0
statictick = 0

fm.LoadFrame(currFrameNum)
while True:
	clock.tick(60)

	
	for event in pygame.event.get():
		if (event.type == KEYDOWN):
			if (event.key == K_LEFT):
				currFrameNum -= 1
			elif (event.key == K_RIGHT):
				currFrameNum += 1
			elif (event.key == K_ESCAPE):
				sys.exit()

			fm.LoadFrame(currFrameNum)
		
		elif event.type == MOUSEBUTTONDOWN:
			if (event.button == 1):
				currFrameNum += 1
			else:
				if (currFrameNum > 0):
					currFrameNum -= 1
			
			fm.LoadFrame(currFrameNum)
		
		elif event.type == pygame.QUIT:
			sys.exit()
	
	backbuf.blit(backstatic[staticpos], (0,0))
	
	statictick += 1
	if (statictick > 10):
		staticpos = (staticpos + 1) % len(backstatic)
		statictick = 0
	
	# Blit the text
	#backbuf.blit(text, (0,0))
	#textbuf.Render(backbuf)
	fm.Render(backbuf)
	
	screen.blit(backbuf, (0, 0))
	pygame.display.flip()