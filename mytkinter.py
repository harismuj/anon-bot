import tkinter as tk
import requests

def test_endpoint():
    url = entry_url.get()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result_label.config(text=f"Endpoint is reachable. Response: {response.text}", fg="green")
        else:
            result_label.config(text=f"Failed to reach endpoint (Status code: {response.status_code})", fg="red")
    except requests.ConnectionError:
        result_label.config(text="Failed to connect to the endpoint", fg="red")

# Create the main window
root = tk.Tk()
root.title("Endpoint Tester")

# Create a frame to hold widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create URL entry
label_url = tk.Label(frame, text="Enter Endpoint URL:")
label_url.grid(row=0, column=0, sticky="w")
entry_url = tk.Entry(frame, width=40)
entry_url.grid(row=0, column=1, padx=10)

# Create button to test endpoint
test_button = tk.Button(frame, text="Test Endpoint", command=test_endpoint)
test_button.grid(row=1, columnspan=2, pady=10)

# Create label to display result
result_label = tk.Label(frame, text="", fg="black")
result_label.grid(row=2, columnspan=2)

# Run the GUI
root.mainloop()
