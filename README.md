# Traffic Light Controller with MicroPython

Youtube Link:
https://www.youtube.com/shorts/b71Qk9Rgh4Y

## Overview
This project is a simple traffic light controller implemented using MicroPython. It controls LEDs to simulate traffic signals for four different lanes.

## Hardware Requirements
- A microcontroller that supports MicroPython (e.g., Raspberry Pi Pico, ESP32)
- LEDs (Red, Yellow, Green) for each lane
- Resistors (220Ω recommended)
- Breadboard and jumper wires

## Wiring Configuration
Each lane has three LEDs (Red, Yellow, Green) connected to specific GPIO pins:

| Lane   | Red Pin | Yellow Pin | Green Pin |
|--------|--------|------------|-----------|
| Jalur 1 | 1      | 2          | 3         |
| Jalur 2 | 5      | 8          | 9         |
| Jalur 3 | 10     | 11         | 12        |
| Jalur 4 | 13     | 14         | 15        |

## Code Explanation
- The `traffic_lights` dictionary stores the GPIO pin configuration for each lane.
- The `all_red()` function ensures that all lanes start with a red signal.
- The `traffic_cycle(jalur)` function controls the signal timing:
  - Sets all lights to red
  - Turns green for the selected lane for 5 seconds
  - Changes to yellow for 2 seconds before switching back to red
- The `while True` loop cycles through all four lanes in sequence.

## Usage
1. Load the script onto your MicroPython-compatible board.
2. Connect the LEDs and power up the board.
3. The traffic lights will cycle automatically.

## Future Improvements
- Add pedestrian crossing functionality
- Implement sensors for traffic density detection
- Integrate with IoT for remote monitoring

## License
This project is open-source and free to use for educational and personal projects.

