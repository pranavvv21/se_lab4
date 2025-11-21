import pygame
from game.game_engine import GameEngine

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Initialize game engine
engine = GameEngine(WIDTH, HEIGHT)

def main():
    # Show the menu *before* starting the first game
    engine.target_score = engine.show_menu(SCREEN)

    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        winner = engine.check_game_over(SCREEN)
        if winner:
            # Show winner message
            SCREEN.fill((0, 0, 0))
            font = pygame.font.SysFont("Arial", 50)
            text_surface = font.render(f"{winner} Wins!", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(engine.width // 2, engine.height // 2))
            SCREEN.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.time.delay(2000)

            # Show the menu again after game over
            new_target = engine.show_menu(SCREEN)
            engine.target_score = new_target
            engine.player_score = 0
            engine.ai_score = 0
            engine.ball.reset()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
    