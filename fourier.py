import pygame as pg
from math import pi, sin, cos

# Color settings
white = (255, 255, 255)
gray = (100, 100, 100)
black = (0, 0, 0)

# Constants
radius_scale = 100


def main():
    time = 0
    path = []

    pg.init()
    pg.font.init()
    font = pg.font.SysFont('Consolas', 24)

    pg.display.set_caption("Fourier")

    # CONFIG
    width = 1500
    height = 1000

    start_x = 300
    start_y = 500

    wave_x = 700

    terms = 2
    time_step = 0.005
    max_points = 2000

    wave_choice = 1  # default to square (map at end of file)
    ###############

    screen = pg.display.set_mode((width, height))

    text = ["Select a wave:",
            "1: Square    2: Sawtooth    3: Triangle     4: Sine    5: Cosine       6: Fourier Wave",
            "Up/Down: Number of terms     Left/Right: Speed"]

    running = True
    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.KEYUP])

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                key = event.unicode
                if keys[pg.K_ESCAPE]:
                    running = False
                if keys[pg.K_UP]:
                    terms += 1
                if keys[pg.K_DOWN] and terms > 1:
                    terms -= 1
                if keys[pg.K_LEFT] and time_step > 0.001:
                    time_step -= 0.001
                if keys[pg.K_RIGHT]:
                    time_step += 0.001
                if key == '1':
                    print("switching to square wave")
                    wave_choice = 1
                if key == '2':
                    print("switching to sawtooth wave")
                    wave_choice = 2
                if key == '3':
                    print("switching to triangle wave")
                    wave_choice = 3
                if key == '4':
                    print("switching to sine wave")
                    wave_choice = 4
                if key == '5':
                    print("switching to cosine wave")
                    wave_choice = 5
                if key == '6':
                    print("switching to Fourier wave")
                    wave_choice = 6

        x = start_x
        y = start_y

        # Mark center point of circles
        pg.draw.circle(screen, (255, 0, 0), (round(x), round(y)), 3)

        circles = []
        lines = [(start_x, start_y)]

        for i in range(0, terms):
            prev_x = x
            prev_y = y

            # For Fourier wave, pass time and terms
            if wave_choice == 6:
                n, radius = waves[wave_choice](i, time, terms)
            else:
                n, radius = waves[wave_choice](i)

            # Prevent "width greater than radius" exception
            if abs(radius) < 1:
                terms -= 1
                break

            x += radius * cos(n * time)
            y += radius * sin(n * time)

            circles.append(((round(prev_x), round(prev_y)), round(abs(radius))))
            lines.append((x, y))

        # Draw circles first, then lines for clarity
        print([circle[1] for circle in circles])
        for circle in circles:
            pg.draw.circle(screen, gray, circle[0], circle[1], 1)

        for i in range(0, len(lines) - 1):
            pg.draw.line(screen, white, lines[i], lines[i + 1], 2)

        # Draw line from circles to wave
        pg.draw.line(screen, gray, (x, y), (wave_x, y), 2)
        path = add_point(path, [wave_x, y], time_step * 50, max_points)
        draw_path(screen, path)

        message_box(screen, font, text)
        pg.display.update()
        screen.fill(black)

        time += time_step


def add_point(path, point, x_increment, max_points):
    path = [[point[0] + x_increment, point[1]] for point in path]

    path.insert(0, point)
    return path[:max_points]


def draw_path(screen, path):
    if len(path) > 1:
        pg.draw.lines(screen, white, False, path, 2)


def message_box(root, font, text):
    pos = 10
    for x in range(len(text)):
        rendered = font.render(text[x], 0, white)
        root.blit(rendered, (10, pos))
        pos += 30


def square_wave(i):
    n = 2 * i + 1
    radius = radius_scale * (4 / (n * pi))

    return n, radius


def sawtooth_wave(i):
    n = i + 1
    radius = radius_scale * (2 * (-1 ** (n + 1)) / (n * pi))

    return n, radius


def triangle_wave(i):
    n = 2 * i + 1
    # radius = radius_scale * 2 * (pi / 4) * (-1 ** i) * (n ** -2)
    radius = (radius_scale * 3) * (4 * (1 - (-1 ** n)) / ((pi ** 2) * (n ** 2)))

    return n, radius


def sine_wave(i):
    n = 1  # Only the fundamental frequency (first harmonic)
    radius = radius_scale * (1 / n)  # Amplitude for the fundamental frequency
    return n, radius


def cosine_wave(i):
    n = 1  # Only the fundamental frequency (first harmonic)
    radius = radius_scale * (1 / n)  # Amplitude for the fundamental frequency
    return n, radius


def fourier_wave(i, time, terms):
    # Sum of sine and cosine waves (Fourier series)
    x = 0
    y = 0

    # Loop through all terms (harmonics)
    for n in range(1, terms + 1):
        radius = radius_scale * (1 / n)  # Amplitude for each harmonic
        # Summing sine and cosine waves for the Fourier series
        x += radius * cos(n * time)  # Cosine component (real part)
        y += radius * sin(n * time)  # Sine component (imaginary part)

    return x, y


# Map wave choices to wave functions
waves = {
    1: square_wave,
    2: sawtooth_wave,
    3: triangle_wave,
    4: sine_wave,
    5: cosine_wave,
    6: fourier_wave  # New Fourier wave added
}

if __name__ == "__main__":
    main()
