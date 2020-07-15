import math


def poly(center_x, center_y, number_of_verts, exterior_radius):
    my_points = []
    for a in range(0,number_of_verts):
        #print(a)
        node_x = math.cos(math.radians(a))*exterior_radius + center_x
        node_y = math.sin(math.radians(a))*exterior_radius + center_y
        my_points.append((node_x, node_y))
    poly_points = get_poly_points_string(my_points)
    f.write(f'\t<polygon points="{poly_points}" style="fill:lime;stroke:purple;stroke-width:1"/>\n')

def get_poly_points_string(points_array):
    points_string = " ".join(map(clean_tup, points_array))
    return points_string

def clean_tup(tuple):
    return '{0},{1}'.format(*tuple)


line_style = "stroke:rgb(200,200,200);stroke-width:0.5"

viewBoxWidth = 2550
viewBoxHeight = 3300

width_in = 8.5
height_in = 11
radius = 0.25
poly_sides = 6


save_file_directory = "papers"
save_file_name = "poly_line_" + str(poly_sides) + "_poly"
save_file_full_path = save_file_directory + "/" + save_file_name


#burst_height = 2*(1/5)
#burst_width = burst_height


x_spacing = (viewBoxWidth/8.5) * 0.25
y_spacing = x_spacing
offsetX = 0
offsetY = 0
x_count = int(viewBoxWidth/x_spacing)
y_count = int(viewBoxHeight/y_spacing)




f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))

f.write('<g id="polygon mesh" transform="translate(%s, %s)">\n' % ("0", "0"))

for row in range(0,y_count):
    for col in range(0, x_count):
        y_cord = offsetY+(row*(y_spacing))
        x_cord = offsetX+(col*(x_spacing)) + (row%2 * x_spacing/2)
        poly(x_cord, y_cord, poly_sides, 1000)


f.write('\t</g>\n') #end grid
f.write('</svg>')
f.close()
