import pygame 
import random 
import os
screen_width = 1000
screen_height = 600
pygame.mixer.init() 


pygame.init()
bgimg = pygame.image.load("back.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height))


gamewindow = pygame.display.set_mode((screen_width , screen_height))
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
yellow = (255, 255, 0)
orange = (255 , 165 , 0)
vibrantpurple = (128 , 0 ,128)
waterblue = (46 , 145 ,230)
Green = (0,255 , 0 )
cyan = (0, 255 , 255)
#Game title
pygame.display.set_caption("Snake Game")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)


    
def text_screen(text , color ,x,y):
    screen_text = font.render(text , True , color) 
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow, color , snk_list , snake_size):
    for x,y in snk_list :
        pygame.draw.rect(gamewindow , color , [x , y , snake_size , snake_size])

def welcome():
    exit_game= False
    while not exit_game:
        gamewindow.fill(cyan)
        text_screen("Welcome To Snake", black , 260 , 250)
        text_screen("Press Space Bar To Play", black , 229 , 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                  pygame.mixer.music.load("background.mp3")
                  pygame.mixer.music.play()
                  gameloop()
                  
                  
        pygame.display.update()
        clock.tick(60)

#GAME LOOP
def gameloop() :
    #GAME specsific variables
    exit_game = False
    game_over = False
    snake_x = 95
    snake_y = 105
    snake_size = 40
    fps = 60
    #Giving speed to our snake in X and Y direction 
    velocity_x = 0   #3
    velocity_y = 0  #3
    #Food for snake 
    food_x = random.randint(20 , screen_width-500)
    food_y = random.randint(20 , screen_height-300)
    score = 0
    init_velocity = 7
    snk_list = []
    snk_length = 1

    #Check is hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f :
            f.write("0")
            
    try:
       with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    except FileNotFoundError:
      with open("hiscore.txt", "w") as f:
        f.write("0")
        hiscore = "0"

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
              f.write(str(hiscore))
            gamewindow.fill(waterblue)
            text_screen("GAME OVER ! Press Enter To Contiune" , black , 130 , 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("background.mp3")
                        pygame.mixer.music.play()
                        gameloop()

        else:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x += init_velocity   #snake_x += 20
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x -= init_velocity  #snake_x -= 20
                        velocity_y = 0 
                    if event.key == pygame.K_UP:
                        velocity_y -= init_velocity  #snake_y -= 20
                        velocity_x = 0    
                    if event.key == pygame.K_DOWN:
                        velocity_y += init_velocity #snake_y += 20
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10
                    if event.key == pygame.K_SPACE :
                        score -= 10

        #Giving speed to our snake in X and Y direction 
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            
            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                pygame.mixer.music.load("eat.mp3")
                pygame.mixer.music.play()
                score += 10
                food_x = random.randint(20 , screen_width-400)
                food_y = random.randint(20 , screen_height-100)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gamewindow.fill(yellow)
            gamewindow.blit(bgimg,(0,0))

            #Screen saw Score on display
            text_screen("Score:" + str(score), black , 5,5)  
            text_screen("High Score: " + str(hiscore), black , 200, 5)
            #Food for snake foodshape and create 
            pygame.draw.rect(gamewindow , red ,[food_x , food_y , snake_size , snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
              del snk_list[0]
            
            

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("explosion1.mp3")
                pygame.mixer.music.play()

                

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("explosion1.mp3")
                pygame.mixer.music.play()
                
            
            #pygame.draw.rect(gamewindow , black , [snake_x , snake_y , snake_size , snake_size])
            plot_snake(gamewindow, vibrantpurple , snk_list , snake_size)
        pygame.display.update() 
        clock.tick(fps)
      


    pygame.quit()
    quit()
welcome()