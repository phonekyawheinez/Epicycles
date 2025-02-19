from Image import Image
from Fourier import Fourier
from Plot import Plot


# # Use only one image (for example, apple.png)
# im_1 = Image("images/images.jpeg", (300, 300))
#
# path_1 = im_1.sort()
#
# # Perform Fourier transformation on the contours
# period_3, tup_circle_rads_3, tup_circle_locs_3 = Fourier(n_approx=600, coord_1=path_1).get_circles()
#
# # Plot the result
# Plot(period_3, tup_circle_rads_3, tup_circle_locs_3, speed=30).plot(close_after_animation=False)
#

import tkinter as tk
from tkinter import filedialog

class FourierTransformUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fourier Transform UI")
        self.root.configure(bg="#2b2b2b")


        self.image_label = tk.Label(self.root, text="Select an image (Png, Jpeg):", font=("Arial", 14), fg="#ffffff", bg="#2b2b2b")
        self.image_label.pack(pady=20)

        self.image_entry = tk.Entry(self.root, width=50, font=("Arial", 14), fg="#000000", bg="#cccccc")
        self.image_entry.pack()

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_image, font=("Arial", 14), fg="#ffffff", bg="#4CAF50")
        self.browse_button.pack(pady=10)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_fourier, font=("Arial", 14), fg="#ffffff", bg="#2196F3")
        self.run_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="Terminal :", font=("Arial", 14), fg="#ffffff", bg="#2b2b2b")
        self.result_label.pack(pady=20)

        self.result_text = tk.Text(self.root, height=10, width=50, font=("Arial", 14), fg="#000000", bg="#cccccc")
        self.result_text.pack()

    def browse_image(self):

        image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png .bmp")])
        self.image_entry.delete(0, tk.END)
        self.image_entry.insert(0, image_path)

    def run_fourier(self):

        image_path = self.image_entry.get()

        im_1 = Image(image_path, (400, 400))
        path_1 = im_1.sort()
        period_3, tup_circle_rads_3, tup_circle_locs_3 = Fourier(n_approx=900, coord_1=path_1).get_circles()
        Plot(period_3, tup_circle_rads_3, tup_circle_locs_3, speed=15).plot(close_after_animation=False)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Fourier transform performed successfully at"+ image_path)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = FourierTransformUI()
    ui.run()
