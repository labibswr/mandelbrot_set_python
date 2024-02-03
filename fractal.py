# Fractals Tkinter
# Developer: Labib Sarwar
# Date: October 20, 2022

import tkinter


# If it is a divergent point, the number of iterations used (i) is used to
# place it in a specific orbitaL.
def gradient (iterations_used, running_x, running_y, canvas):
    if iterations_used < 2:
        canvas.create_line(running_x, running_y, running_x + 1, running_y + 1,
                           fill="#BAF2FF")
    elif iterations_used < 4:
        canvas.create_line(running_x, running_y, running_x + 1, running_y + 1,
                           fill="#9AE9FC")
    elif iterations_used < 6:
        canvas.create_line(running_x, running_y, running_x + 1, running_y + 1,
                           fill="#64D9F5")
    elif iterations_used < 8:
        canvas.create_line(running_x, running_y, running_x + 1, running_y + 1,
                           fill="#3DC0E0")
    elif iterations_used < 10:
        canvas.create_line(running_x, running_y, running_x + 1, running_y + 1,
                           fill="#1BA3C4")


def main():
    # Open up tkinter window 800x800
    window = tkinter.Tk()
    window.geometry("800x800")
    window.title("Mandelbrot Fractal")
    canvas = tkinter.Canvas(window, width = 800, height = 800, bg="#0682A0")

    # Define constant variables such as the minimum and maximum ranges
    # of the complex plane (x min/max and y min/max)
    x_min = -2
    x_max = 1
    y_min = -1
    y_max = 1
    iter_c = 250            # Number of iterations through recursive formula

    # Set up for loop to iterate through every pixel in the 800x800 window
    for y in range(800):
        for x in range(800):
            # Convert the pixel coordinate to coordinate on the complex plane
            c = complex(x_min + (x_max - x_min) * x / 800,
                        y_min + (y_max - y_min) * y / 800)
            # Set z0 as 0, and the number of iterations
            z = 0
            i = 0
            is_divergent = False    # Setting up condition for while loop
            while i < iter_c and is_divergent is False:
                # Recursive sequence formula used to determine whether the
                # point is divergent or not.
                z = (z * z) + c
                # Boolean changed to break out of while loop if z exceeds 100
                if abs(z) >= 1000:
                    is_divergent = True
                i += 1
            # If point is non-divergent, it is plotted as part of the
            # Mandelbrot set
            if is_divergent is False:
                canvas.create_line(x, y, x+1, y+1)
            # If point is divergent, gradient function and i value is used
            # for surrounding orbital.
            else:
                gradient(i, x, y, canvas)

    canvas.pack()
    window.mainloop()


main()
