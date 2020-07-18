import math
from operator import itemgetter

pxPerInch = float(300)
width_in = float(8.5)
height_in = float(11)
viewBoxWidth = width_in * pxPerInch
viewBoxHeight = height_in * pxPerInch

poly_style = "stroke: rgb(50,50,50); stroke-width:0.5; fill: none;"
line_style = "stroke: rgb(50,50,50); stroke-width:0.5;"

AC = float(pxPerInch/2)
BD = float(pxPerInch/4)
padding = 0.0
x_spacing = AC + padding
y_spacing = BD + padding

tight_packed = True
draw_radials = "none" #both, AC, BD, none

rotation = math.radians(float(0.0))
vertical_snuggle = True
offsetX = 0.0
offsetY = 0.0

def draw_polar_line(origin_x, origin_y, radius, rad_angle):
    end_x = math.cos(rad_angle)*radius + origin_x
    end_y = math.sin(rad_angle)*radius + origin_y
    f.write(f'\t\t<line x1="{origin_x}" y1="{origin_y}" x2="{end_x}" y2="{end_y}" style="{line_style}"/>\n')

def draw_coord_line(x1, y1, x2, y2):
    f.write(f'\t\t<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="{line_style}"/>\n')

def get_vertex(x, y, my_radius, angle_radians):
    end_x = math.cos(angle_radians)*my_radius + x
    end_y = math.sin(angle_radians)*my_radius + y
    return (end_x, end_y)

def get_length(x1, y1, x2, y2):
    sideA = float(x2 - x1)
    sideB = float(y2 - y1)
    return float(math.sqrt((sideA * sideA) + (sideB * sideB)))


def rhombus1(center_x, center_y, r1, r2, radial_offset, lines):
    degree_step = 90.0
    my_points = []
    for a in range(0, 4):
        radians = math.radians(a*degree_step) + radial_offset
        if a%2:
            radius = r2
        else:
            radius = r1
        my_points.append(get_vertex(center_x, center_y, radius, radians))
    poly_points = get_poly_points_string(my_points)
    f.write(f'\t<polygon points="{poly_points}" style="{poly_style}"/>\n')
    if lines=="both":
        draw_r1 = True
        draw_r2 = True
    elif lines=="AC":
        draw_r1 = True
        draw_r2 = False
    elif lines=="BD":
        draw_r1 = False
        draw_r2 = True
    else:
        draw_r1 = False
        draw_r2 = False

    if draw_r1:
        draw_coord_line(my_points[0][0], my_points[0][1], my_points[2][0], my_points[2][1])
    if draw_r2:
        draw_coord_line(my_points[1][0], my_points[1][1], my_points[3][0], my_points[3][1])

def get_poly_points_string(points_array):
    points_string = " ".join(map(clean_tup, points_array))
    return points_string

def clean_tup(tuple):
    return '{0},{1}'.format(*tuple)

def get_rhombus_dimensions(r1, r2, radial_offset):
    degree_step = 90.0
    my_points = []
    for a in range(0, 4):
        radians = math.radians(a*degree_step) + radial_offset
        if a%2:
            radius = r2
        else:
            radius = r1
        my_points.append(get_vertex(r1*10.0, r2*10.0, radius, radians))
    bottom = max(my_points,key=itemgetter(1))[1]
    top = min(my_points,key=itemgetter(1))[1]
    left = max(my_points,key=itemgetter(0))[0]
    right = min(my_points,key=itemgetter(0))[0]
    side = get_length(my_points[0][0], my_points[0][1], my_points[1][0], my_points[1][1])
    return (float(left-right), float(bottom-top), side)

save_file_directory = "papers"
save_file_name = "rhombus1_" + str(int(AC)) + "_" + str(int(BD)) + "_" + draw_radials
if tight_packed:
    save_file_name = save_file_name + "_tp"
if vertical_snuggle:
    save_file_name = save_file_name + "_sng"
save_file_name = save_file_name + "_" + str(int(math.degrees(rotation))) + "_deg"

save_file_full_path = save_file_directory + "/" + save_file_name

f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))

rhomb_width, rhomb_height, side_length = get_rhombus_dimensions(AC/2.0, BD/2.0, rotation)

x_spacing = rhomb_width + padding
y_spacing = rhomb_height + padding

if vertical_snuggle:
    y_spacing = y_spacing - side_length/2.0

x_count = int(viewBoxWidth/x_spacing)
y_count = int(viewBoxHeight/y_spacing)

for row in range(0,y_count):
    for col in range(0, x_count):
        y_cord = offsetY+(float(row)*(y_spacing))
        #x_cord = offsetX+(col*(x_spacing)) + (row%2 * x_spacing/2)
        x_cord = offsetX+(float(col)*(x_spacing))
        if tight_packed:
            x_cord = x_cord + (float(row%2) * x_spacing/2.0)
        rhombus1(x_cord, y_cord, AC/2, BD/2, rotation, draw_radials)


f.write('</svg>')
f.close()
