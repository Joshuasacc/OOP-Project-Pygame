import pygame
from character import Character
import gamesetting as gs



class Game:
  def __init__(self, main, assets):
    # LINK WITH MAIN CLASS AND ASSETS
    self.MAIN = main
    self.ASSETS = assets

    # Player Character 
    self.PLAYER = Character(self,self.ASSETS.player_char)

    # Level Information
    self.level = 1
    self.level_matrix = self.generate_level_matrix(gs.ROWS,gs.COLS)

  def input(self):
    # for event in pygame.event.get():
    #   # CHECK IF RED CROSS IS CLICKED
    #   if event.type == pygame.QUIT:
    #     self.MAIN.running = False  
    #   elif event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_ESCAPE:
    #       self.MAIN.running = False
    self.PLAYER.input()

  def update(self):
    self.PLAYER.update()


  def draw(self,window):
    # self.PLAYER.draw(window)
    self.PLAYER.draw(window)

  def generate_level_matrix(self,rows,cols):
    """Generate the basic level matrix"""
    matrix = []
    for row in range(rows + 1):
      line = []
      for col in range(cols + 1):
        line.append("_")
      matrix.append(line)
    for row in matrix:
      print(row)
    return matrix
      

