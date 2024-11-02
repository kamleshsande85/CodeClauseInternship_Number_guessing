import requests
import tkinter as tk
import webbrowser


def shorten_url_bitly(long_url):
    # Replace with your actual Bitly API token
    access_token = "94b9e5b651ea4fc267070b700b5385d98dd4dbf1"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "long_url": long_url
    }
    url = "https://api-ssl.bitly.com/v4/shorten"
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        return data["link"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def open_link(url):
    webbrowser.open_new_tab(url)


def short_url_process():
    # Example usage
    long_url = entry.get()
    short_url = shorten_url_bitly(long_url)
    if short_url:
        label2.config(text=f"Short URL is :: {short_url}", cursor="hand2")
        label2.bind("<Button-1>", lambda e: open_link(short_url))


def clear_text_box():
    entry.delete(0, tk.END)


root = tk.Tk()
root.geometry("500x200")
root.title("URL shortner")
root.config(bg="#CBDDE6")

frame = tk.Frame(root)
frame.pack()
frame.config(bg="#02B0C0")
label1 = tk.Label(frame, text="Enter url ", bg="#02B0C0")
label1.grid(row=0, column=0)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5)

btnSubmit = tk.Button(frame, text="Submit", width=10,
                      bg="#0E0B07", fg="#F9F7F3", command=short_url_process)
btnSubmit.grid(row=1, column=0, padx=20, pady=10)

btnClear = tk.Button(frame, text="Clear", width=10,
                     bg="#02B0C0", command=clear_text_box)
btnClear.grid(row=1, column=1, pady=10)

label2 = tk.Label(root, text="short url ", cursor="hand2")
label2.pack(pady=20)


root.mainloop()
