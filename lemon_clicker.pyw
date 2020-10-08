import pygame
import random
from image_button import Button
import bg
#Setup Stuff
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("Assets/sound/bg-music.mp3")
window = pygame.display.set_mode((600, 450)) #Original resolution 450 x 450
pygame.display.set_caption("Lemon Clicker") #Alpha 0.40
pygame.display.set_icon(pygame.transform.scale(pygame.image.load("Assets/fruits/lemon.png").convert_alpha(), (32, 32)))

#Variables
clock = pygame.time.Clock()
PLAYERSCORE = 0
extra_clicks = 0
global_timer = 0
minute_timer = 60
click_power = 1
click_power_timer = 0
timer_ready = False

#Class Variables
backg = bg.Background(window, "Assets/fruits/lemon.png")
lemon = Button(window, 25, 75, "Assets/fruits/Lemon.png", 400, 300)
AutoClick = Button(window, 450, 0, "Assets/buttons/Auto_Clicker_Button.png", 150, 150)
Lemonade = Button(window, 450, 150, "Assets/buttons/Lemonade_Button.png", 150, 150)
Double = Button(window, 450, 300, "Assets/buttons/Double_Button.png", 150, 150)

#Get Save Data
try:
    save_file = open("Assets/save_data.lemon", "r").read()
    save_file = save_file.split(" ")
    PLAYERSCORE = int(save_file[0])
    extra_clicks = int(save_file[1])
except Exception as e:
    open("Assets/save_data.lemon", "w").truncate(0)
    open("Assets/save_data.lemon", "w").write("0 0")

#Functions
def disp_text(window, x, y, text):
    font = pygame.font.SysFont("Comic Sans MS", 20)
    surface = font.render(text, False, (0, 0, 0))
    window.blit(surface, (x, y))

#Main Pygame Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Debug Keys: Up arrow sets the minute timer to 1, Down arrow resets scores to zero
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                minute_timer = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                PLAYERSCORE = 0
                extra_clicks = 0
        
    ''' Scripts that run every frame '''
    #Background Script
    backg.update()
    #Music Script
    if global_timer % 900 == 0:
        pygame.mixer.music.play()
    #Auto Click Script
    if global_timer % 30 == 0:
        PLAYERSCORE += (extra_clicks * click_power)
    #Click Power Script
    if click_power_timer > 0:
        if global_timer % 30 == 0:
            click_power_timer -= 1
    elif click_power_timer <= 0:
        click_power = 1
    #Minute timer script
    if global_timer % 30 == 0 and minute_timer > 0:
        minute_timer -= 1
        timer_ready = False
    if minute_timer <= 0:
        timer_ready = True
    
    #Class Updates
    #Buttons
    #Lemon
    lemon.update()
    if lemon.clicked:
        print(f"Lemon Clicked! Score = {PLAYERSCORE + 1}")
        PLAYERSCORE += (1 * click_power)
    #Auto Clicker Button
    AutoClick.update()
    if AutoClick.clicked:
        if PLAYERSCORE >= 100:
            PLAYERSCORE -= 100
            extra_clicks += 1
    #Lemonade Button
    Lemonade.update(disp_img = timer_ready)
    if Lemonade.clicked and timer_ready:
        minute_timer = 60
        timer_ready = False
        PLAYERSCORE += (200 * click_power)
    #Double Score Button
    Double.update(disp_img = timer_ready)
    if Double.clicked and timer_ready:
        minute_timer = 60
        timer_ready = False
        click_power = 2
        click_power_timer = 20

    disp_text(window, 0, 0, f"Score: {PLAYERSCORE} | AutoClicks: {extra_clicks} | Timer: {minute_timer} {'| READY' if minute_timer <=0 else ''}")
    disp_text(window, 0, 22, 'Double Points Time Left: '+str(click_power_timer) if click_power_timer > 0 else '')
    global_timer += 1
    pygame.display.update()
    clock.tick(30)
    window.fill((255, 255, 0))
    

#End of Pygame Loop, final save function before program exit
with open("Assets/save_data.lemon", "w") as savedata:
    savedata.truncate(0)
    savedata.write(f"{str(PLAYERSCORE)} {str(extra_clicks)}")
    savedata.close()
pygame.quit()
quit(0)
