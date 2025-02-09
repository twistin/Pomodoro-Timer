# Pomodoro Timer Professional

Pomodoro Timer Professional is a desktop application that helps you to manage your time using the Pomodoro technique. The application is developed in Python using Tkinter for the graphical interface and Pygame for sound playback.

<img title="" src="file:///Users/sdcarr/Desktop/pomodoro/pomodoro_project/resources/images/logo.png" alt="" data-align="center" width="258">

## Features

- Friendly graphical interface.
- Pomodoro timer with working sessions and breaks.
- Playing sounds to indicate the start and end of sessions.
- Editing of task schedule.
- Notifications on completion of all tasks.

## Requirements

- Python 3.x
- Additional libraries:
  - `tkinter`
  - `Pillow`
  - `pygame`
  - `PyInstaller` (to create the executable)

## Installation

1. Clone the repository on your local machine:
   
   ```sh
   git clone https://github.com/tu_usuario/pomodoro_timer_profesional.git
   cd pomodoro_timer_professional
   ```

2. Install the necessary dependencies:
   
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   
   ```sh
   python pomodoro_app.py
   ```

## Create an executable

To turn the application into an executable, you can use PyInstaller. Follow these steps:

1. Install PyInstaller:
   
   ```sh
   pip install pyinstaller
   ```

2. Create the executable:
   
   ```sh
   pyinstaller --onefile --windowed pomodoro_app.py
   ```

3. The executable will be generated in the ``dist`` folder.

## Usage

1. When you start the application, you will see the main screen with the logo and the timer.
2. You can start, stop and 
