import math


def line_at_angle(x, y, my_radius, my_angle):
    end_x = math.cos(math.radians(my_angle))*my_radius + x
    end_y = math.sin(math.radians(my_angle))*my_radius + y
    f.write(f'\t<line x1="{x}in" y1="{y}in" x2="{end_x}in" y2="{end_y}in" style="{line_style}"/>\n')

def radial_burst(cx, cy, number_of_rays, exterior_radius, interior_offset):
    line_length = exterior_radius - interior_offset
    degree_step = int(360/number_of_rays)
    for a in range(0,360,degree_step):
        interior_x = math.cos(math.radians(a))*interior_offset + cx
        interior_y = math.sin(math.radians(a))*interior_offset + cy
        line_at_angle(interior_x, interior_y, line_length, a)

line_style = "stroke:rgb(200,200,200);stroke-width:0.5"

width_in = 8.5
height_in = 11
divisions_per_inch = 5
burst_number = 6


save_file_directory = "papers"
save_file_name = "radial_line_verts_" + str(burst_number) + "_radials"
save_file_full_path = save_file_directory + "/" + save_file_name


#burst_height = 2*(1/5)
#burst_width = burst_height


x_spacing = 2*1/divisions_per_inch
y_spacing = x_spacing
offsetX = 0
offsetY = 0
x_count = int(width_in/x_spacing)-1
y_count = int(height_in/y_spacing)-1




f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write(f'<svg width="{width_in}in" height="{height_in}in" xmlns="http://www.w3.org/2000/svg">\n')

f.write('<g id="radial burst mesh" transform="translate(%s, %s)">\n' % ("0", "0"))

for y in range(1,y_count):
    y_cord = offsetY+(y*(y_spacing))
    for x in range(1, x_count):
        x_cord = offsetX+(x*(x_spacing))
        radial_burst(x_cord, y_cord, burst_number, x_spacing/2 , 0)

f.write('\t</g>\n') #end grid
f.write('</svg>')
f.close()
