import math

pxPerInch = 300
width_in = 8.5
height_in = 11
viewBoxWidth = width_in * pxPerInch
viewBoxHeight = height_in * pxPerInch


number_verts = 6
radial_offset = math.radians(-90)
offsetX = 0.25 * pxPerInch
offsetY = 0.25 * pxPerInch
centerX = viewBoxWidth / 2
centerY = viewBoxHeight / 2
ext_radius = (width_in)/2 * pxPerInch
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
    poly_points = get_poly_points_string(my_points)
    f.write(f'\t<polygon points="{poly_points}" style="fill:lime;stroke:purple;stroke-width:1"/>\n')


def get_poly_points_string(points_array):
    points_string = " ".join(map(clean_tup, points_array))
    return points_string

def clean_tup(tuple):
    return '{0},{1}'.format(*tuple)

#radius = 0.015625#1/64th

save_file_directory = "papers"
save_file_name = "polyshape_" + str(number_verts) + "_sides"
save_file_full_path = save_file_directory + "/" + save_file_name

trace_style = "stroke: rgb(200,200,200); fill: none;"

f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))


polygon(centerX, centerY, radius, number_verts)

f.write('</svg>')
f.close()
