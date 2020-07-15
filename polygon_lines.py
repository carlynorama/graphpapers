import math


def line_at_angle(x, y, my_radius, my_angle):
    end_x = math.cos(math.radians(my_angle))*my_radius + x
    end_y = math.sin(math.radians(my_angle))*my_radius + y
    f.write(f'\t<line x1="{x}in" y1="{y}in" x2="{end_x}in" y2="{end_y}in" style="{line_style}"/>\n')

def poly(center_x, center_y, number_of_verts, exterior_radius):
    degree_step = int(360/number_of_verts)
    my_points[]
    for a in range(0,360,degree_step):
        node_x = math.cos(math.radians(my_angle))*my_radius + x
        node_y = math.sin(math.radians(my_angle))*my_radius + y
        my_points.append(node_x, node_y)

line_style = "stroke:rgb(200,200,200);stroke-width:0.5"

width_in = 8.5
height_in = 11
radius = 0.25
poly_sides = 6


save_file_directory = "papers"
save_file_name = "radial_line_tess_" + str(burst_number) + "_poly"
save_file_full_path = save_file_directory + "/" + save_file_name


#burst_height = 2*(1/5)
#burst_width = burst_height


x_spacing = radius
y_spacing = x_spacing
offsetX = 0
offsetY = 0
x_count = int(width_in/x_spacing)-1
y_count = int(height_in/y_spacing)-1




f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write(f'<svg width="{width_in}in" height="{height_in}in" xmlns="http://www.w3.org/2000/svg">\n')

f.write('<g id="polygon mesh" transform="translate(%s, %s)">\n' % ("0", "0"))

for row in range(0,y_count):
    for col in range(0, x_count):
        y_cord = offsetY+(row*(y_spacing))
        x_cord = offsetX+(col*(x_spacing)) + (row%2 * x_spacing/2)
        radial_burst(x_cord, y_cord, burst_number, x_spacing/2 , 0)


f.write('\t</g>\n') #end grid
f.write('</svg>')
f.close()
