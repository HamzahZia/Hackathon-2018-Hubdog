import pygame
import vkeyboard

RED = (255,0,0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
DARK_GRAY = (128, 128, 128)

import GLOBAL

class Display:
  def __init__(self, pygame):
    self.fontObj = pygame.font.Font('assets/PressStart2P.ttf', 20)
    self.dogImages = []
    self.dogIndex = 0
    self.dogFace = 0

    self.fontHighScore = pygame.font.Font('assets/PressStart2P.ttf', 50)
    self.fontColumn = pygame.font.Font('assets/PressStart2P.ttf', 30)
    self.fontData = pygame.font.Font('assets/PressStart2P.ttf', 20)
    
    leftImages = []
    rightImages = []
    bigBanks = {}
    smallBanks = {}

    left1 = pygame.image.load('assets/move/left1.png')
    left2 = pygame.image.load('assets/move/left2.png')
    left1 = pygame.transform.scale(left1, (GLOBAL.PLAYER_WIDTH, GLOBAL.PLAYER_HEIGHT))
    left2 = pygame.transform.scale(left2, (GLOBAL.PLAYER_WIDTH, GLOBAL.PLAYER_HEIGHT))

    right1 = pygame.image.load('assets/move/right1.png')
    right2 = pygame.image.load('assets/move/right2.png')
    right1 = pygame.transform.scale(right1, (GLOBAL.PLAYER_WIDTH, GLOBAL.PLAYER_HEIGHT))
    right2 = pygame.transform.scale(right2, (GLOBAL.PLAYER_WIDTH, GLOBAL.PLAYER_HEIGHT))

    attack1 = pygame.image.load('assets/attack/attackLeft.png')
    attack2 = pygame.image.load('assets/attack/attackRight.png')
    attack1 = pygame.transform.scale(attack1, (GLOBAL.PLAYER_WIDTH, GLOBAL.PLAYER_HEIGHT))
    attack2 = pygame.transform.scale(attack2, (GLOBAL.PLAYER_WIDTH, GLOBAL.PLAYER_HEIGHT))

    # box assets:
    amex = pygame.image.load('assets/bigBank/amex.png')
    amex = pygame.transform.scale(amex, (GLOBAL.BOX_WIDTH, GLOBAL.BOX_HEIGHT))
    bmo = pygame.image.load('assets/bigBank/bmo.png')
    bmo = pygame.transform.scale(bmo, (GLOBAL.BOX_WIDTH, GLOBAL.BOX_HEIGHT))
    chase = pygame.image.load('assets/bigBank/chase.png')
    chase = pygame.transform.scale(chase, (GLOBAL.BOX_WIDTH, GLOBAL.BOX_HEIGHT))
    td = pygame.image.load('assets/bigBank/td.png')
    td = pygame.transform.scale(td, (GLOBAL.BOX_WIDTH, GLOBAL.BOX_HEIGHT))
    wellsFargo = pygame.image.load('assets/bigBank/wellsFargo.png')
    wellsFargo = pygame.transform.scale(wellsFargo, (GLOBAL.BOX_WIDTH, GLOBAL.BOX_HEIGHT))
    bigBanks = {'amex':amex, 'bmo':bmo, 'chase':chase, 'td':td, 'wellsFargo':wellsFargo}
    
    fido = pygame.image.load('assets/smallBank/fido.png')
    fido = pygame.transform.scale(fido, (GLOBAL.BOX_WIDTH, GLOBAL.BOX_HEIGHT))
    tangerine = pygame.image.load('assets/smallBank/tangerine.png')
    tangerine = pygame.transform.scale(tangerine, (GLOBAL.BOX_WIDTH, GLOBAL.BOX_HEIGHT))
    telstra = pygame.image.load('assets/smallBank/telstra.png')
    telstra = pygame.transform.scale(telstra, (GLOBAL.BOX_WIDTH, GLOBAL.BOX_HEIGHT))
    smallBanks = {'fido':fido, 'tangerine':tangerine, 'telstra':telstra}

    self.banks = {'B':bigBanks, 'S':smallBanks}

    # Document assets
    cheque = pygame.image.load('assets/document/cheque.png')
    cheque = pygame.transform.scale(cheque, (GLOBAL.CHEQUE_WIDTH, GLOBAL.CHEQUE_HEIGHT))
    invoice = pygame.image.load('assets/document/invoice.png')
    invoice = pygame.transform.scale(invoice, (GLOBAL.DOC_WIDTH, GLOBAL.DOC_HEIGHT))
    pdf = pygame.image.load('assets/document/pdf.png')
    pdf = pygame.transform.scale(pdf, (GLOBAL.DOC_WIDTH, GLOBAL.DOC_HEIGHT))

    self.documents = {'cheque':cheque, 'invoice':invoice, 'pdf':pdf}

    self.inserted = False
    # Competitor Assets
    comp = pygame.image.load('assets/enemy/veryfi.png')
    self.comp = pygame.transform.scale(comp, (GLOBAL.COMP_WIDTH, GLOBAL.COMP_HEIGHT))

    # bryan Assets:
    bryan = pygame.image.load('assets/bryan/bryan.png')
    self.bigBryan = pygame.transform.scale(bryan, (GLOBAL.BRYAN_WIDTH+20, GLOBAL.BRYAN_HEIGHT+20))
    bryan = pygame.transform.scale(bryan, (GLOBAL.BRYAN_WIDTH, GLOBAL.BRYAN_HEIGHT))
    bryan1 = pygame.image.load('assets/bryan/bryan1.png')
    bryan1 = pygame.transform.scale(bryan1, (GLOBAL.BRYAN_WIDTH, GLOBAL.BRYAN_HEIGHT))
    bryan2 = pygame.image.load('assets/bryan/bryan2.png')
    bryan2 = pygame.transform.scale(bryan2, (GLOBAL.BRYAN_WIDTH, GLOBAL.BRYAN_HEIGHT))
    self.bryans = [bryan, bryan1, bryan2]

    # map
    # self.map = pygame.image.load('assets/boss battle.png')

    leftImages.append(left1)
    leftImages.append(left2)
    rightImages.append(right1)
    rightImages.append(right2)

    self.dogImages.append(leftImages)
    self.dogImages.append(rightImages)
    self.dogImages.append(attack1)
    self.dogImages.append(attack2)

    self.gameDisplay = pygame.display.set_mode((GLOBAL.MAP_WIDTH, GLOBAL.MAP_HEIGHT))
    self.showKeyboard = False
    self.replace = False

  def drawBryans(self, bryans):
    for b in bryans:
      self.gameDisplay.blit(self.bryans[0], b.getRect())

  def drawBoxes(self, boxes):
    for b in boxes:
      self.gameDisplay.blit(self.banks[b.getSize()][b.getLogo()], b.getRect())
  
  # pass in the hp class into this function
  def drawHp(self, hp, hpValue):
    hp.setGameDisplay(self.gameDisplay)
    hp.healthBarMain(hpValue)
  
  def drawHomeBot(self,homeBot):
    homeBot.setGameDisplay(self.gameDisplay)

  def drawDocuments(self, docs):
    for d in docs:
      self.gameDisplay.blit(self.documents[d.getFormat()], d.getRect())

  def drawComps(self, comps):
    for c in comps:
      self.gameDisplay.blit(self.comp, c.getRect())

  def drawDog(self, dog, cooldownevent):
    # self.gameDisplay.blit(self.map, (0, 0))
    if (self.dogIndex == 19):
      self.dogIndex = 0

    if (dog.getMoveLeft()):
      self.dogFace = 0
    elif (dog.getMoveRight()):
      self.dogFace = 1

    if (dog.getMoveLeft() or dog.getMoveRight() or dog.getMoveUp() or dog.getMoveDown()):
      self.dogIndex += 1
    
    if (dog.getAttack()):
      if (self.dogFace == 0):
        dogImage = self.dogImages[2]
      elif(self.dogFace == 1):
        dogImage = self.dogImages[3]
      dog.attack(self.dogFace, cooldownevent)
      self.gameDisplay.blit(dogImage, (dog.getRect().x, dog.getRect().y))
    else:
      dogImage = self.dogImages[self.dogFace][self.dogIndex//10]
      self.gameDisplay.blit(dogImage, dog.getRect())
    
    if dog.hasPowerup():
      self.gameDisplay.blit(self.bigBryan, (GLOBAL.MAP_WIDTH - 90, 20, GLOBAL.BRYAN_WIDTH+20, GLOBAL.BRYAN_HEIGHT+20))

  def showEnterUsername(self, leaderboard, keyboard, text):
    if (not leaderboard.getReadLeaderboard()):
      self.replace = leaderboard.updateLeaderboard()
      leaderboard.setReadLeaderboard(True)

    if (not vkeyboard.FINISHED):
      self.showKeyboard = True
      keyboard.draw()
      spacing = 225
      for index in range(8):
        self.drawWord("_", spacing, 250, ((RED, RED)), self.fontHighScore)
        if (index < len(text)):
          self.drawWord(text[index], spacing, 220, ((RED, RED)), self.fontHighScore)
        spacing += 75

    if (vkeyboard.FINISHED and not self.inserted and self.replace):
      if (len(leaderboard.getScoreList()) <= leaderboard.getMaxList()):
        del leaderboard.getScoreList()[-1]
      leaderboard.setUsername(text)
      leaderboard.insertScore()
      self.inserted = True
      self.replace = False
    
    if (vkeyboard.FINISHED):
      self.showLeaderboard(leaderboard)

    
  def showLeaderboard(self, leaderboard):
    self.showKeyboard = False
    self.drawWord("HIGH SCORES", GLOBAL.MAP_WIDTH/2, 50, ((RED, RED)), self.fontHighScore)
    self.drawWord("RANK", 100, 100, ((YELLOW, YELLOW)), self.fontColumn)
    self.drawWord("SCORE", 500, 100, ((YELLOW, YELLOW)), self.fontColumn)
    self.drawWord("NAME", 900, 100, ((YELLOW, YELLOW)), self.fontColumn)
    spacing = 150
    rank = 1
    for score in leaderboard.getScoreList():
      self.drawWord(rank, 100, spacing, ((WHITE, DARK_GREEN)), self.fontData)
      self.drawWord(score["score"], 500, spacing, ((WHITE, DARK_GREEN)), self.fontData)
      self.drawWord(score["name"], 900, spacing, ((WHITE, DARK_GREEN)), self.fontData)
      spacing += 50
      rank += 1
    self.drawWord("Game over. Press A to play again", GLOBAL.MAP_WIDTH/2, spacing + 50, ((RED, RED)), self.fontData)

  def drawWord(self, text, x, y, colours, font=None):
    if font == None:
      font = self.fontObj
    word_surface = font.render(str(text), True, colours[0])
    word_rect = word_surface.get_rect()
    word_rect.center  = (x, y)

    word_outline = font.render(str(text), True, colours[1])
    outline_rect = word_outline.get_rect()
    outline_rect.center = (x - 1, y)
    self.gameDisplay.blit(word_outline, outline_rect)
    outline_rect.center = (x + 1, y)
    self.gameDisplay.blit(word_outline, outline_rect)
    outline_rect.center = (x - 1, y - 1)
    self.gameDisplay.blit(word_outline, outline_rect)
    outline_rect.center = (x - 1, y + 1)
    self.gameDisplay.blit(word_outline, outline_rect)
    outline_rect.center = (x + 1, y - 1)
    self.gameDisplay.blit(word_outline, outline_rect)
    outline_rect.center = (x + 1, y + 1)
    self.gameDisplay.blit(word_outline, outline_rect)
    outline_rect.center = (x, y - 1)
    self.gameDisplay.blit(word_outline, outline_rect)
    outline_rect.center = (x, y + 2)
    self.gameDisplay.blit(word_outline, outline_rect)
    self.gameDisplay.blit(word_surface, word_rect)
    return word_rect
