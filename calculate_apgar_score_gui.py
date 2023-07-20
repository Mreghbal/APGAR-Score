import tkinter as tk
from tkinter import messagebox

def calculate_apgar_score():
    try:
        # Get user input for appearance, pulse, grimace, activity, and respiration
        appearance = appearance_entry.get().lower()
        pulse = int(pulse_entry.get())
        grimace = grimace_entry.get().lower()
        activity = activity_entry.get().lower()
        respiration = int(respiration_entry.get())

        # Validate input values
        if appearance not in ["pink", "blue"]:
            raise ValueError("Invalid appearance. Please enter 'pink' or 'blue'.")
        if pulse < 0:
            raise ValueError("Invalid pulse rate. Please enter a non-negative value.")
        if grimace not in ["cough/sneeze", "active motion", "grimace"]:
            raise ValueError("Invalid grimace. Please enter 'cough/sneeze', 'active motion', or 'grimace'.")
        if activity not in ["active motion", "some flexion of extremities"]:
            raise ValueError("Invalid activity. Please enter 'active motion' or 'some flexion of extremities'.")
        if respiration < 0:
            raise ValueError("Invalid respiration rate. Please enter a non-negative value.")

        # Calculate APGAR score
        score = 0
        if appearance == "pink":
            score += 2
        elif appearance == "blue":
            score += 1

        if pulse >= 100:
            score += 2
        elif 60 <= pulse < 100:
            score += 1

        if grimace == "cough/sneeze" or grimace == "active motion":
            score += 2
        elif grimace == "grimace":
            score += 1

        if activity == "active motion":
            score += 2
        elif activity == "some flexion of extremities":
            score += 1

        if respiration >= 30:
            score += 2
        elif 0 <= respiration < 30:
            score += 1

        # Show the result in a message box
        result_text = "APGAR Score Calculation:\n\n"
        result_text += "Appearance: {}\n".format(appearance)
        result_text += "Pulse Rate: {}\n".format(pulse)
        result_text += "Grimace: {}\n".format(grimace)
        result_text += "Activity: {}\n".format(activity)
        result_text += "Respiration Rate: {}\n".format(respiration)
        result_text += "APGAR Score: {}".format(score)
        messagebox.showinfo("APGAR Score Calculation Result", result_text)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("APGAR Score Calculator")

# Create labels and entry fields for appearance, pulse, grimace, activity, and respiration
appearance_label = tk.Label(window, text="Appearance (pink/blue):")
appearance_label.pack()
appearance_entry = tk.Entry(window)
appearance_entry.pack()

pulse_label = tk.Label(window, text="Pulse Rate:")
pulse_label.pack()
pulse_entry = tk.Entry(window)
pulse_entry.pack()

grimace_label = tk.Label(window, text="Grimace (cough/sneeze/active motion/grimace):")
grimace_label.pack()
grimace_entry = tk.Entry(window)
grimace_entry.pack()

activity_label = tk.Label(window, text="Activity (active motion/some flexion of extremities):")
activity_label.pack()
activity_entry = tk.Entry(window)
activity_entry.pack()

respiration_label = tk.Label(window, text="Respiration Rate:")
respiration_label.pack()
respiration_entry = tk.Entry(window)
respiration_entry.pack()

# Create a button to calculate the APGAR score
calculate_button = tk.Button(window, text="Calculate", command=calculate_apgar_score)
calculate_button.pack()

# Run the GUI event loop
window.mainloop()
