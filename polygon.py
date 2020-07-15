import math

width_in = 8.5
height_in = 11
number_verts = 5
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


def line_at_angle(x, y, my_radius, angle_radians):
    end_x = math.cos(angle_radians)*my_radius + x
    end_y = math.sin(angle_radians)*my_radius + y
    f.write(f'\t<line x1="{x}in" y1="{y}in" x2="{end_x}in" y2="{end_y}in" style="{trace_style}"/>\n')

def polygon(center_x, center_y, ext_radius, number_verts):
    degree_step = float(360/number_verts)
    for a in range(0, number_verts):
        radians = math.radians(a*degree_step) + radial_offset
        line_at_angle(center_x, center_y, radius, radians)



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
