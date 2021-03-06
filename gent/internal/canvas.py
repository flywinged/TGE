# Copyright Clayton Brown 2019. See LICENSE file.

from typing import List

import numpy

import platform

from sty import fg, bg

from ..utilities import ImageData
from typing import Tuple

class Canvas:
    '''
    The Canvas class holds all the screen information necessary to draw in the terminal.

    Parameters
    ----------
    width, height: The width and the height of the canvas in characters.
    '''       

    def __init__(self, width: int, height: int):
        
        # Hold the width and height variables for use elsewhere
        self.width: int = width
        self.height: int = height

        # Create the character and format arrays. Separated as such for linting reasons
        self.characters: numpy.ndarray
        self.characters = numpy.zeros((self.width, self.height), dtype = numpy.uint16)
        self.textColors: numpy.ndarray
        self.textColors = numpy.zeros((self.width, self.height, 3), dtype = numpy.uint8)
        self.backgroundColors: numpy.ndarray
        self.backgroundColors = numpy.zeros((self.width, self.height, 3), dtype = numpy.uint8)
        self.transparency: numpy.ndarray
        self.transparency = numpy.ones((self.width, self.height), dtype = numpy.uint8)

        # Populate the character and format arrays with default values
        self.clearCanvas(" ", 0)
    
    def drawImage(self, image: ImageData, location: Tuple[int] = (0, 0)):
        '''
        Draw imageData onto a location on the canvas
        '''

        startX = location[0]
        endX = location[0] + image.backgroundColorData.shape[0]
        startY = location[1]
        endY = location[1] + image.backgroundColorData.shape[1]

        self.backgroundColors[startX:endX, startY:endY, :] = image.backgroundColorData[:,:,:]
        self.textColors[startX:endX, startY:endY, :] = image.textColorData[:,:,:]
        self.transparency[startX:endX, startY:endY] = image.transparencyData[:,:]
        self.characters[startX:endX, startY:endY] = image.characterData[:,:]
    
    def clearCanvas(self, clearCharacter: str = " ", textColor: tuple = (255, 255, 255), backgroundColor: tuple = (0, 0, 0), transparency: int = 0):
        '''
        Assign format and character values to the entire canvas at once
        '''

        # Replace the canvas characters and formats at each "pixel" location
        self.characters.fill(ord(clearCharacter))
        self.textColors[:,:] = numpy.array(textColor)
        self.backgroundColors[:,:] = numpy.array(backgroundColor)
        self.transparency[:,:] = transparency

    def getCanvasText(self):
        '''
        Return a string representation of the canvas. This string is what will be printed for visuals.
        '''

        # Allocated all the memory for the string right at the start
        resultingString: List[str] = [""] * (self.width * self.height + 2)

        # Loop through all the characters of both the string and the formatString, and create the resulting string list
        previousTextColor = None
        previousBackgroundColor = None
        for j in range(self.height):
            for i in range(self.width):
            
                character = chr(self.characters[i, j])

                textColor = tuple(self.textColors[i, j])
                backgroundColor = tuple(self.backgroundColors[i, j])

                if not previousTextColor or textColor != previousTextColor:
                    character = fg(*textColor) + character
                    previousTextColor = textColor

                if not previousBackgroundColor or backgroundColor != previousBackgroundColor:
                    character = bg(*backgroundColor) + character
                    previousBackgroundColor = backgroundColor

                # If at the beginning of the line, need to include a new line \n to the character
                if i == 0:

                    if "win" in platform.system().lower():
                        character = "\n" + character

                resultingString[j * self.width + i] = character

        # Clear the terminal format after each draw
        resultingString[-2] = bg.rs
        resultingString[-1] = fg.rs

        # Add the last
        return "".join(resultingString)

