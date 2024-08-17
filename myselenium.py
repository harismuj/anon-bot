import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Fungsi login
def login(email, password):
    # URL login
    login_url = 'https://cat.binacikalcibubur.id/'

    # Buka halaman login
    driver.get(login_url)

    # Tunggu hingga elemen email dan password muncul
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))

    # Isi formulir login
    email_input.send_keys(email)
    password_input.send_keys(password)

    # Klik tombol login
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Login")]')))
    login_button.click()

    # Tunggu hingga halaman setelah login dimuat sepenuhnya
    WebDriverWait(driver, 10).until(EC.url_changes(login_url))

    # Tampilkan URL setelah login
    new_url = driver.current_url
    print("URL setelah login:", new_url)

    # Selanjutnya, Anda dapat menambahkan logika untuk menjalankan tugas-tugas yang diinginkan
    while True:
        print("Tugas yang diinginkan sedang dijalankan...")
# Tambahkan tugas yang diinginkan di sini

        # Tidur selama beberapa detik sebelum menjalankan tugas berikutnya
        time.sleep(5)  # Misalnya, tugas dijalankan setiap 5 detik

    # Tutup browser
    driver.quit()

# Fungsi untuk menginisialisasi ChromeDriver dan melakukan login
def on_login_click():
    # Instantiate the ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--kiosk')
    global driver
    driver = webdriver.Chrome(options=options)

    # Tampilkan URL sebelum login
    global url
    url = driver.current_url
    print("URL sebelum login:", url)

    # Trigger the login function with email and password inputs
    email = email_input.get()
    password = password_input.get()
    login(email, password)

# Fungsi untuk menutup browser
def on_close_click():
    if driver is not None:
        driver.quit()

def logout():
    # Find the logout button and click it
    logout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Log out')]")))
    logout_button.click()

    # Quit the driver
    driver.quit()

# Tampilkan tampilan tkinter
window = tk.Tk()

# Tampilkan label dan input email dan password
email_label = tk.Label(window, text="Email:")
email_label.grid(row=0, column=0)
email_input = tk.Entry(window, width=30)
email_input.grid(row=0, column=1)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0)
password_input = tk.Entry(window, width=30, show='*')
password_input.grid(row=1, column=1)

# Tombol untuk login
login_button = tk.Button(window, text="Login", command=on_login_click)
login_button.grid(row=2, column=0, columnspan=2)

# Tombol untukmenutup browser
close_button = tk.Button(window, text="Close", command=on_close_click)
close_button.grid(row=3, column=0, columnspan=2)

# Start the tkinter event loop
window.mainloop()