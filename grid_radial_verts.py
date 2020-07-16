import math


def line_at_angle(x, y, my_radius, my_angle):
    end_x = math.cos(math.radians(my_angle))*my_radius + x
    end_y = math.sin(math.radians(my_angle))*my_radius + y
    f.write(f'\t\t<line x1="{x}" y1="{y}" x2="{end_x}" y2="{end_y}" style="{line_style}"/>\n')

def radial_burst(cx, cy, number_of_rays, exterior_radius, interior_offset):
    line_length = exterior_radius - interior_offset
    degree_step = int(360/number_of_rays)
    f.write(f'\t<g>\n')
    for a in range(0,360,degree_step):
        interior_x = math.cos(math.radians(a))*interior_offset + cx
        interior_y = math.sin(math.radians(a))*interior_offset + cy
        line_at_angle(interior_x, interior_y, line_length, a)
    f.write(f'\t</g>\n')

line_style = "stroke:rgb(100,100,100);stroke-width:1"

pxPerInch = 300
width_in = 8.5
height_in = 11
viewBoxWidth = width_in * pxPerInch
viewBoxHeight = height_in * pxPerInch

tight_packed = True

intervals_per_inch = 5
x_spacing = pxPerInch/intervals_per_inch
y_spacing = x_spacing
offsetX = 0
offsetY = 0
x_count = int(viewBoxWidth/x_spacing)-1
y_count = int(viewBoxHeight/y_spacing)-1

number_of_verts = 6
vert_radius = x_spacing/3


save_file_directory = "papers"
save_file_name = "test2_radial_line_verts_" + str(number_of_verts) + "_radials"
if tight_packed:
    save_file_name = save_file_name + "_tp"
save_file_full_path = save_file_directory + "/" + save_file_name


#burst_height = 2*(1/5)
#burst_width = burst_height







f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))

f.write('<g id="radial burst mesh" transform="translate(%s, %s)">\n' % ("0", "0"))

for row in range(1,y_count):
    y_cord = offsetY+(row*(y_spacing))
    for col in range(1, x_count):
        x_cord = offsetX+(col*(x_spacing))
        if tight_packed:
            x_cord = x_cord + (row%2 * x_spacing/2)
        radial_burst(x_cord, y_cord, number_of_verts, vert_radius , 0)

f.write('\t</g>\n') #end grid
f.write('</svg>')
f.close()
