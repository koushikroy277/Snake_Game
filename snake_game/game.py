import pygame, random, time, sys

# Initializing the game
pygame.init()
clock = pygame.time.Clock()

# Declaring colours
orange = (255, 123, 7)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display measurement
display_width = 900
display_height = 600

GRIDSIZE = 25
GRID_WIDTH = display_width / GRIDSIZE
GRID_HEIGHT = display_height / GRIDSIZE

# Setting up display & caption
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake game")

snake_block = 15
snake_speed = 15
snake_list = []

class SNAKE(object):
    def __init__(self):
        self.positions = [((display_width / 2),
                           (display_height / 2))]
        self.color = (0, 155, 155)
    def head_positions(self):
        return self.positions[0]

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (0, 0, 0), r, 1)


# Defining the snake's structure


class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 255, 255)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, display_width - snake_block) / 10.0) * 10.0,
        (random.randint(0, display_width - snake_block) / 10.0) * 10.0


def main_snake_game():

    # Changes position
    x1_change = 0
    y1_change = 0

    snake_list = []
    lenth_of_snake = 1

    food_2 = Food()
    snake_2 = SNAKE()


    # Game Loop
    start = False
    end = False

    while not start:
        while end == True:
            dis.fill(blue)
            font_style = pygame.font.SysFont("Times New Roman", 37)
            msg = font_style.render("You lost! Wanna try again? Press Space bar", True, red)
            dis.blit(msg, [display_width / 6, display_height / 3])

            #Displaying the score
            score = lenth_of_snake - 1
            score_font = pygame.font.SysFont("Arial", 35)
            value = score_font.render(f"Your score: {str(score)}", True, blue)
            dis.blit(value, [display_width / 3, display_height / 5])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        main_snake_game()

                if event.type == pygame.QUIT:
                    start = True
                    end = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0

                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0

                if event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        snake_head = []

        snake_head.append(snake_2.positions)
        snake_list.append(snake_head)

        # Ending the games the length of snake exceeds
        if len(snake_list) > lenth_of_snake:
            del snake_list[0]

        # When the snake hits itself, end the game
        for x in snake_list[:-1]:
            if x == snake_head:
                end = True


        pygame.display.update()

        # Increases the snake's size when it eats the food
        if snake_2.head_positions() == food_2.position:
            lenth_of_snake += 1
            score += 1
            food_2.randomize_position()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

main_snake_game()












