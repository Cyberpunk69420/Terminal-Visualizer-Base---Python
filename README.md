# ASCII Music Visualizer

A mesmerizing terminal-based music visualizer that generates complex, colorful patterns using mathematical functions and trigonometric waves.

![ASCII Music Visualizer Demo](demo.gif)

## Features

- **Complex Mathematical Patterns**: Creates intricate designs using sine, cosine, and harmonic functions
- **Colorful ASCII Art**: 13 vibrant colors that cycle through the patterns
- **Smooth Animation**: Fluid motion with adjustable speed
- **Responsive Design**: Automatically adapts to terminal window size
- **Lightweight Implementation**: Pure Python with minimal dependencies

## Screenshots

<img width="1519" height="1087" alt="image" src="https://github.com/user-attachments/assets/06d04ea9-66aa-4246-9cd7-128910e4cacf" />


## Requirements

- Python 3.x
- Colorama library (install with `pip install colorama`)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ascii-music-visualizer.git
cd ascii-music-visualizer

# Install dependencies
pip install colorama
```

## Usage

Run the visualizer:
```bash
python ascii_visualizer.py
```

Press `Ctrl+C` to exit the visualizer.

## How It Works

The visualizer generates patterns using complex mathematical combinations:

1. **Wave Components**: Multiple sine and cosine waves with different frequencies
2. **Harmonic Mixing**: Combines waves with different amplitudes and phases
3. **Positional Math**: Uses x,y coordinates and distance from center
4. **Color Mapping**: Maps pattern values to vibrant terminal colors

## Customization

### Adjust Animation Speed
Modify the `time.sleep()` value in `main()`:
```python
time.sleep(0.05)  # Lower = faster, higher = slower
```

### Modify Pattern Complexity
Adjust the mathematical combinations in `create_pattern()` function.

## Terminal Compatibility

Works best in:
- Windows Terminal
- Linux terminals (gnome-terminal, konsole, etc.)
- macOS Terminal
- VS Code Integrated Terminal

## Controls

- **Ctrl+C**: Exit the visualizer gracefully
- **Resize Window**: Automatically adjusts to new terminal dimensions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Author

Created with ❤️ for ASCII art enthusiasts and music visualizer fans

---

*Note: For best results, use a terminal with 256-color support and proper ANSI color rendering.*
