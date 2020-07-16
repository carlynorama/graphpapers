import math

width_in = 8.5
height_in = 11
cicles_per_revolution = 4
degree_step = int(360/cicles_per_revolution)
radial_offset = 0
offsetX = 0.25
offsetY = 0.25
centerX = width_in/2
centerY = height_in/2
ext_radius = ((width_in- offsetX)/2)/2
int_radius = 0
radius = ext_radius - int_radius
x_cord = centerX
y_cord = centerY


def line_at_angle(x, y, my_radius, angle):
    end_x = math.cos(math.radians(angle))*my_radius + x
    end_y = math.sin(math.radians(angle))*my_radius + y
    f.write(f'\t<line x1="{x}in" y1="{y}in" x2="{end_x}in" y2="{end_y}in" style="{trace_style}"/>\n')


#radius = 0.015625#1/64th

save_file_directory = "papers"
save_file_name = "radial_lines_" + str(cicles_per_revolution) + "_per_cicle_" + str(int(ext_radius)) + "_ext_" + str(int(int_radius)) + "_int"
save_file_full_path = save_file_directory + "/" + save_file_name

trace_style = "stroke: rgb(200,200,200); fill: none;"

f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write(f'<svg width="{width_in}in" height="{height_in}in"  xmlns="http://www.w3.org/2000/svg">\n')

for a in range(0,360,degree_step):
    circle_edge_x = math.cos(math.radians(a))*int_radius + centerX
    circle_edge_y = math.sin(math.radians(a))*int_radius + centerY
    line_at_angle(circle_edge_x, circle_edge_y, radius, a)

f.write('</svg>')
f.close()
