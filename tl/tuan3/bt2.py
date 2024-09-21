import pygame
import sys
import math

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (50, 50, 50)
PLAYER_COLOR = (0, 0, 255)
PLAYER2_COLOR = (255, 0, 0)
ATTACK_COLOR = (255, 255, 0)
FPS = 60
PLAYER_SIZE = 50
ATTACK_SIZE = 10
ATTACK_SPEED = 10

# Initialize Pygame
pygame.init()

class Player:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = color
        self.vel = 5
        self.attack_cooldown = 0
        self.controls = controls
        self.facing_direction = 'right'  # Default facing direction
        self.score = 0  # Add a score attribute

    def move(self, keys, other_player):
        new_rect = self.rect.copy()
        
        if keys[self.controls['left']] and self.rect.left > 0:
            new_rect.x -= self.vel
            self.facing_direction = 'left'
        if keys[self.controls['right']] and self.rect.right < WIDTH:
            new_rect.x += self.vel
            self.facing_direction = 'right'
        if keys[self.controls['up']] and self.rect.top > 0:
            new_rect.y -= self.vel
        if keys[self.controls['down']] and self.rect.bottom < HEIGHT:
            new_rect.y += self.vel
        
        if not new_rect.colliderect(other_player.rect):
            self.rect = new_rect

    def attack(self, other_player):
        if self.attack_cooldown == 0:
            self.attack_cooldown = FPS // 2  # Cooldown for half a second
            
            # Determine turret position
            if self.facing_direction == 'right':
                turret_x = self.rect.right
                turret_y = self.rect.centery
            else:
                turret_x = self.rect.left - 10
                turret_y = self.rect.centery
            
            return Attack(turret_x, turret_y, self.facing_direction, other_player.rect.centerx, other_player.rect.centery)
        return None

    def update_cooldown(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def draw(self, win):
        # Draw the body of the tank
        pygame.draw.rect(win, self.color, self.rect)
        
        # Draw the turret (cannon)
        if self.facing_direction == 'right':
            turret_rect = pygame.Rect(self.rect.right - 20, self.rect.centery - 5, 20, 10)
        else:
            turret_rect = pygame.Rect(self.rect.left - 20, self.rect.centery - 5, 20, 10)
        
        pygame.draw.rect(win, (0, 0, 0), turret_rect)  # Draw the turret

class Attack:
    def __init__(self, x, y, direction, target_x, target_y):
        self.rect = pygame.Rect(x, y, ATTACK_SIZE, ATTACK_SIZE)
        
        # Calculate direction towards the target
        dx, dy = target_x - x, target_y - y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance != 0:  # Avoid division by zero
            self.vel_x = (dx / distance) * ATTACK_SPEED
            self.vel_y = (dy / distance) * ATTACK_SPEED
        else:
            self.vel_x = 0
            self.vel_y = 0

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def draw(self, win):
        pygame.draw.rect(win, ATTACK_COLOR, self.rect)

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tank Battle Game")
        self.clock = pygame.time.Clock()
        self.player1 = Player(100, HEIGHT // 2, PLAYER_COLOR, {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s, 'attack': pygame.K_f})
        self.player2 = Player(WIDTH - 150, HEIGHT // 2, PLAYER2_COLOR, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN, 'attack': pygame.K_RETURN})
        self.attacks = []

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player1.move(keys, self.player2)
        self.player2.move(keys, self.player1)

        for attack in self.attacks[:]:
            attack.move()
            if attack.rect.colliderect(self.player2.rect) and attack.vel_x > 0:
                print("Player 1 hits Player 2!")
                self.player1.score += 1  # Increase Player 1's score
                self.attacks.remove(attack)
            elif attack.rect.colliderect(self.player1.rect) and attack.vel_x < 0:
                print("Player 2 hits Player 1!")
                self.player2.score += 1  # Increase Player 2's score
                self.attacks.remove(attack)
            elif attack.rect.x > WIDTH or attack.rect.x < 0 or attack.rect.y > HEIGHT or attack.rect.y < 0:
                self.attacks.remove(attack)

        self.player1.update_cooldown()
        self.player2.update_cooldown()

        self.handle_attack_input()

    def handle_attack_input(self):
        keys = pygame.key.get_pressed()
        if keys[self.player1.controls['attack']]:
            attack = self.player1.attack(self.player2)
            if attack:
                self.attacks.append(attack)
        if keys[self.player2.controls['attack']]:
            attack = self.player2.attack(self.player1)
            if attack:
                self.attacks.append(attack)

    def draw(self):
        self.win.fill(BACKGROUND_COLOR)
        self.player1.draw(self.win)
        self.player2.draw(self.win)
        for attack in self.attacks:
            attack.draw(self.win)
        
        # Draw scores
        font = pygame.font.SysFont(None, 36)
        score_text1 = font.render(f"Player 1 Score: {self.player1.score}", True, (255, 255, 255))
        score_text2 = font.render(f"Player 2 Score: {self.player2.score}", True, (255, 255, 255))
        self.win.blit(score_text1, (10, 10))
        self.win.blit(score_text2, (WIDTH - score_text2.get_width() - 10, 10))

        pygame.display.update()

if __name__ == "__main__":
    Game().run()
