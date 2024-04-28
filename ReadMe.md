# Dragon Curve Generator

This code snippet generates an image of a Dragon Curve using a binary sequence. The Dragon Curve is a type of fractal pattern that creates intricate designs. 
This implementation uses the Python Imaging Library (PIL) to draw the curve on an image canvas and save it to a BMP file.

![Example](./dragon.bmp)

## Prerequisites

- Python 3.x
- PIL (Python Imaging Library)

Ensure that Python is installed on your system and the PIL library is available.

## How It Works

- The code starts by initializing an image with a specific size (2048x1024 pixels) and a default color (black).
- It generates a binary sequence representing the Dragon Curve based on a specified number of iterations.
- The `DragonIteration` function generates the binary sequence, and the `DrawDragonBinary` function plots the curve onto the image.
- The `PlaceIt` function handles the directional logic for drawing the curve on the canvas.
- After generating the Dragon Curve, the image is saved as "dragon.bmp".

## Usage

To run the code snippet, use a Python environment with the necessary dependencies installed. The snippet has several default parameters, but you can modify the following:

- **number_of_iterations**: The number of times the Dragon Curve is iterated (default is 17).
- **prevDir**: The initial direction for the curve (default is "North").
- **initialPos**: The starting position for the curve (default is the center of the image).

Example command to run the code:
```bash
python dragon_curve.py
```

## Output

The output is a BMP image with the generated Dragon Curve, saved as "dragon.bmp" in the current directory.