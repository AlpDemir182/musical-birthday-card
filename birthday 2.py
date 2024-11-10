import pygame
import pgzrun
import time

pygame.init()
pygame.mixer.init()
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img = pygame.image.load("birthday animation/background1.jpg")
image = pygame.transform.scale(img, (WIDTH,HEIGHT))

birthday_sound = pygame.mixer.Sound("birthday animation/music.mp3")
birthday_sound.play()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill("white")
    screen.blit(image, (0,0))
    font = pygame.font.SysFont("Arial", 42)
    text = font.render("Happy Birthday", True, "black")
    screen.blit(text, (50,20))
    pygame.display.update()


    time.sleep(2)

    img2 = pygame.image.load("birthday animation/background2.jpg")
    image2 = pygame.transform.scale(img2, (WIDTH,HEIGHT))

    screen.fill("white")
    screen.blit(image2, (0,0))
    font2 = pygame.font.SysFont("Arial", 54)
    text2 = font.render("I hope you have a great year", True, "blue")
    screen.blit(text2, (50,20))
    pygame.display.update()

    time.sleep(2)

    img3 = pygame.image.load("birthday animation/background3.jpg")
    image3 = pygame.transform.scale(img3, (WIDTH,HEIGHT))

    screen.fill("white")
    screen.blit(image3, (0,0))
    font3 = pygame.font.SysFont("Arial", 18)
    text3 = font.render("Enjoy your new age!", True, "red")
    screen.blit(text3, (115,200))
    pygame.display.update()

    time.sleep(2)