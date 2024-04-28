import os
import sys
from PIL import Image
from random import randint

def DragonIteration(gen, dragonbinary):
	size = len(dragonbinary)
	mem = 0
	gen+=1;

	if size == 1 :
		mem = 0
	else:
		mem = int((size - 1)/2)

	dragonbinary.append(1)

	for i in range(0,size):
		if i == mem:
			if dragonbinary[mem] == 0:
				dragonbinary.append(1)
			else:
				dragonbinary.append(0)
		else:
			dragonbinary.append(dragonbinary[i])
	return gen, dragonbinary

def DrawDragonBinary(pixels, dragonbinary, initialPos, prevDir):
	for i in range(0,len(dragonbinary)):

		if prevDir == "West":
			if dragonbinary[i] == 1:
				prevDir,pixels,initialPos = PlaceIt("Down",pixels,initialPos)
			else:
				prevDir,pixels,initialPos = PlaceIt("Up",pixels,initialPos)
		elif prevDir == "East":
			if dragonbinary[i] == 1:
				prevDir,pixels,initialPos = PlaceIt("Up",pixels,initialPos)
			else:
				prevDir,pixels,initialPos = PlaceIt("Down",pixels,initialPos)
		elif prevDir == "North":
			if dragonbinary[i] == 1:
				prevDir,pixels,initialPos = PlaceIt("Right",pixels,initialPos)
			else:
				prevDir,pixels,initialPos = PlaceIt("Left",pixels,initialPos)
		elif prevDir == "South":
			if dragonbinary[i] == 1:
				prevDir,pixels,initialPos = PlaceIt("Left",pixels,initialPos)
			else:
				prevDir,pixels,initialPos = PlaceIt("Right",pixels,initialPos)
	return pixels

def PlaceIt(direction, pixels, initialPos):

	color = (233,84,32)

	if direction == "Down":
		pixels[initialPos[0], initialPos[1] - 1] = color
		initialPos = [initialPos[0], initialPos[1] - 1] 
		direction = "South"

	elif direction == "Up":
		pixels[initialPos[0], initialPos[1] + 1] = color
		initialPos = [initialPos[0], initialPos[1] + 1]
		direction = "North"

	elif direction == "Left":
		pixels[initialPos[0] - 1, initialPos[1]] = color
		initialPos = [initialPos[0] - 1, initialPos[1]]
		direction = "East"

	elif direction == "Right":
		pixels[initialPos[0] + 1, initialPos[1] ] = color
		initialPos = [initialPos[0] + 1, initialPos[1]]
		direction = "West"
	return direction, pixels, initialPos

print("sys.argv --> x, y, number_of_iterations, initialDir")
print(sys.argv)
img = Image.new('RGB', (2048, 1024), "black")
pixels = img.load()
number_of_iterations = 14
dragonbinary = []
gen = 0
prevDir = "North"
initialPos = [img.size[0]/2,img.size[1]/2]

dragonbinary.append(1)
	
for i in range(0, number_of_iterations):
	gen, dragonbinary = DragonIteration(gen, dragonbinary)

pixels = DrawDragonBinary(pixels, dragonbinary, initialPos, prevDir)



img.save("dragon.bmp")