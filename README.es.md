# Pomodoro Timer Profesional

Pomodoro Timer Profesional es una aplicación de escritorio que te ayuda a gestionar tu tiempo utilizando la técnica Pomodoro. La aplicación está desarrollada en Python utilizando Tkinter para la interfaz gráfica y Pygame para la reproducción de sonidos.

<img title="" src="file:///Users/sdcarr/Desktop/pomodoro/pomodoro_project/resources/images/logo.png" alt="" data-align="center" width="245">

## Características

- Interfaz gráfica amigable.
- Temporizador Pomodoro con sesiones de trabajo y descansos.
- Reproducción de sonidos para indicar el inicio y fin de las sesiones.
- Edición del horario de tareas.
- Notificaciones al completar todas las tareas.

## Requisitos

- Python 3.x
- Bibliotecas adicionales:
  - `tkinter`
  - `Pillow`
  - `pygame`
  - `PyInstaller` (para crear el ejecutable)

## Instalación

1. Clona el repositorio en tu máquina local:
   
   ```sh
   git clone https://github.com/tu_usuario/pomodoro_timer_profesional.git
   cd pomodoro_timer_profesional
   ```

2. Instala las dependencias necesarias:
   
   ```sh
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   
   ```sh
   python pomodoro_app.py
   ```

## Crear un ejecutable

Para convertir la aplicación en un ejecutable, puedes usar PyInstaller. Sigue estos pasos:

1. Instala PyInstaller:
   
   ```sh
   pip install pyinstaller
   ```

2. Crea el ejecutable:
   
   ```sh
   pyinstaller --onefile --windowed pomodoro_app.py
   ```

3. El ejecutable se generará en la carpeta `dist`.

## Uso

1. Al iniciar la aplicación, verás la pantalla principal con el logo y el temporizador.
2. Puedes iniciar, detener y reiniciar el temporizador utilizando los botones correspondientes.
3. Para editar el horario de tareas, haz clic en el botón "✎ Editar Horario".
4. Al completar todas las tareas, recibirás una notificación.

## Estructura del Proyecto

- `pomodoro_app.py`: El archivo principal de la aplicación.
- `resources/`: Carpeta que contiene las imágenes y sonidos utilizados en la aplicación.
- `README.md`: Este archivo.
- `requirements.txt`: Lista de dependencias necesarias para la aplicación.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, por favor abre un issue o un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

---

¡Gracias por usar Pomodoro Timer Profesional! Esperamos que te ayude a ser más productivo.