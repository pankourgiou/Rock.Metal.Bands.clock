import pygame
import math
import datetime
import random

# Rock/metal bands and albums
bands_and_albums = [
    ("Metallica", "Master of Puppets"),
    ("Iron Maiden", "The Number of the Beast"),
    ("Black Sabbath", "Paranoid"),
    ("Slayer", "Reign in Blood"),
    ("Pantera", "Vulgar Display of Power"),
    ("Led Zeppelin", "IV"),
    ("Pink Floyd", "The Wall"),
    ("L", "discography"),
    ("Megadeth", "Rust in Peace"),
    ("AC/DC", "Back in Black"),
    ("System of a Down", "Toxicity"),
    ("Animals as Leaders", "Animals as Leaders"),
    ("Deep Purple", "Machine Head"),
    ("Judas Priest", "British Steel"),
    ("Queen", "A Night at the Opera"),
    ("Animals as Leaders", "Weightless")
]

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Metal/Rock Clock")
font = pygame.font.SysFont("arial", 20)
band_font = pygame.font.SysFont("arial", 26, bold=True)
clock = pygame.time.Clock()

def draw_clock(surface, center, time_now):
    pygame.draw.circle(surface, (40, 40, 40), center, 250)
    pygame.draw.circle(surface, (180, 0, 0), center, 5)

    for i in range(60):
        angle = math.radians(i * 6)
        x1 = center[0] + 240 * math.sin(angle)
        y1 = center[1] - 240 * math.cos(angle)
        x2 = center[0] + 230 * math.sin(angle)
        y2 = center[1] - 230 * math.cos(angle)
        pygame.draw.line(surface, (100, 100, 100), (x1, y1), (x2, y2), 1)

    hour = time_now.hour % 12
    minute = time_now.minute
    second = time_now.second

    def draw_hand(length, angle, color, width):
        angle_rad = math.radians(angle)
        x = center[0] + length * math.sin(angle_rad)
        y = center[1] - length * math.cos(angle_rad)
        pygame.draw.line(surface, color, center, (x, y), width)

    hour_angle = (hour + minute / 60) * 30
    minute_angle = (minute + second / 60) * 6
    second_angle = second * 6

    draw_hand(120, hour_angle, (200, 0, 0), 8)
    draw_hand(180, minute_angle, (255, 255, 255), 5)
    draw_hand(200, second_angle, (255, 0, 0), 2)

# Main loop
running = True
last_hour = -1
current_band = random.choice(bands_and_albums)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()

    # Change band/album only at the start of each hour
    if now.hour != last_hour:
        current_band = random.choice(bands_and_albums)
        last_hour = now.hour

    screen.fill((10, 10, 10))
    draw_clock(screen, (WIDTH // 2, HEIGHT // 2), now)

    # Display band and album
    band_text = band_font.render(f"{current_band[0]}", True, (255, 255, 255))
    album_text = font.render(f"Album: {current_band[1]}", True, (200, 200, 200))
    screen.blit(band_text, (WIDTH//2 - band_text.get_width()//2, HEIGHT - 80))
    screen.blit(album_text, (WIDTH//2 - album_text.get_width()//2, HEIGHT - 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
