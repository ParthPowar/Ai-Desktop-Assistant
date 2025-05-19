import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
from triss_assistant import TrissAssistant

class TrissAssistantUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Triss Assistant UI")
        self.root.geometry("600x450")

        self.assistant = TrissAssistant()

        # Greeting on startup
        greeting = self.assistant.get_greeting()
        # self.assistant.speak(greeting)  # Removed synchronous speak here

        # Create UI components
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=15)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Status label to show listening or idle state
        self.status_label = tk.Label(root, text="Status: Idle", font=("Arial", 12), fg="blue")
        self.status_label.pack(padx=10, pady=(0,5), anchor='w')

        # Remove entry field, add button to start voice input
        # self.entry = tk.Entry(root, font=("Arial", 14))
        # self.entry.pack(padx=10, pady=(0,10), fill=tk.X)
        # self.entry.bind("<Return>", self.process_input)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(padx=10, pady=(0,10), fill=tk.X)

        # Remove listen button for automatic listening
        # self.listen_button = tk.Button(self.button_frame, text="Start Listening", command=self.start_listening)
        # self.listen_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0,5))

        self.speak_button = tk.Button(self.button_frame, text="Speak Response", command=self.speak_response)
        self.speak_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5,0))

        self.current_response = ""

        # Display greeting in text area
        self.append_text("Assistant: " + greeting + "\n")

        # Schedule greeting speech after UI is shown
        self.root.after(100, self.speak_greeting)
        # Remove automatic start of listening here to start only after greeting speech
        # self.root.after(500, self.start_listening)

    def speak_greeting(self):
        greeting = self.assistant.get_greeting()

        def speak():
            self.assistant.speak(greeting)

        self.greeting_thread = threading.Thread(target=speak)
        self.greeting_thread.start()

        # Start polling to check if greeting speech is done
        self.check_greeting_done()

    def check_greeting_done(self):
        if self.greeting_thread.is_alive():
            # Greeting still speaking, check again after 100ms
            self.root.after(100, self.check_greeting_done)
        else:
            # Greeting finished, start listening
            self.start_listening()

    def append_text(self, text):
        # Schedule UI update on main thread
        def update_text():
            self.text_area.config(state='normal')
            self.text_area.insert(tk.END, text)
            self.text_area.see(tk.END)
            self.text_area.config(state='disabled')
        self.root.after(0, update_text)

    def start_listening(self):
        # Update status label
        self.status_label.config(text="Status: Listening...")
        # self.listen_button.config(state='disabled')
        threading.Thread(target=self.listen_and_process).start()

    def listen_and_process(self):
        query = self.assistant.take_command()
        if query:
            self.append_text(f"You (voice): {query}\n")
            self.handle_command(query)
        else:
            self.append_text("No voice input detected.\n")
        # Reset status label and button
        self.status_label.config(text="Status: Idle")
        # self.listen_button.config(state='normal')

    def handle_command(self, query):
        result = self.assistant.process_command(query)

        response = result.get("response", "")
        action = result.get("action", None)

        self.current_response = response
        self.append_text("Assistant: " + response + "\n")

        # Speak the response automatically
        self.assistant.speak(response)

        # Execute action if callable
        if callable(action):
            try:
                action()
            except Exception as e:
                self.append_text(f"Error executing action: {str(e)}\n")

        # Handle special actions
        if action == "exit":
            self.append_text("Exiting application...\n")
            self.root.quit()
        else:
            # Automatically start listening again after handling command
            self.start_listening()

    def speak_response(self):
        if self.current_response:
            threading.Thread(target=self.assistant.speak, args=(self.current_response,)).start()
        else:
            messagebox.showinfo("Info", "No response to speak.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrissAssistantUI(root)
    root.mainloop()
