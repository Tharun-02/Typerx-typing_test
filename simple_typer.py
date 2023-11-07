import tkinter as tk
import random
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x350")
        self.frame = tk.Frame(self.root)
        self.strings = ["The quick brown fox jumps over the lazy dog"
                    "The sky is clear and blue today",
                    "I love to eat pizza and ice cream",
                    "The cat sat on the mat",
                    "The tree stood tall in the forest",
                    "The sun shone brightly on the beach"]
        self.text = random.choice(self.strings)
        self.texts = open("text.txt", "r").read().split("\n")
        self.user_input = tk.StringVar()
        self.time_start = 0

        self.create_widgets()

    def create_widgets(self):
        # Text to type
        self.text_label = tk.Label(self.frame, text=self.text, font=("Helvetica", 14))
        self.text_label.grid(row=0, column=0,columnspan=2, padx=5, pady=10)

        # User input entry
        self.entry = tk.Entry(self.frame, textvariable=self.user_input, width=40, font=("Montserrat", 16))
        self.entry.grid(row=1, column=0,columnspan=2, padx=5, pady=10)

        # Start button
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_test)
        self.start_button.grid(row=2, column=0, pady=10)
        
        
        # Exit button
        self.exit_button = tk.Button(self.frame, text="Exit", command = root.destroy)
        self.exit_button.grid(row=2, column=1,columnspan=2, padx=5, pady=10)

        # Result display
        self.result_label = tk.Label(self.frame, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        
        self.frame.pack(expand = True)

    def start_test(self):
        self.time_start = time.time()
        self.user_input.set("")  # Clear the input field
        self.entry.config(state="normal")  # Enable input field
        self.start_button.config(state="disabled")  # Disable start button

        self.root.bind('<Return>', self.stop_test)  # Bind Enter key to stop the test
    

    def stop_test(self, event):
        self.entry.config(state="disabled")  # Disable input field
        self.root.unbind('<Return>')  # Unbind Enter key
        self.start_button.config(state="normal")  # Enable start button

        elapsed_time = time.time() - self.time_start
        words = len(self.text.split())
        wpm = words / elapsed_time * 60
        wps = wpm / 60
        
        accuracy = sum(a == b for a, b in zip(self.text, self.user_input.get())) / len(self.text) * 100

        result_text = f"Time: {elapsed_time:.2f} seconds \n Words per sec (WPS): {wps:.2f} \n Words per minute (WPM): {wpm:.2f} \n Accuracy: {accuracy:.2f}%"
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
