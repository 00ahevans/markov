"""
    Adelaide Evans
    Markov Chains HW
    Generates abstract art using transition matrices to determine shapes and colors. 
    Dependencies:
        aggdraw
        numpy
        Pillow
    To install all use command "pip install -r requirements.txt"
"""

import numpy as np
from numpy import array as a
from numpy import random
import math
import aggdraw
from constants import BLOB_DICT, COLORS_DICT, COLOR_PROBS, SHAPE_PROBS, COLOR_GROUPS, NUM_COLORS_PER_GROUP, \
                      SHAPE_GROUPS, NUM_SHAPES_PER_GROUP
from PIL import Image, ImageDraw, ImagePath
from itertools import cycle



class ShapeArt:

    def __init__(self, num_cgs, num_cpg, color_probs, num_sgs, num_spg, shape_probs):
        """
        params: 
            num_cgs (int): number of color groups
            num_cpg (int): number of colors per group
            color_probabilities (list): probabilities of a color group being chosen
            num_sgs (int): number of shape groups
            num_spg (int): number of shapes per group 
        """
        self.num_color_groups = num_cgs
        self.num_colors_per_group = num_cpg
        self.num_shape_groups = num_sgs
        self.num_shapes_per_group = num_spg
        self.color_tm = None
        self.shape_tm = None
        self.color_probs = color_probs
        self.shape_probs = shape_probs
        self.color_group = random.randint(1,num_cgs +1)
        self.color = self.color_group * random.randint(1, num_cpg +1 )
        self.shape_group = random.randint(1, num_sgs + 1)
        self.shape = self.shape_group * random.randint(1, num_spg + 1)
        

    def make_tm(self, type):
        """
        params: 
            type (string): type of transition matrix you want to create (color or shape)
        """
        tm = {}
        if (type=="color"):
            g = self.num_color_groups
            probs = self.color_probs
        if (type=="shape"):
            g = self.num_shape_groups
            probs = self.shape_probs
        
        
        for num in range(1, g + 1):
            tm[num] = {}
            for index in range(1, g + 1 ):
                tm[num][index] = probs[index-1]
            probs = np.roll(probs, 1)
        
        if (type == "color"):
            self.color_tm = tm
        if (type == "shape"):
            self.shape_tm = tm

    def get_color(self):
        """
        returns the current color of the ShapeArt object, represented by an int that corresponds
        to a color in the constants file
        """
        return self.color
        
    def get_shape(self):
        """
        returns the current shape of the ShapeArt object, represented by an int that corresponds
        to a shape in the constants file
        """
        return self.shape

    def set_next_color(self):
        """
        sets the next color, according to the current color and the probability of other color groups
        based on the transition matrix of the object. Picks a random number from within the chosen color group
        """
        group_choices = range(1, self.num_color_groups + 1)
        group =  np.random.choice(
            group_choices,
            p=[self.color_tm[self.color_group][x] \
            for x in group_choices])

        randomizer  = random.randint(1, self.num_colors_per_group)

        self.color_group = group
        self.color = group*self.num_colors_per_group - randomizer

    def set_next_shape(self):
        """
        sets the next shape to make based on the current shape and the probability of other shape groups
        based on the transition matrix in the constants file. Picks a random number from within the chosen shape group
        """
        group_choices = range(1, self.num_shape_groups + 1)
        group =  np.random.choice(
            group_choices,
            p=[self.shape_tm[self.shape_group][x] \
            for x in group_choices])
        
        randomizer  = random.randint(1, self.num_shapes_per_group)

        self.shape_group = group
        self.shape = group*self.num_shapes_per_group - randomizer

    def draw_grid(self, filename):
        """
        draws 25 colored shapes in a grid of size 1000x1000 pixels. The shapes and colors are chosen according
        to the set_next_shape and set_next_color functions.

        params:
            filename (string): the name of the file to save the image as
        """
        img = Image.new("RGBA", (1000,1000)) # last part is image dimensions
        draw = aggdraw.Draw(img)
        for x in range(0, 5):
            x_coord = (x) * 200 + 100
            for y in range(0, 5):
                y_coord = (y) * 200 + 100
                path = BLOB_DICT[self.get_shape()]
                self.set_next_shape()
                color = COLORS_DICT[self.get_color()]
                self.set_next_color()
                fill = aggdraw.Pen(color, 5)
                outline = aggdraw.Brush(color)
                symbol = aggdraw.Symbol(path)
                draw.symbol((x_coord, y_coord), symbol, outline, fill)
        draw.flush()
        #img.show()
        img.save(filename + ".png")

    def draw_random(self,filename):
        """
        draws a random number (between 1 and 200) of colored shapes. Again, the shape chosen and color chosen depend on the 
        transition matrix in the constants file.
        params:
            filename (string): the name of the file to save the image as
        """
        img = Image.new("RGBA", (1000,1000)) # last part is image dimensions
        draw = aggdraw.Draw(img)
        num_shapes = random.randint(1,200)
        for x in range(0,num_shapes):
            x_coord = random.randint(0,1000)
            y_coord = random.randint(0,1000)
            path = BLOB_DICT[random.randint(0,25)]
            color = COLORS_DICT[self.get_color()]
            self.set_next_color()
            fill = aggdraw.Pen(color, 5)
            outline = aggdraw.Brush(color)
            symbol = aggdraw.Symbol(path)
            draw.symbol((x_coord, y_coord), symbol, outline, fill)
        draw.flush()
        img.save(filename + ".png")


def main():

    ShapeArt1 = ShapeArt(COLOR_GROUPS, NUM_COLORS_PER_GROUP, COLOR_PROBS, SHAPE_GROUPS, NUM_SHAPES_PER_GROUP, SHAPE_PROBS  )
    ShapeArt1.make_tm("color")
    ShapeArt1.make_tm("shape")


    for x in range(0,3):
        filename = "grid_test" + str(x)
        ShapeArt1.draw_grid(filename)

    for x in range(0,3):
        filename = "random_test" + str(x)
        ShapeArt1.draw_random(filename)

if __name__ == "__main__":
    main()


