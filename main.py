"""
https://paulbourke.net/fractals/lsys/


"""



import pygame
import math

class L_system:
	def __init__(self, axiom, rules, theta, start, length, scale, dtheta):
		self.sentence = axiom
		self.rules = rules
		self.theta = theta
		self.x, self.y = start
		self.length = length
		self.scale = scale
		self.dtheta = dtheta
		self.positions = []

	def __str__(self):
		return self.sentence

	def generate(self):
		newStr = ""
		for char in self.sentence:
			mapped = char
			try:
				mapped = self.rules[char]
			except:
				pass
			newStr += mapped 
		self.sentence = newStr

	def draw(self, screen):
		for char in self.sentence:
			if char == "F":
				x2 = self.x - self.length * math.cos(math.radians(self.theta))
				y2 = self.y - self.length * math.sin(math.radians(self.theta))
				pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (x2, y2))
				self.x, self.y = x2, y2
			elif char == "+":
				self.theta += self.dtheta
			elif char == "-":
				self.theta -= self.dtheta
			elif char == "[":
				self.positions.append({"x": self.x, "y": self.y, "theta": self.theta})
			elif char == "]":
				position = self.positions.pop()
				self.x, self.y, self.theta = position["x"], position["y"], position["theta"]
			elif char == ">":
				self.length += self.length * self.scale
			elif char == "<":
							self.length -= self.length * self.scale




if __name__ == "__main__":

	axiom = "F+F+F"
	rules = {
	"F": "F-F+F",
	}


	pygame.init()
	# Drawing Parameters
	size = (1000, 1000)
	theta = 90
	start = (0, 0)
	length = 10
	scale = 1.36 
	dtheta = 120

	screen = pygame.display.set_mode(size)
	sys = L_system(axiom, rules, theta, start, length, scale, dtheta)
	
	pressed = False
	running = True
	sys.draw(screen)

	while (running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYUP:
				sys.draw(screen)
				sys.generate()
				sys.theta = theta
				sys.x, sys.y = start
		print(sys)

		pygame.display.flip()

	pygame.quit()
	
