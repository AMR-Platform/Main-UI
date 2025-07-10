#!/usr/bin/env python3
import pygame
import sys
import time
import math
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

# --- Splash Screen (Pygame) ---
def run_splash_screen():
    # Set SDL video driver for Windows
    os.environ['SDL_VIDEODRIVER'] = 'x11'  # Use Windows driver
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Hide pygame welcome message
    os.environ['DBUS_FATAL_WARNINGS'] = '0'  # Prevent D-Bus warnings (not needed on Windows)

    # Initialize pygame
    pygame.display.init()
    pygame.font.init()

    # Get display info
    try:
        info = pygame.display.Info()
        WIDTH, HEIGHT = info.current_w, info.current_h
    except:
        WIDTH, HEIGHT = 1920, 1080  # Fallback resolution

    # Setup fullscreen display
    try:
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.NOFRAME)
    except pygame.error:
        try:
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        except pygame.error:
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("AMR TEAM 1")

    # Colors
    BACKGROUND = (0, 0, 0)  # Black
    TEXT_COLOR = (255, 255, 255)  # White
    ACCENT_COLOR = (0, 120, 255)  # Blue

    # Clock and animation settings
    clock = pygame.time.Clock()
    FPS = 60
    start_time = time.time()
    duration = 5.0  # seconds

    # Font setup
    try:
        main_font = pygame.font.Font(None, min(200, HEIGHT // 5))
        sub_font = pygame.font.Font(None, min(60, HEIGHT // 15))
    except pygame.error:
        fonts = pygame.font.get_fonts()
        if fonts:
            main_font = pygame.font.SysFont(fonts[0], min(200, HEIGHT // 5))
            sub_font = pygame.font.SysFont(fonts[0], min(60, HEIGHT // 15))
        else:
            print("Fatal error: Cannot initialize fonts")
            pygame.quit()
            sys.exit(1)

    # Main animation loop
    running = True
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False

            # Calculate animation time
            current_time = time.time()
            elapsed = current_time - start_time
            if elapsed >= duration:
                running = False
                continue

            # Animation progress
            progress = min(elapsed / duration, 1.0)

            # Clear screen
            screen.fill(BACKGROUND)

            # Draw animated background circles
            center_x, center_y = WIDTH // 2, HEIGHT // 2
            for i in range(5):
                radius = int(min(WIDTH, HEIGHT) * 0.4 * (0.6 + 0.4 * math.sin(progress * math.pi * 2 + i * 0.5)))
                thickness = max(1, int(4 + 2 * math.sin(progress * math.pi * 3)))
                pygame.draw.circle(screen, ACCENT_COLOR, (center_x, center_y), radius, thickness)

            # Text animations
            text_scale = 1.0 + 0.05 * math.sin(progress * math.pi * 4)

            # Main title
            if progress < 0.3:
                alpha = int(255 * (progress / 0.3))
                main_text = main_font.render("AMR TEAM 1", True, TEXT_COLOR)
                main_rect = main_text.get_rect(center=(center_x, center_y))
                temp = pygame.Surface(main_text.get_size(), pygame.SRCALPHA)
                temp.blit(main_text, (0, 0))
                temp.set_alpha(alpha)
                screen.blit(temp, main_rect)
            elif progress > 0.8:
                alpha = int(255 * (1 - (progress - 0.8) / 0.2))
                main_text = main_font.render("AMR TEAM 1", True, TEXT_COLOR)
                main_rect = main_text.get_rect(center=(center_x, center_y))
                temp = pygame.Surface(main_text.get_size(), pygame.SRCALPHA)
                temp.blit(main_text, (0, 0))
                temp.set_alpha(alpha)
                screen.blit(temp, main_rect)
            else:
                main_text = main_font.render("AMR TEAM 1", True, TEXT_COLOR)
                text_width, text_height = main_text.get_size()
                scaled_width, scaled_height = int(text_width * text_scale), int(text_height * text_scale)
                if abs(text_scale - 1.0) > 0.01:
                    try:
                        main_text = pygame.transform.smoothscale(main_text, (scaled_width, scaled_height))
                    except:
                        pass
                main_rect = main_text.get_rect(center=(center_x, center_y))
                screen.blit(main_text, main_rect)

            # Subtitle
            if progress > 0.2 and progress < 0.9:
                subtitle_alpha = int(255 * min((progress - 0.2) / 0.2, 1.0))
                if progress > 0.7:
                    subtitle_alpha = int(subtitle_alpha * (1 - (progress - 0.7) / 0.2))
                sub_text = sub_font.render("Autonomous Mobile Robotics", True, TEXT_COLOR)
                sub_rect = sub_text.get_rect(center=(center_x, center_y + 100))
                temp = pygame.Surface(sub_text.get_size(), pygame.SRCALPHA)
                temp.blit(sub_text, (0, 0))
                temp.set_alpha(subtitle_alpha)
                screen.blit(temp, sub_rect)

            # Particle effects
            for i in range(15):
                angle = progress * 10 + i * (math.pi * 2 / 15)
                distance = 200 + 50 * math.sin(progress * 5 + i)
                x = center_x + int(math.cos(angle) * distance)
                y = center_y + int(math.sin(angle) * distance)
                size = int(3 + 2 * math.sin(progress * 8 + i))
                pygame.draw.circle(screen, TEXT_COLOR, (x, y), size)

            # Update display
            pygame.display.flip()
            clock.tick(FPS)

        except Exception as e:
            print(f"Error in animation loop: {e}")
            time.sleep(0.1)

    # Clean up pygame
    pygame.quit()
    # Brief delay to ensure Pygame cleanup completes
    time.sleep(0.1)

# --- Menu UI (PyQt5) ---
class AMRInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AMR Robot UI")

        # Set fullscreen mode
        self.showFullScreen()

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Set gradient background
        central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y1:1,
                    stop:0 #1e1e2e, stop:1 #3b4252
                );
            }
        """)
        
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(50, 50, 50, 50)  # Add margins for better spacing

        # Status bar
        status_label = QLabel("AMR Team 1 : Menu")
        status_label.setStyleSheet("""
            font-size: 36px;
            font-weight: bold;
            color: #ffffff;
            background-color: rgba(0, 0, 0, 0.7);
            padding: 15px;
            border-radius: 10px;
            qproperty-alignment: AlignCenter;
        """)
        layout.addWidget(status_label)

        # Menu buttons
        mapping_btn = QPushButton("Mapping Mode")
        navigation_btn = QPushButton("Navigation Mode")
        debug_btn = QPushButton("Debug Mode")

        # Button styling for modern look
        for btn in [mapping_btn, navigation_btn, debug_btn]:
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 48px;
                    font-weight: bold;
                    color: #ffffff;
                    background: qlineargradient(
                        x1:0, y1:0, x2:1, y1:0,
                        stop:0 #0078FF, stop:1 #00b4ff
                    );
                    border: 2px solid #ffffff;
                    border-radius: 15px;
                    padding: 40px;
                    min-height: 120px;
                    min-width: 400px;
                }
                QPushButton:hover {
                    background: qlineargradient(
                        x1:0, y1:0, x2:1, y1:0,
                        stop:0 #0096ff, stop:1 #00d4ff
                    );
                    border: 2px solid #00d4ff;
                }
                QPushButton:pressed {
                    background: qlineargradient(
                        x1:0, y1:0, x2:1, y1:0,
                        stop:0 #0056b3, stop:1 #0096ff
                    );
                }
            """)
            layout.addWidget(btn, alignment=Qt.AlignCenter)

        # Add stretch to center buttons vertically
        layout.addStretch()

        # Connect buttons to functions
        mapping_btn.clicked.connect(self.show_mapping_mode)
        navigation_btn.clicked.connect(self.show_navigation_mode)
        debug_btn.clicked.connect(self.show_debug_mode)

    def keyPressEvent(self, event):
        # Exit on ESC key
        if event.key() == Qt.Key_Escape:
            self.close()

    def show_mapping_mode(self):
        print("Mapping Mode Selected")
        # Add logic for mapping sub-options later

    def show_navigation_mode(self):
        print("Navigation Mode Selected")
        # Add logic for navigation sub-options later

    def show_debug_mode(self):
        print("Debug Mode Selected")
        # Add logic for debug sub-options later

# --- Main Execution ---
if __name__ == "__main__":
    # Run splash screen
    run_splash_screen()
    
    # Run PyQt5 menu UI
    app = QApplication(sys.argv)
    window = AMRInterface()
    window.show()
    sys.exit(app.exec_())