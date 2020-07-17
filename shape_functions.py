import math
from operator import itemgetter

def get_vertex(center_x, center_y, my_radius, angle_radians):
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
    f.write(f'\t<polygon points="{poly_points}" style="{dot_style}"/>\n')


def get_poly_points_string(points_array):
    points_string = " ".join(map(clean_tup, points_array))
    return points_string

def clean_tup(tuple):
    return '{0},{1}'.format(*tuple)

def draw_polar_line(origin_x, origin_y, radius, rad_angle):
    end_x = math.cos(rad_angle)*radius + origin_x
    end_y = math.sin(rad_angle)*radius + origin_y
    f.write(f'\t\t<line x1="{origin_x}" y1="{origin_y}" x2="{end_x}" y2="{end_y}" style="{line_style}"/>\n')

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
