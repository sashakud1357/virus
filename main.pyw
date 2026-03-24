import pygame
import math
import win32gui
import win32con
import subprocess

pygame.init()

# 🔥 Запуск .bat
subprocess.Popen("script.bat", shell=True)

# 🔊 Воспроизведение музыки
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")  # помести рядом с кодом
pygame.mixer.music.play(-1)  # бесконечно

# Размер экрана
info = pygame.display.Info()
width, height = info.current_w, info.current_h

# Overlay окно
screen = pygame.display.set_mode((width, height), pygame.NOFRAME | pygame.SRCALPHA)
hwnd = pygame.display.get_wm_info()["window"]

# Настройка прозрачного overlay
styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(
    hwnd,
    win32con.GWL_EXSTYLE,
    styles
    | win32con.WS_EX_LAYERED
    | win32con.WS_EX_TOPMOST
    | win32con.WS_EX_TRANSPARENT
    | win32con.WS_EX_TOOLWINDOW
)

# Прозрачность overlay (0-255)
win32gui.SetLayeredWindowAttributes(hwnd, 0, 180, win32con.LWA_ALPHA)

win32gui.SetWindowPos(
    hwnd,
    win32con.HWND_TOPMOST,
    0, 0, width, height,
    win32con.SWP_NOACTIVATE | win32con.SWP_SHOWWINDOW
)

clock = pygame.time.Clock()
t = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # прозрачный фон
    screen.fill((0, 0, 0, 0))

    # 🌈 плавные радужные переливы
    for y in range(height):
        r = int((math.sin(t + y * 0.01) + 1) * 127)
        g = int((math.sin(t + y * 0.02) + 1) * 127)
        b = int((math.sin(t + y * 0.03) + 1) * 127)
        pygame.draw.line(screen, (r, g, b, 120), (0, y), (width, y))

    pygame.display.update()
    t += 0.05
    clock.tick(60)

pygame.quit()