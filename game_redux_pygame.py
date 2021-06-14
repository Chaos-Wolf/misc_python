import pygame
from pygame.locals import *

class Window:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.weight, self.height = 640, 400
		self.screen=pygame.display.set_mode(self.size)
		self.mouse = pygame.mouse.get_pos()
	
	def on_init(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True
		self.screen.fill((60,25,60))
		
	def on_event(self, event):
		if event.type == QUIT:
			self.on_exit()
		if event.type == MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			if self.weight/2 <= mouse[0] <= self.weight/2+140 and self.height/2 <= mouse[1] <= self.height/2+40:
				print("hello world")
	def on_loop(self):
		pass
	
	def on_render(self):
		pass 
	
	def on_cleanup(self):
		pygame.quit()
		
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
			
		while(self._running):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()

if __name__ == "__main__" :
	window = Window()
	window.on_execute()