# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from turtle import fillcolor
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
    x0 = 500
    y0 = 425
    x1 = 550
    y1 = 475
    draw_oval(canvas, x0, y0, x1, y1,width=1, outline="yellow2", fill="yellow1")
    draw_cloud(canvas,scene_width, scene_height)


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="tan4")
    
    tree_center_x = 360
    tree_bottom = 100
    tree_height = 300
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)

    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)
    draw_grass_background(canvas)
    draw_fence(canvas)
    draw_grass_foreground(canvas)
    

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="tan2", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="green", width=1, fill="dark green")
def draw_cloud(canvas,scene_width, scene_height):
    # draw_oval(canvas, x0, y0, x1, y1, *,
        # width=1, outline="black", fill=""):
    cloud_1 = 100 
    cloud_2 = 300 
    cloud_3 = 450 
    cloud_4 = 350 
    draw_oval(canvas, cloud_1, cloud_2, cloud_3, cloud_4, width=1, outline="snow1", fill="snow1")
    draw_oval(canvas, cloud_1 + 10, cloud_2 + 10, cloud_3 + 50, cloud_4 + 50, width=1, outline="snow1", fill="snow1")
    draw_oval(canvas, cloud_1 + 200, cloud_2 + 50, cloud_3 + 300, cloud_4 + 100, width=1, outline="snow1", fill="snow1")
        
def draw_fence(canvas):
    draw_fence_post(canvas)
    fence_support(canvas)
    
def draw_fence_post(canvas):
    fence_point(canvas)
    fence_body(canvas)

def fence_point(canvas):
    xb = 0
    x0 = 10
    y0 = 100
    x1 = 25
    y1 = 125
    x2 = 40
    y2 = 100
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, width=1, outline="snow1", fill="snow1")
    while xb != 15:
        x0 += 50
        x1 += 50
        x2 += 50
        draw_polygon(canvas, x0, y0, x1, y1, x2, y2, width=1, outline="snow1", fill="snow1")
        xb += 1      

def fence_body(canvas):
    xb =0
    x0 = 10
    y0 = 10
    x1 = 40
    y1 = 100
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="snow1", fill="snow1")
    while xb != 15:
        x0 += 50
        x1 += 50
        draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="snow1", fill="snow1")
        xb += 1

def fence_support(canvas):
    xb = 0
    x0 = 0
    y0 = 50
    x1 = 500
    y1 = 75
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="snow2", fill="snow1")
    while xb != 3:
        x0 += 275
        x1 += 275
        draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="snow2", fill="snow1")
        xb += 1

def draw_grass_background(canvas):
    xb = 0
    x0 = 5
    y0 = 20
    x1 = 20
    y1 = 50
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="green2", fill="green1")
    while xb != 41:
        y1 = 80
        x0 += 19
        x1 += 19
        y1 += random.randint(10,40)
        draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="green2", fill="green1")
        xb += 1

def draw_grass_foreground(canvas):
    xb = 0
    x0 = 5
    y0 = 5
    x1 = 20
    y1 = 40
    draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="green2", fill="green1")
    while xb != 41:
        y1 = 20
        x0 += 19
        x1 += 19
        y1 += random.randint(1,20)
        draw_rectangle(canvas, x0, y0, x1, y1, width=1, outline="green2", fill="green1")
        xb += 1

        

# Call the main function so that
# this program will start executing.
main()