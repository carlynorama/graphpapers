import math
from operator import itemgetter

pxPerInch = float(300)
width_in = float(8.5)
height_in = float(11)
viewBoxWidth = width_in * pxPerInch
viewBoxHeight = height_in * pxPerInch

polys_per_inch = 4
spacer = False
spacer_height = 0
tight_packed = True
vertical_snuggle = True
padding = 0#float(x_spacing/10)
size = (pxPerInch/float(polys_per_inch) - padding)



number_verts = 12
#rotation = math.radians(-90)
#rotation = math.radians(360.0/float(number_verts))
rotation = math.radians(360.0/float(number_verts)/2.0)
offsetX = 0
offsetY = 0

def draw_polar_line(origin_x, origin_y, radius, rad_angle):
    end_x = math.cos(rad_angle)*radius + origin_x
    end_y = math.sin(rad_angle)*radius + origin_y
    f.write(f'\t\t<line x1="{origin_x}" y1="{origin_y}" x2="{end_x}" y2="{end_y}" style="{line_style}"/>\n')

def get_vertex(x, y, my_radius, angle_radians):
    end_x = math.cos(angle_radians)*my_radius + x
    end_y = math.sin(angle_radians)*my_radius + y
    return (end_x, end_y)

def get_length(x1, y1, x2, y2):
    sideA = float(x2 - x1)
    sideB = float(y2 - y1)
    return math.sqrt((sideA * sideA) + (sideB * sideB))

def get_poly_height(this_radius, number_verts, radial_offset):
    degree_step = float(360/number_verts)
    my_points = []
    for a in range(0, number_verts):
        radians = math.radians(a*degree_step) + radial_offset
        my_points.append(get_vertex(4.0*this_radius, 4.0*this_radius, this_radius, radians))
    bottom = max(my_points,key=itemgetter(1))[1]
    top = min(my_points,key=itemgetter(1))[1]
    return bottom-top

def get_poly_width(this_radius, number_verts, radial_offset):
    degree_step = float(360/number_verts)
    my_points = []
    for a in range(0, number_verts):
        radians = math.radians(a*degree_step) + radial_offset
        my_points.append(get_vertex(4.0*this_radius, 4.0*this_radius, this_radius, radians))
    #print(my_points)
    left = max(my_points,key=itemgetter(0))[0]
    right = min(my_points,key=itemgetter(0))[0]
    #print(left, right)
    return left-right

def get_poly_height(this_radius, number_verts, radial_offset):
    degree_step = float(360/number_verts)
    my_points = []
    for a in range(0, number_verts):
        radians = math.radians(a*degree_step) + radial_offset
        my_points.append(get_vertex(4.0*this_radius, 4.0*this_radius, this_radius, radians))
    bottom = max(my_points,key=itemgetter(1))[1]
    top = min(my_points,key=itemgetter(1))[1]
    return bottom-top


def polygon(center_x, center_y, this_radius, number_verts, radial_offset, line_spacer):
    degree_step = float(360/number_verts)
    my_points = []
    for a in range(0, number_verts):
        radians = math.radians(a*degree_step) + radial_offset
        my_points.append(get_vertex(center_x, center_y, this_radius, radians))
    poly_points = get_poly_points_string(my_points)
    f.write(f'\t<polygon points="{poly_points}" style="{poly_style}"/>\n')
    if line_spacer:
        #side_length = get_length(my_points[0][0], my_points[0][1], my_points[1][0], my_points[1][1])
        #This needs to be fixed so doesn't reference a global
        draw_polar_line(center_x, center_y-this_radius, spacer_height, math.radians(-90))

def get_poly_side_length(this_radius, number_verts, radial_offset):
    degree_step = float(360/number_verts)
    my_points = []
    for a in range(0, 2):
        radians = math.radians(a*degree_step) + radial_offset
        my_points.append(get_vertex(4.0*this_radius, 4.0*this_radius, this_radius, radians))
    return get_length(my_points[0][0], my_points[0][1], my_points[1][0], my_points[1][1])


def get_poly_points_string(points_array):
    points_string = " ".join(map(clean_tup, points_array))
    return points_string

def clean_tup(tuple):
    return '{0},{1}'.format(*tuple)



save_file_directory = "papers"
save_file_name = "tiles_poly_" + str(number_verts) + "_sides_" + str(polys_per_inch) + "_per_inch"
if spacer:
    save_file_name = save_file_name + "_spaced"
if tight_packed:
    save_file_name = save_file_name + "_tp"
if vertical_snuggle:
    save_file_name = save_file_name + "_sng"
save_file_name = save_file_name + "_" + str(int(math.degrees(rotation))) + "_deg"

save_file_full_path = save_file_directory + "/" + save_file_name

poly_style = "stroke: rgb(200,200,200); stroke-width:0.; fill: none;"
line_style = "stroke: rgb(200,200,200); stroke-width:0.;"

f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))

x_spacing = get_poly_width(size/2.0, number_verts, rotation)
y_spacing = get_poly_height(size/2.0, number_verts, rotation)

side_length = get_poly_side_length(size/2.0, number_verts, rotation)

if vertical_snuggle:
    y_spacing = y_spacing - side_length/2.0

if spacer:
    spacer_height = y_spacing
    #y_spacing = y_spacing *1.5
    y_spacing = y_spacing * 1.5
    spacer_height = y_spacing-spacer_height



x_count = int(viewBoxWidth/x_spacing)
y_count = int(viewBoxHeight/y_spacing)


for row in range(0,y_count):
    for col in range(0, x_count):
        y_cord = offsetY+(float(row)*(y_spacing))
        #x_cord = offsetX+(col*(x_spacing)) + (row%2 * x_spacing/2)
        x_cord = offsetX+(float(col)*(x_spacing))
        if tight_packed:
            x_cord = x_cord + (float(row%2) * x_spacing/2.0)
        polygon(x_cord, y_cord, size/2.0, number_verts, rotation, spacer)


f.write('</svg>')
f.close()
