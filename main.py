import pygame  
import time    
import datetime
               
               
pygame.init()  
LEVELS = {     
    1: [       
        [0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [2, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 4, 4, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 4, 4, 4, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 2, 0, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    2: [
        [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 3],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
        [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 4, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 4, 4, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1]
    ],
    3: [
        [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 2, 2, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 4, 4, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 4, 4, 1, 4, 4, 1, 1, 1, 1, 1]
    ],
    4: [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

}
SCRENN_WEIGHT = 750
SCRENN_HEIGHT = 750
TILE_SIZE = 50
game_over = 0
MAX_LEVELS = 4
level_num = 1
main_menu = True
end_game = False
start_time = time.time()
start_time_play = datetime.datetime.now()
font = pygame.font.SysFont('Verdana', 29)
font.set_bold(True)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((SCRENN_WEIGHT, SCRENN_HEIGHT))
pygame.display.set_caption('Skyboard')
icon_image = pygame.image.load('img/logo.png')
pygame.display.set_icon(icon_image)
file_object = open('time_game_play.txt', 'a')


background = pygame.transform.scale(
    pygame.image.load('img/bg1.png'), (1000, 1000))
start_button_img = pygame.image.load('img/play.png')
quit_button_img = pygame.image.load('img/quit.png')
restart_button_img = pygame.image.load('img/restart.png')
game_over_button_img = pygame.image.load('img/game_over.png')


def reset_level_on(level):
    player.reset(100, SCRENN_HEIGHT - 128)
    lava_group.empty()
    exit_group.empty()
    if level in LEVELS:
        world_data = LEVELS[level]
        return World(world_data)
    else:
        print('Неверный номер уровня')
        return None


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        elif pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)

        return action


class World():
    def __init__(self, data):
        self.tile_list = []

        earth_img = pygame.image.load('img/dirt4.png')
        grass_img = pygame.transform.scale(pygame.image.load(
            'img/tree.png'), (TILE_SIZE * 2, TILE_SIZE * 2))
        door_img = pygame.transform.scale(pygame.image.load(
            'img/door.png'), (TILE_SIZE * 2, TILE_SIZE * 2))

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(
                        earth_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    img_rect.width = TILE_SIZE - 25
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(
                        grass_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE + 4
                    img_rect.width = TILE_SIZE - 25
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    exit = Exit(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    exit_group.add(exit)
                if tile == 4:
                    lava = Lava(col_count * TILE_SIZE,
                                row_count * TILE_SIZE + 27)
                    lava_group.add(lava)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        direction_x = 0
        direction_y = 0
        walking_animation = 5
        if game_over == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.in_air == False:
                self.position_y = -15
                self.jumped = True
                self.on_ground = False
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                direction_x -= 5
                self.resist += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                direction_x += 5
                self.resist += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.resist = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            if self.resist > walking_animation:
                self.resist = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            self.position_y += 1
            if self.position_y > 10:
                self.position_y = 10
            direction_y += self.position_y

            def x_collision(tile, direction_x):
                if tile[1].colliderect(self.rect.x + direction_x, self.rect.y, self.width, self.height):
                    return 0
                return direction_x

            def y_collision(tile, direction_y):
                if tile[1].colliderect(self.rect.x, self.rect.y + direction_y, self.width, self.height):
                    if self.position_y < 0:
                        direction_y = tile[1].bottom - self.rect.top
                        self.position_y = 0
                    elif self.position_y >= 0:
                        direction_y = tile[1].top - self.rect.bottom
                        self.position_y = 0
                        self.in_air = False
                return direction_y

            self.in_air = True

            for tile in world.tile_list:
                direction_x = x_collision(tile, direction_x)
                direction_y = y_collision(tile, direction_y)

            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > SCRENN_WEIGHT:
                self.rect.right = SCRENN_WEIGHT

            if self.rect.top < 0:
                self.rect.top = 0
                self.position_y = 0
            elif self.rect.bottom > SCRENN_HEIGHT:
                self.rect.bottom = SCRENN_HEIGHT
                self.position_y = 0
                self.in_air = False

            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1

            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            self.rect.x += direction_x
            self.rect.y += direction_y

        elif game_over == -1:
            self.image = self.dead_ghost

        screen.blit(self.image, self.rect)

        return game_over

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.resist = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/hero{num}.png')
            img_right = pygame.transform.scale(img_right, (75, 50))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.dead_ghost = pygame.image.load('img/ghost.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.position_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = 0


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/lava.png')
        self.image = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/door.png')
        self.image = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


player = Player(100, SCRENN_HEIGHT - 128)
lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
restart_button = Button(SCRENN_WEIGHT // 2 - 40,
                        SCRENN_HEIGHT // 2 - 10, restart_button_img)
start_button = Button(SCRENN_WEIGHT // 2 - 325,
                      SCRENN_HEIGHT - 450, start_button_img)
exit_button = Button(SCRENN_WEIGHT // 2 + 100,
                     SCRENN_HEIGHT - 450, quit_button_img)
game_over_button = Button(SCRENN_WEIGHT // 2 - 150,
                          SCRENN_HEIGHT // 2 - 150, game_over_button_img)


def load_level(level_number):
    return LEVELS.get(level_number, None)


world_data = load_level(level_num)

world = World(world_data)
clock = pygame.time.Clock()
result_time = 0
run = True

while run:
    screen.blit(background, (0, 0))

    if main_menu:
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False

    else:
        world.draw()
        lava_group.update(game_over)
        lava_group.draw(screen)
        exit_group.draw(screen)

        if level_num == 4:
            game_over_button.draw()
            text = font.render(
                f'Время прохождения: {result_time} секунд', 1, BLACK)
            screen.blit(text, (150, 175))

        game_over = player.update(game_over)

        if game_over == -1:
            if restart_button.draw():
                player.reset(100, SCRENN_HEIGHT - 128)
                game_over = 0

        if game_over == 1:
            level_num += 1
            if level_num <= MAX_LEVELS:
                world_data = load_level(level_num)
                if world_data:
                    world = reset_level_on(level_num)
                    game_over = 0
                    end_game = True
                    result_time = round(time.time() - start_time, 2)
                else:
                    print('Error')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(60)

file_object.write(
    f'Время прохождения: {str(result_time)} секунд. Дата: {start_time_play} \n')
file_object.close()
