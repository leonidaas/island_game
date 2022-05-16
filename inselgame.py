from shutil import move
import pygame
import pygame_assets as assets
import random
import time

WIDTH = 1024
HEIGHT = 780
SIZES = [(75, 75), (125, 125), (100, 100)]
island_rects = []
player_rect = None

class Island():
    def __init__(self):
        self.x = random.randint(0,WIDTH-125)
        self.y = random.randint(0,HEIGHT-125)
        self.size = SIZES[random.randint(len(SIZES)-1)] 
        self.image = 'assets/image/island2.png'


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/image/boat.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,HEIGHT / 2)
        self.image_size = (75, 75)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
    
def place_islands(pygame, screen):
    island_image = pygame.image.load('assets/image/island2.png').convert_alpha()
    counter = 0
    while counter < 5:
        #time.sleep(3)
        print("Durchlauf: " + str(counter))
        x = random.randint(50, WIDTH-100)
        y = random.randint(50, HEIGHT-100)

        print("x:" + str(x) + "y: " + str(y))
        
        size = SIZES[random.randint(0, len(SIZES)-1)] 

        image = pygame.transform.scale(island_image, size)
        island_rect = image.get_rect()
        island_rect.center = (x, y)
        
        shouldSkip = False
        shouldSkip = check_if_collides(island_rect)

        if len(island_rects) == 0:
            island_rects.append(island_rect)
    
        if shouldSkip == False:
            island_rects.append(island_rect)
            counter += 1
            screen.blit(image, island_rect)
            pygame.display.update()  

def place_player(pygame, screen, player):
    boat_image = pygame.image.load(player.imageUrl).convert_alpha()
    image = pygame.transform.scale(boat_image, player.image_size)
    image_rect = image.get_rect()
    image_rect.center = (player.x, player.y)

    while(check_if_collides(image_rect)):
        player.x += random.randint(0, 100)
        player.y += random.randint(0, 100)
        image_rect.center = (player.x, player.y)

    return (image, image_rect)
    #screen.blit(image, image_rect)

def move_player(image_rect, moveToX, moveToY):
    image_rect.center = (moveToX, moveToY)
    
    return image_rect

def check_if_collides(rect):
    for currentRect in island_rects:
            print(rect)
            if rect.colliderect(currentRect):
                print("collided")
                return True
    return False
        

def main():
    pygame.init()

    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Urlaub")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    

    player_sprite = Player()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player_sprite)

    place_islands(pygame, screen)
    #(image, image_rect) = place_player(pygame, screen, player)
    #move_player(player, 50)


    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                image_rect = move_player(image_rect, 50, 50)
        
        screen.fill("blue")
        all_sprites.update()
        all_sprites.draw(screen)
        #screen.blit(image, image_rect)
        pygame.display.update()


if __name__== "__main__":
    # call the main function
    main()
