import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500  #screen dimension
win = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("PyGame - Hangman Game")  #TITLE

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('timesnewroman', 35)
WORD_FONT = pygame.font.SysFont('comicsans', 50)
TITLE_FONT = pygame.font.SysFont('comicsans', 60)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = ["PYTHON","PACKAGES", "PYGAME", "HANGMAN","PYMONGO","PANDAS","NUMPY"]
word = random.choice(words)
guessed = []

# colors
BLACK = (0,0,0)
GRAY = (220,220,220)
RED=(255, 87, 51 )
GREEN=(127, 255, 0)


def draw():
    win.fill(GRAY)

    # draw title
    text = TITLE_FONT.render("HANGMAN-PyGame", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    #blit will draw the image
    win.blit(images[hangman_status], (150, 100))
    #update will update the screen after the image is drawn
    pygame.display.update()


def display_message(message,color):
    pygame.time.delay(1000)
    win.fill(GRAY)
    text = WORD_FONT.render(message, 1, color)
    
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    FPS = 60  #speed of the game
    clock = pygame.time.Clock()
    run = True  

    while run:
        clock.tick(FPS)
        #keyboard input
        #if event.key == pygame.K_a:
                #print("Key A has been pressed")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #quit button
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:  #to get mouse position(x,y)
                m_x, m_y = pygame.mouse.get_pos()     #increase x--right ,y--down 
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            color="GREEN"
            display_message("You WON!",color)
            break

        if hangman_status == 6:
            color="RED"
            display_message("You LOST!",color)
            break
    
while True:
    
    main()
pygame.quit()
