import pygame
import math
from random import choice
from words import word_list




#set up display
pygame.init()
WIDTH , HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Hangman Game")
fontt = pygame.font.SysFont(None, 80)





def get_word():
    # get random choice from list
    random_choice = choice(word_list)
    # remove choice from list to prevent selection again
    word_list.remove(random_choice)
    # return random choice
    return random_choice




#load images
images = []
for i in range(8):
    images.append(pygame.image.load("hangman"+str(i)+".png"))



#fonts
letter_font = pygame.font.SysFont("comicsans",40)



#buttons variables
RADUIS =20
GAP = 15
buttons =[]
start_x = round((WIDTH -(RADUIS*2 + GAP) *13)/2)
start_y= 400
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vis = [True for i in range(26)]


#buttons postions
for i in range(26):
    x = start_x +  GAP *2 + (RADUIS*2 + GAP) * (i%13)
    y = start_y + (GAP + RADUIS*2) *(i//13)
    buttons.append([x,y])


#game variables
guessed=[]
word =get_word().upper()
hangman_index = 0
print(word)




#draw buttons
def draw():
    win.fill((255,255,255)) #fills the window with white color
    #draw buttons
    count=0
    for button in buttons:
        x,y = button
        if vis[count]:
            pygame.draw.circle(win,(0,0,0),(x,y),RADUIS,3)
            text = letter_font.render(letters[count],1,(0,0,0))

            #to make letters in center perfectly
            text_x = x - text.get_width()/2
            text_y = y - text.get_height()/2
            win.blit(text,(text_x,text_y))
        count+=1

    display_word=""
                   
    
    #draw word dashed
    for l in word:
        if l.upper() in guessed:
            display_word += l +" "
        else:
            display_word += "- "
    scored = fontt.render(display_word, True, (0,0,0))
    win.blit(scored, (400,250))
    
    

        
def display_message(message):
    
    win.fill((255,255,255))
    text2 = fontt.render(message, True, (255,0,0))
    win.blit(text2,(WIDTH/2 - text2.get_width() /2 ,HEIGHT/2 -text2.get_height() /2 ))
    
    text3 = fontt.render("The word is: "+word , True, (0,0,255))
    win.blit(text3,(WIDTH/2 - text3.get_width() /2 ,HEIGHT/2+100 -text3.get_height() /2 ))
    pygame.display.update()





FPS = 80
clock = pygame.time.Clock()
run = True










#Game Loop

while run:
    clock.tick(FPS) #makes sure that the loop runs at the speed we determined

    
    
    

    


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            #print(mx,my)
            count=0
            for button in buttons:
                x,y = button

                if vis[count]:
                
                    dis = math.sqrt((x-mx)**2 + (y-my)**2)
                    #checks for collision in every button
                    #that if it inside the raduis then there is a collision
                    
                    
                    if dis < RADUIS:
                        #print(letters[count])
                        #print(count)
                        vis[count] = False

                        guessed.append(letters[count])
                        if letters[count] not in word:
                            hangman_index+=1
                            
                    
                count+=1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vis = [True for i in range(26)]
                guessed=[]
                word =get_word().upper()
                print(word)
                draw()
                hangman_index=0

                
    
    draw()
    
    
    #draw imags
    win.blit(images[hangman_index],(150,100))
    
    
    
    
    win_condition =True
    for letter in word:
        if letter not in guessed:
            win_condition =False
            
    if win_condition:
        
        display_message("you won")
        
        
                
    if hangman_index ==7:
        
        display_message("Game over")
        
        
        


    


    
    
    pygame.display.update()

pygame.quit()
