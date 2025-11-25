import os
import time
import math
from colorama import init, Fore, Style
import random

# Initialize colorama
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_char(value):
    """Map numeric value to ASCII character"""
    chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '█', '▓', '▒', '░', '8', 'o', 'O', 'G']
    return chars[value % len(chars)]

def get_color(value):
    """Get color based on value"""
    colors = [
        Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW,
        Fore.MAGENTA, Fore.CYAN, Fore.WHITE,
        Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX,
        Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
    ]
    return colors[value % len(colors)]

def create_pattern(width, height, offset):
    """Create complex mathematical pattern using trigonometric functions"""
    pattern = []
    
    for y in range(height):
        row = ""
        for x in range(width):
            # Create complex mathematical combinations
            dx = x - width // 2
            dy = y - height // 2
            
            # Multiple wave components with different frequencies
            wave1 = math.sin(dx * 0.05 + offset * 0.02)
            wave2 = math.cos(dy * 0.05 + offset * 0.03)
            wave3 = math.sin(math.sqrt(dx*dx + dy*dy) * 0.03 + offset * 0.01)
            wave4 = math.cos((dx - dy) * 0.02 + offset * 0.04)
            
            # Combine waves with different amplitudes
            combined = (wave1 * 3 + 
                       wave2 * 2 + 
                       wave3 * 4 + 
                       wave4 * 2 +
                       math.sin(offset * 0.005) * 0.5) * 10
            
            # Add harmonic components for complexity
            harmonic = (math.sin(dx * 0.1 + offset * 0.01) * 
                       math.cos(dy * 0.1 + offset * 0.02))
            
            value = int((combined + harmonic + offset * 0.1) % 18)
            
            char = get_char(value)
            color = get_color(value)
            
            colored_char = f"{color}{char}"
            row += colored_char
            
        pattern.append(row)
    
    return pattern

def main():
    try:
        width, height = os.get_terminal_size()
    except Exception:
        width, height = 80, 24
    
    # Ensure reasonable dimensions
    width = max(40, min(width - 1, 150))
    height = max(20, min(height - 1, 100))
    
    print(f"Terminal size: {width} x {height}")
    print("Complex ASCII Music Visualizer - Press Ctrl+C to exit")
    print("=" * (width + 5))
    
    offset = 0
    
    try:
        while True:
            clear_screen()
            
            pattern = create_pattern(width, height, offset)
            
            # Print the pattern
            for row in pattern:
                print(row)
                
            offset += 1
            time.sleep(0.02)  # Control animation speed
            
    except KeyboardInterrupt:
        clear_screen()
        print("Visualizer stopped.")

if __name__ == "__main__":
    main()
