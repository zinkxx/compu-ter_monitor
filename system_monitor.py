import psutil
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Monitorü")
        self.root.geometry("800x600")

        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')

        # Özelleştirilmiş tema renkleri
        self.style.configure('TLabel', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12), padding=5)
        self.style.configure('TFrame', background='#f0f0f0')

        self.is_dark_mode = False

        self.create_widgets()
        self.update_stats()

    def create_widgets(self):
        # Menü ve Araç Çubuğu
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Dosya", menu=file_menu)
        file_menu.add_command(label="Notları Kaydet", command=self.save_notes)
        file_menu.add_command(label="Notları Yükle", command=self.load_notes)
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", command=self.root.quit)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Görünüm", menu=view_menu)
        view_menu.add_command(label="Karanlık/Aydınlık Modu", command=self.toggle_mode)

        # Sistem Bilgileri
        info_frame = ttk.Frame(self.root, padding="10 10 10 10")
        info_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.battery_label = ttk.Label(info_frame, text="Batarya Durumu: Yükleniyor...")
        self.battery_label.grid(row=0, column=0, pady=5, padx=10, sticky="w")

        self.ram_label = ttk.Label(info_frame, text="RAM Kullanımı: Yükleniyor...")
        self.ram_label.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        self.disk_label = ttk.Label(info_frame, text="Disk Kullanımı: Yükleniyor...")
        self.disk_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        self.cpu_label = ttk.Label(info_frame, text="CPU Kullanımı: Yükleniyor...")
        self.cpu_label.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        # Notlar
        self.notes_label = ttk.Label(info_frame, text="Notlar:", font=('Arial', 14, 'bold'))
        self.notes_label.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        self.notes_text = tk.Text(info_frame, height=5, width=50, font=('Arial', 12), wrap=tk.WORD)
        self.notes_text.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        # Grafikler
        graph_frame = ttk.Frame(self.root, padding="10 10 10 10")
        graph_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(6, 4))
        self.fig.tight_layout(pad=3.0)

        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_stats(self):
        battery = psutil.sensors_battery()
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        cpu = psutil.cpu_percent(interval=1)

        self.battery_label.config(text=f"Batarya Durumu: {battery.percent}%")
        self.ram_label.config(text=f"RAM Kullanımı: {ram.percent}%")
        self.disk_label.config(text=f"Disk Kullanımı: {disk.percent}%")
        self.cpu_label.config(text=f"CPU Kullanımı: {cpu}%")

        # Grafik Verileri Güncelleme
        self.ax1.clear()
        self.ax1.set_title("CPU Kullanımı")
        self.ax1.set_ylabel("Yüzde")
        self.ax1.bar(["CPU"], [cpu], color='#5DADE2')

        self.ax2.clear()
        self.ax2.set_title("RAM Kullanımı")
        self.ax2.set_ylabel("Yüzde")
        self.ax2.bar(["RAM"], [ram.percent], color='#58D68D')

        self.canvas.draw()

        self.root.after(1000, self.update_stats)

    def save_notes(self):
        notes = self.notes_text.get("1.0", tk.END)
        with open("notes.txt", "w") as file:
            file.write(notes)
        messagebox.showinfo("Bilgi", "Notlar kaydedildi!")

    def load_notes(self):
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()
                self.notes_text.delete("1.0", tk.END)
                self.notes_text.insert(tk.END, notes)
        except FileNotFoundError:
            messagebox.showwarning("Uyarı", "Notlar dosyası bulunamadı!")

    def toggle_mode(self):
        if self.is_dark_mode:
            self.root.config(bg="white")
            self.style.configure('TLabel', background="white", foreground="black")
            self.style.configure('TButton', background="white", foreground="black")
            self.style.configure('TFrame', background='#f0f0f0')
            self.notes_text.config(bg="white", fg="black")
            self.is_dark_mode = False
        else:
            self.root.config(bg="black")
            self.style.configure('TLabel', background="black", foreground="white")
            self.style.configure('TButton', background="black", foreground="white")
            self.style.configure('TFrame', background='#333333')
            self.notes_text.config(bg="black", fg="white")
            self.is_dark_mode = True

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()
import psutil
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Monitorü")
        self.root.geometry("800x600")

        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')

        # Özelleştirilmiş tema renkleri
        self.style.configure('TLabel', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12), padding=5)
        self.style.configure('TFrame', background='#f0f0f0')

        self.is_dark_mode = False

        self.create_widgets()
        self.update_stats()

    def create_widgets(self):
        # Menü ve Araç Çubuğu
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Dosya", menu=file_menu)
        file_menu.add_command(label="Notları Kaydet", command=self.save_notes)
        file_menu.add_command(label="Notları Yükle", command=self.load_notes)
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", command=self.root.quit)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Görünüm", menu=view_menu)
        view_menu.add_command(label="Karanlık/Aydınlık Modu", command=self.toggle_mode)

        # Sistem Bilgileri
        info_frame = ttk.Frame(self.root, padding="10 10 10 10")
        info_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.battery_label = ttk.Label(info_frame, text="Batarya Durumu: Yükleniyor...")
        self.battery_label.grid(row=0, column=0, pady=5, padx=10, sticky="w")

        self.ram_label = ttk.Label(info_frame, text="RAM Kullanımı: Yükleniyor...")
        self.ram_label.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        self.disk_label = ttk.Label(info_frame, text="Disk Kullanımı: Yükleniyor...")
        self.disk_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        self.cpu_label = ttk.Label(info_frame, text="CPU Kullanımı: Yükleniyor...")
        self.cpu_label.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        # Notlar
        self.notes_label = ttk.Label(info_frame, text="Notlar:", font=('Arial', 14, 'bold'))
        self.notes_label.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        self.notes_text = tk.Text(info_frame, height=5, width=50, font=('Arial', 12), wrap=tk.WORD)
        self.notes_text.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        # Grafikler
        graph_frame = ttk.Frame(self.root, padding="10 10 10 10")
        graph_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(6, 4))
        self.fig.tight_layout(pad=3.0)

        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_stats(self):
        battery = psutil.sensors_battery()
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        cpu = psutil.cpu_percent(interval=1)

        self.battery_label.config(text=f"Batarya Durumu: {battery.percent}%")
        self.ram_label.config(text=f"RAM Kullanımı: {ram.percent}%")
        self.disk_label.config(text=f"Disk Kullanımı: {disk.percent}%")
        self.cpu_label.config(text=f"CPU Kullanımı: {cpu}%")

        # Grafik Verileri Güncelleme
        self.ax1.clear()
        self.ax1.set_title("CPU Kullanımı")
        self.ax1.set_ylabel("Yüzde")
        self.ax1.bar(["CPU"], [cpu], color='#5DADE2')

        self.ax2.clear()
        self.ax2.set_title("RAM Kullanımı")
        self.ax2.set_ylabel("Yüzde")
        self.ax2.bar(["RAM"], [ram.percent], color='#58D68D')

        self.canvas.draw()

        self.root.after(1000, self.update_stats)

    def save_notes(self):
        notes = self.notes_text.get("1.0", tk.END)
        with open("notes.txt", "w") as file:
            file.write(notes)
        messagebox.showinfo("Bilgi", "Notlar kaydedildi!")

    def load_notes(self):
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()
                self.notes_text.delete("1.0", tk.END)
                self.notes_text.insert(tk.END, notes)
        except FileNotFoundError:
            messagebox.showwarning("Uyarı", "Notlar dosyası bulunamadı!")

    def toggle_mode(self):
        if self.is_dark_mode:
            self.root.config(bg="white")
            self.style.configure('TLabel', background="white", foreground="black")
            self.style.configure('TButton', background="white", foreground="black")
            self.style.configure('TFrame', background='#f0f0f0')
            self.notes_text.config(bg="white", fg="black")
            self.is_dark_mode = False
        else:
            self.root.config(bg="black")
            self.style.configure('TLabel', background="black", foreground="white")
            self.style.configure('TButton', background="black", foreground="white")
            self.style.configure('TFrame', background='#333333')
            self.notes_text.config(bg="black", fg="white")
            self.is_dark_mode = True

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()
