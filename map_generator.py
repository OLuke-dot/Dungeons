import pygame


class game_graphics:
    def __init__(self, player, inv):
        self.winWidth = 960
        self.winHeight = 540
        self.x_p = 50
        self.y_p = 50
        self.width_p = 40
        self.height_p = 60
        self.mainLoop(player, inv)

    def mainLoop(self, player, inv):
        isJump = False
        jumpCount = 10
        run = True
        pygame.init()
        window = pygame.display.set_mode((self.winWidth, self.winHeight))
        pygame.display.set_caption('Dungeons')
        while run:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_file(player, inv)
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.x_p > player.vel:
                self.x_p -= player.vel
            if keys[pygame.K_d] and self.x_p < self.winWidth - self.width_p - player.vel:
                self.x_p += player.vel
            if not(isJump):
                if keys[pygame.K_w] and self.y_p > player.vel:
                    self.y_p -= player.vel
                if keys[pygame.K_s] and self.y_p < self.winHeight - self.height_p - player.vel:
                    self.y_p += player.vel
                if keys[pygame.K_SPACE]:
                    isJump = True
            else:
                if jumpCount >= -10:
                    neg = 1
                    if jumpCount < 0:
                        neg = -1
                    self.y_p -= (jumpCount**2) * 0.5 * neg
                    jumpCount -= 1
                else:
                    isJump = False
                    jumpCount = 10
            window.fill((0, 0, 0))  # Probably to throw out
            pygame.draw.rect(window, (255, 0, 0), (self.x_p, self.y_p, self.width_p, self.height_p))
            pygame.display.update()
        pygame.quit()

    def save_file(self, player, inv)
