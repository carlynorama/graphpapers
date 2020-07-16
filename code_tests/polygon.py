import math

width_in = 8.5
height_in = 11
number_verts = 6
radial_offset = math.radians(-90)
offsetX = 0.25
offsetY = 0.25
centerX = width_in/2
centerY = height_in/2
ext_radius = ((width_in- offsetX)/2)/2
int_radius = 0
radius = ext_radius - int_radius
x_cord = centerX
y_cord = centerY


def get_vertex(x, y, my_radius, angle_radians):
    end_x = math.cos(angle_radians)*my_radius + x
    end_y = math.sin(angle_radians)*my_radius + y
    return (end_x, end_y)

def polygon(center_x, center_y, this_radius, number_verts):
    degree_step = float(360/number_verts)
    my_points = []
    for a in range(0, number_verts):
        radians = math.radians(a*degree_step) + radial_offset
        my_points.append(get_vertex(center_x, center_y, this_radius, radians))
    start_x = my_points[0][0]
    start_y = my_points[0][1]
    for i in range(1,number_verts):
        end_x = my_points[i][0]
        end_y = my_points[i][1]
        f.write(f'\t<line x1="{start_x}in" y1="{start_y}in" x2="{end_x}in" y2="{end_y}in" style="{trace_style}"/>\n')
        start_x = end_x
        start_y = end_y
    f.write(f'\t<line x1="{start_x}in" y1="{start_y}in" x2="{my_points[0][0]}in" y2="{my_points[0][1]}in" style="{trace_style}"/>\n')


def get_poly_points_string(points_array):
    points_string = " ".join(map(clean_tup, points_array))
    return points_string

def clean_tup(tuple):
    return '{0},{1}'.format(*tuple)

#radius = 0.015625#1/64th

save_file_directory = "papers"
save_file_name = "poly_" + str(number_verts) + "_sides"
save_file_full_path = save_file_directory + "/" + save_file_name

trace_style = "stroke: rgb(200,200,200); fill: none;"

f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write(f'<svg width="{width_in}in" height="{height_in}in"  xmlns="http://www.w3.org/2000/svg">\n')

polygon(centerX, centerY, radius, number_verts)

f.write('</svg>')
f.close()
