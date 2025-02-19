import pygame as pg
from math import pi, sin, cos

# Color settings
white = (255, 255, 255)
gray = (100, 100, 100)
black = (0, 0, 0)

# Constants
radius_scale = 200  # Increased scale for better visibility

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

    terms = 5
    time_step = 0.01  # Adjusted time step for smoother waves
    max_points = 2000

    # Get user input for the equation
    equation_input = input("Enter equation (e.g., 'sin(x)', 'cos(x)', 'sin(x) + cos(x)', etc.): ")

    # Define the lambda function for the equation
    wave_function = lambda t: eval(equation_input, {"x": t, "sin": sin, "cos": cos, "pi": pi})

    screen = pg.display.set_mode((width, height))

    text = ["Enter your equation and watch the wave:",
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

        x = start_x
        y = start_y

        # Mark center point of circles
        pg.draw.circle(screen, (255, 0, 0), (round(x), round(y)), 3)

        circles = []
        lines = [(start_x, start_y)]

        for i in range(terms):
            prev_x = x
            prev_y = y

            n = i + 1

            # Calculate the radius using the input equation and apply radius scale for bigger waves
            radius = radius_scale * wave_function(n * time)  # Apply equation for each term

            # Update x and y positions for each term
            x += radius * cos(n * time)  # Moving along x-axis (epicycle concept)
            y += radius * sin(n * time)  # Moving along y-axis (epicycle concept)

            circles.append(((round(prev_x), round(prev_y)), round(abs(radius))))
            lines.append((x, y))

        # Draw circles first, then lines for clarity
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


# Run the main function
if __name__ == "__main__":
    main()
