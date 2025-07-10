# AMR Robot UI

This project provides a user interface (UI) for an Autonomous Mobile Robot (AMR) system, designed for deployment on a NVIDIA Jetson board with touchscreen support and tested on a Windows laptop. The UI consists of a visually engaging splash screen built with Pygame and a modern, fullscreen menu interface built with PyQt5.

## Features

### Splash Screen:
- Built with Pygame, displays for 5 seconds in fullscreen mode
- Shows animated "AMR TEAM 1" and "Autonomous Mobile Robotics" text with pulsating circles and particle effects
- Exits early with the ESC key

### Main Menu:
- Built with PyQt5, displays in fullscreen mode with a modern dark gradient background
- Features three touch-friendly buttons: "Mapping Mode", "Navigation Mode", and "Debug Mode"
- Buttons have gradient fills, hover effects, and pressed states for a polished look
- Displays a status bar ("AMR Status: Online | Battery: 80%") with a semi-transparent background
- Exits with the ESC key

### System Features:
- Automatic Transition: Seamlessly transitions from splash screen to main menu
- Cross-Platform: Tested on Windows (Python 3.13.2) and designed for NVIDIA Jetson boards

## Requirements

### Software:
- **Python**: 3.13.2 (or 3.12 for broader compatibility)
- **Dependencies**:
  ```bash
  pip install pygame==2.6.1 pyqt5==5.15.11
