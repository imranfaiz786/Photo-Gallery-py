import os
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class PhotoGalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PHOTO GALLERY")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        self.image_files = []

        # Add a background color and title font
        self.root.configure(bg="#ff61bc")
        
        # Title Label
        self.title_label = tk.Label(self.root, text="Photo Gallery", bg="#ff61bc", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=10)

        # Create a Frame for the scrollable area and canvas
        self.canvas_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.canvas = tk.Canvas(self.canvas_frame, bg="#fff")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Load Button
        self.load_button = tk.Button(self.root, text="Load Images", font=("Helvetica", 14), bg="#e10a91", fg="white", command=self.load_images)
        self.load_button.pack(pady=10)

    def load_images(self):
        """Load images from a folder."""
        folder_path = filedialog.askdirectory(title="Select Folder with Images")
        if not folder_path:
            messagebox.showerror("Error", "No folder selected. Exiting...")
            return

        # Get all image files from the selected folder
        supported_formats = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
        self.image_files = [
            os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(supported_formats)
        ]

        # Debugging: print the list of images found
        print("Images found:", self.image_files)

        if not self.image_files:
            messagebox.showerror("Error", "No image files found in the selected folder.")
            return

        # Clear any previous images and load new ones
        self.canvas.delete("all")

        # Display the images in a grid layout
        self.display_images()

    def display_images(self):
        """Display all images in a grid layout inside the canvas."""
        try:
            image_width = 150
            image_height = 150
            padding = 10  # Padding between images

            # Create a frame to hold the images
            image_frame = tk.Frame(self.canvas, bg="#fff")
            self.canvas.create_window((0, 0), window=image_frame, anchor="nw")

            # Grid layout (Number of columns)
            cols = 4

            for idx, image_path in enumerate(self.image_files):
                row = idx // cols
                col = idx % cols

                # Open the image
                image = Image.open(image_path)
                image = image.resize((image_width, image_height), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)

                # Create a label to hold the image and place it in the grid
                image_label = tk.Label(image_frame, image=photo, cursor="hand2")
                image_label.grid(row=row, column=col, padx=padding, pady=padding)

                # Hover effect
                image_label.bind("<Enter>", lambda e, label=image_label: label.config(bg="#e0e0e0"))
                image_label.bind("<Leave>", lambda e, label=image_label: label.config(bg=""))

                image_label.image = photo  # Keep a reference to avoid garbage collection
                image_label.bind("<Button-1>", lambda e, image_path=image_path: self.view_image(image_path))

            # Update the scroll region of the canvas to include all images
            canvas_width = cols * (image_width + padding)
            canvas_height = (len(self.image_files) // cols + (1 if len(self.image_files) % cols > 0 else 0)) * (image_height + padding)
            self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))

        except Exception as e:
            messagebox.showerror("Error", f"Error displaying images: {e}")
            print(f"Error displaying images: {e}")

    def view_image(self, image_path):
        """Open the clicked image in a larger window."""
        try:
            new_window = tk.Toplevel(self.root)
            new_window.title("Image Viewer")
            new_window.geometry("600x600")

            # Load and display the image in the new window
            image = Image.open(image_path)
            image = image.resize((500, 500), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(new_window, image=photo)
            label.pack(pady=20)
            label.image = photo  # Keep a reference to avoid garbage collection

            close_button = tk.Button(new_window, text="Close", bg="#e10a91", font=("Helvetica", 12), command=new_window.destroy)
            close_button.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"Error viewing image: {e}")
            print(f"Error viewing image: {e}")


def run_app():
    root = tk.Tk()
    app = PhotoGalleryApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()
def display_images(self):
    """Display all images in a grid layout inside the canvas."""
    try:
        image_width = 150
        image_height = 150
        padding = 10  # Padding between images

        # Create a frame to hold the images and set the background color to "#ffcedc"
        image_frame = tk.Frame(self.canvas, bg="#ffcedc")
        self.canvas.create_window((0, 0), window=image_frame, anchor="nw")

        # Grid layout (Number of columns)
        cols = 4

        for idx, image_path in enumerate(self.image_files):
            row = idx // cols
            col = idx % cols

            # Open the image
            image = Image.open(image_path)
            image = image.resize((image_width, image_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            # Create a label to hold the image and place it in the grid
            image_label = tk.Label(image_frame, image=photo, cursor="hand2")
            image_label.grid(row=row, column=col, padx=padding, pady=padding)

            # Hover effect
            image_label.bind("<Enter>", lambda e, label=image_label: label.config(bg="#e0e0e0"))
            image_label.bind("<Leave>", lambda e, label=image_label: label.config(bg=""))

            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.bind("<Button-1>", lambda e, image_path=image_path: self.view_image(image_path))

        # Update the scroll region of the canvas to include all images
        canvas_width = cols * (image_width + padding)
        canvas_height = (len(self.image_files) // cols + (1 if len(self.image_files) % cols > 0 else 0)) * (image_height + padding)
        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))

    except Exception as e:
        messagebox.showerror("Error", f"Error displaying images: {e}")
        print(f"Error displaying images: {e}")
