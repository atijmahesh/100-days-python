import tkinter as tk
import time

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")

        self.sample_text = (
            "The quick brown fox jumps over the lazy dog. "
            "This sentence contains every letter of the alphabet. "
            "It's often used to test typing speed and keyboard layouts."
        )

        self.time_start = 0
        self.time_elapsed = 0  # Initialize time_elapsed

        self.label_instruction = tk.Label(root, text="Type the following text as quickly as you can:", font=("Arial", 16))
        self.label_instruction.pack(pady=10)

        self.text_display = tk.Text(root, wrap="word", height=6, width=70, font=("Arial", 14), bg="#e0e0e0", padx=10, pady=10)
        self.text_display.insert(tk.END, self.sample_text)
        self.text_display.config(state=tk.DISABLED)
        self.text_display.pack(pady=10)

        self.entry_text = tk.Text(root, wrap="word", height=6, width=70, font=("Arial", 14), padx=10, pady=10)
        self.entry_text.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.button_start = tk.Button(self.button_frame, text="Start", command=self.start_test, font=("Arial", 14), width=10, height=2)
        self.button_start.grid(row=0, column=0, padx=20)

        self.button_submit = tk.Button(self.button_frame, text="Submit", command=self.submit_test, font=("Arial", 14), width=10, height=2)
        self.button_submit.grid(row=0, column=1, padx=20)

        self.label_timer = tk.Label(root, text="Time: 0 seconds", font=("Arial", 14))
        self.label_timer.pack(pady=10)

        self.label_result = tk.Label(root, text="", font=("Arial", 18))
        self.label_result.pack(pady=20)

        self.root.bind("<KeyRelease>", self.update_typing_speed)

    def start_test(self):
        self.entry_text.delete(1.0, tk.END)
        self.entry_text.config(bg="white")
        self.label_result.config(text="")
        self.time_start = time.time()
        self.time_elapsed = 0  # Reset time_elapsed at start
        self.button_start.config(state=tk.DISABLED)
        self.update_timer()

    def update_timer(self):
        self.time_elapsed = time.time() - self.time_start
        self.label_timer.config(text=f"Time: {int(self.time_elapsed)} seconds")
        if self.button_start['state'] == tk.DISABLED:
            self.root.after(1000, self.update_timer)

    def submit_test(self):
        time_end = time.time()
        time_taken = time_end - self.time_start
        typed_text = self.entry_text.get(1.0, tk.END).strip()
        word_count = len(typed_text.split())

        if typed_text != self.sample_text:
            self.label_result.config(text="Typed text doesn't match sample text!", fg="red")
            self.entry_text.config(bg="#ffcccc")
        elif time_taken > 0:
            wpm = (word_count / time_taken) * 60
            self.label_result.config(text=f"Your typing speed is {wpm:.2f} words per minute.", fg="green")
            self.entry_text.config(bg="#ccffcc")
        else:
            self.label_result.config(text="Please start the test first!", fg="red")

        self.button_start.config(state=tk.NORMAL)

    def update_typing_speed(self, event):
        typed_text = self.entry_text.get(1.0, tk.END).strip()
        if typed_text:
            word_count = len(typed_text.split())
            if self.time_elapsed > 0:
                wpm = (word_count / self.time_elapsed) * 60
                self.label_result.config(text=f"Current speed: {wpm:.2f} WPM", fg="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
