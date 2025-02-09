import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk, ImageDraw
import os
import pygame

# Definición de colores
COLORS = {
    "background": "#2E3440",
    "foreground": "#D8DEE9",
    "button_bg": "#4C566A",
    "button_fg": "#ECEFF4",
    "active_bg": "#5E81AC",
    "listbox_bg": "#3B4252",
    "listbox_fg": "#E5E9F0",
}


class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temporizador Pomodoro Profesional")
        self.root.geometry("700x600")
        self.root.configure(bg=COLORS["background"])
        self.colors = COLORS
        self.tick_sound_playing = False

        # Inicializar pygame y cargar los sonidos
        pygame.mixer.init()
        self.load_sounds()

        # Cargar el logotipo
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(
                script_dir, 'resources', 'images', '/Users/sdcarr/Desktop/pomodoro/pomodoro_project/resources/images/logo.png')
            self.logo_image = Image.open(logo_path)
            self.logo_image = self.create_circular_logo(self.logo_image, 100)
            self.logo = ImageTk.PhotoImage(self.logo_image)
        except FileNotFoundError:
            print(f"Logotipo no encontrado en: {logo_path}")
            self.logo = None
        except Exception as e:
            print(f"Error al cargar el logotipo: {str(e)}")
            self.logo = None

        self.setup_ui()
        self.initialize_schedule()

    def load_sounds(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            tick_sound_path = os.path.normpath(os.path.join(
                script_dir, 'resources', 'sounds', '/Users/sdcarr/Desktop/pomodoro/pomodoro_project/resources/sounds /tick.wav'))
            end_break_sound_path = os.path.normpath(os.path.join(
                script_dir, 'resources', 'sounds', '/Users/sdcarr/Desktop/pomodoro/pomodoro_project/resources/sounds /end_break.wav'))
            end_task_sound_path = os.path.normpath(os.path.join(
                script_dir, 'resources', 'sounds', '/Users/sdcarr/Desktop/pomodoro/pomodoro_project/resources/sounds /end_task.wav'))

            if not os.path.exists(tick_sound_path):
                raise FileNotFoundError(
                    f"Archivo no encontrado: {tick_sound_path}")
            if not os.path.exists(end_break_sound_path):
                raise FileNotFoundError(
                    f"Archivo no encontrado: {end_break_sound_path}")
            if not os.path.exists(end_task_sound_path):
                raise FileNotFoundError(
                    f"Archivo no encontrado: {end_task_sound_path}")

            self.tick_sound = pygame.mixer.Sound(tick_sound_path)
            self.end_break_sound = pygame.mixer.Sound(end_break_sound_path)
            self.end_task_sound = pygame.mixer.Sound(end_task_sound_path)
            print(
                f"Sonidos cargados correctamente:\n{tick_sound_path}\n{end_break_sound_path}\n{end_task_sound_path}")
        except Exception as e:
            print(f"Error al cargar sonidos: {str(e)}")
            self.tick_sound = None
            self.end_break_sound = None
            self.end_task_sound = None

    def play_tick_sound(self):
        """Inicia el sonido del tick en loop"""
        if self.tick_sound and not self.tick_sound_playing:
            self.tick_sound.set_volume(0.3)
            self.tick_sound.play(loops=-1)
            self.tick_sound_playing = True

    def stop_tick_sound(self):
        """Detiene el sonido del tick"""
        if self.tick_sound and self.tick_sound_playing:
            self.tick_sound.stop()
            self.tick_sound_playing = False

    def start_timer(self):
        """Inicia el temporizador y el sonido del tick"""
        if not self.is_running:
            if not self.schedule:  # Verificar si no hay tareas
                messagebox.showinfo(
                    "Sin tareas", "No hay tareas configuradas. Añade tareas para comenzar.")
                return
            self.is_running = True
            self.play_tick_sound()
            self.update_timer()

    def update_timer(self):
        """Actualiza el temporizador cada segundo"""
        if self.is_running:
            if self.time_left > 0:
                self.time_left -= 1
                self.label.config(text=self.format_time(self.time_left))
                self.root.after(1000, self.update_timer)
            else:
                self.stop_tick_sound()
                self.next_step()

    def stop_timer(self):
        """Detiene el temporizador y el sonido"""
        if self.is_running:
            self.is_running = False
            self.stop_tick_sound()

    def next_step(self):
        """Maneja la transición entre tareas y pomodoros"""
        self.stop_tick_sound()
        if not self.schedule:  # Verificar si no hay tareas
            self.stop_timer()
            return

        current_task = self.schedule[self.current_task_index]
        if current_task.get("is_break", False):
            # Reproducir sonido de fin de descanso
            if self.end_break_sound:
                self.end_break_sound.play()
        else:
            # Reproducir sonido de fin de tarea
            if self.end_task_sound:
                self.end_task_sound.play()

        self.move_to_next_task()

    def move_to_next_task(self):
        self.current_task_index += 1
        if self.current_task_index < len(self.schedule):
            self.time_left = self.schedule[self.current_task_index]["duration"]
            self.task_label.config(
                text=self.schedule[self.current_task_index]["task"])
            self.update_schedule_listbox()
            self.root.after(1000, self.update_timer)
        else:
            self.stop_timer()

    def create_circular_logo(self, image, size):
        """Crear una imagen circular"""
        image = image.resize((size, size), Image.LANCZOS)
        mask = Image.new('L', (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        output = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        output.paste(image, (0, 0), mask)
        return output

    def setup_ui(self):
        """Configurar la interfaz de usuario"""
        self.main_frame = tk.Frame(self.root, bg=self.colors["background"])
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        if self.logo:
            self.logo_label = tk.Label(
                self.main_frame, image=self.logo, bg=self.colors["background"])
            self.logo_label.pack(pady=10)

        self.label = tk.Label(self.main_frame, text="00:00", font=(
            "Helvetica", 48), bg=self.colors["background"], fg=self.colors["foreground"])
        self.label.pack(pady=20)

        self.task_label = tk.Label(self.main_frame, text="No hay tareas", font=(
            "Helvetica", 24), bg=self.colors["background"], fg=self.colors["foreground"])
        self.task_label.pack(pady=10)

        self.create_buttons()
        self.create_schedule_list()

    def create_buttons(self):
        self.button_frame = tk.Frame(
            self.main_frame, bg=self.colors["background"])
        self.button_frame.pack(pady=10)

        button_styles = [
            {
                "text": "▶ Iniciar",
                "command": self.start_timer,
                "bg": "#A3BE8C",
                "fg": "#2E3440",
                "hover_bg": "#8FAF7C",
                "hover_fg": "#2E3440"
            },
            {
                "text": "⏸ Detener",
                "command": self.stop_timer,
                "bg": "#BF616A",
                "fg": "#2E3440",
                "hover_bg": "#AF515A",
                "hover_fg": "#2E3440"
            },
            {
                "text": "✎ Editar Horario",
                "command": self.edit_schedule,
                "bg": "#5E81AC",
                "fg": "#2E3440",
                "hover_bg": "#4E719C",
                "hover_fg": "#2E3440"
            },
            {
                "text": "🔄 Reiniciar",
                "command": self.reset_schedule,
                "bg": "#D08770",
                "fg": "#2E3440",
                "hover_bg": "#B07660",
                "hover_fg": "#2E3440"
            }
        ]

        for style in button_styles:
            button = tk.Button(
                self.button_frame,
                text=style["text"],
                command=style["command"],
                font=("Helvetica", 14),
                width=12,
                relief=tk.RAISED,
                borderwidth=2,
                cursor="hand2"
            )
            button.configure(
                bg=style["bg"],
                fg=style["fg"],
                activebackground=style["hover_bg"],
                activeforeground=style["hover_fg"]
            )
            button.pack(side=tk.LEFT, padx=10)

    def create_schedule_list(self):
        self.schedule_frame = tk.Frame(
            self.main_frame, bg=self.colors["background"])
        self.schedule_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        self.schedule_label = tk.Label(self.schedule_frame, text="Cronograma", font=(
            "Helvetica", 18), bg=self.colors["background"], fg=self.colors["foreground"])
        self.schedule_label.pack()

        self.schedule_listbox = tk.Listbox(self.schedule_frame, font=(
            "Helvetica", 12), bg=self.colors["listbox_bg"], fg=self.colors["listbox_fg"], selectbackground=self.colors["active_bg"])
        self.schedule_listbox.pack(fill=tk.BOTH, expand=True)

    def initialize_schedule(self):
        """Inicializa la lista de tareas vacía"""
        self.schedule = []
        self.current_task_index = 0
        self.time_left = 0
        self.is_running = False
        self.update_schedule_listbox()

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02}:{seconds:02}"

    def edit_schedule(self):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Editar Horario")
        edit_window.geometry("400x300")
        edit_window.configure(bg=self.colors["background"])

        edit_frame = tk.Frame(edit_window, bg=self.colors["background"])
        edit_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(edit_frame, text="Editar Tareas", font=("Helvetica", 18),
                 bg=self.colors["background"], fg=self.colors["foreground"]).pack(pady=10)

        self.edit_listbox = tk.Listbox(edit_frame, font=(
            "Helvetica", 12), bg=self.colors["listbox_bg"], fg=self.colors["listbox_fg"], selectbackground=self.colors["active_bg"])
        self.edit_listbox.pack(fill=tk.BOTH, expand=True)

        if not self.schedule:
            self.edit_listbox.insert(tk.END, "No hay tareas configuradas")
        else:
            for task in self.schedule:
                self.edit_listbox.insert(
                    tk.END, f"{task['task']} - {self.format_time(task['duration'])}")

        button_frame = tk.Frame(edit_frame, bg=self.colors["background"])
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="➕ Añadir tarea", command=self.add_task, bg=self.colors["button_bg"], fg=self.colors["button_fg"], font=(
            "Helvetica", 12), activebackground=self.colors["active_bg"]).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="➖ Eliminar tarea", command=self.remove_task, bg=self.colors["button_bg"], fg=self.colors["button_fg"], font=(
            "Helvetica", 12), activebackground=self.colors["active_bg"]).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="💾 Guardar cambios", command=lambda: self.save_changes(edit_window), bg=self.colors["button_bg"], fg=self.colors["button_fg"], font=(
            "Helvetica", 12), activebackground=self.colors["active_bg"]).pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task_name = simpledialog.askstring(
            "Añadir tarea", "Nombre de la tarea:")
        if task_name:
            task_duration = simpledialog.askinteger(
                "Añadir tarea", "Duración (minutos):", minvalue=1, maxvalue=120)
            if task_duration:
                is_break = messagebox.askyesno(
                    "Tipo de tarea", "¿Es esta tarea un descanso?")
                self.schedule.append({
                    "task": task_name,
                    "duration": task_duration * 60,
                    "is_break": is_break
                })
                self.edit_listbox.insert(
                    tk.END, f"{task_name} - {self.format_time(task_duration * 60)}")

    def remove_task(self):
        selected_index = self.edit_listbox.curselection()
        if selected_index:
            self.schedule.pop(selected_index[0])
            self.edit_listbox.delete(selected_index)

    def save_changes(self, edit_window):
        self.update_schedule_listbox()
        edit_window.destroy()

    def reset_schedule(self):
        self.initialize_schedule()
        self.update_schedule_listbox()
        self.stop_timer()
        self.label.config(text="00:00")
        self.task_label.config(text="No hay tareas")

    def update_schedule_listbox(self):
        self.schedule_listbox.delete(0, tk.END)
        if not self.schedule:
            self.schedule_listbox.insert(tk.END, "No hay tareas configuradas")
        else:
            for i, task in enumerate(self.schedule):
                task_text = f"{task['task']} - {self.format_time(task['duration'])}"
                if i == self.current_task_index:
                    task_text = "➤ " + task_text
                self.schedule_listbox.insert(tk.END, task_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
