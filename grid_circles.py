width_in = 8.5
height_in = 11
divisions_per_inch = 5
offsetX = 0
offsetY = 0
padding = 0.015625
tight_packed = True
#radius = 0.015625#1/64th

save_file_directory = "papers"
if tight_packed:
    save_file_name = "packed_circles_" + str(divisions_per_inch) + "_per_inch"
else:
    save_file_name = "grid_circles_" + str(divisions_per_inch) + "_per_inch"
save_file_full_path = save_file_directory + "/" + save_file_name
#margin = 0.5
#spacing = radius*2 + margin
x_spacing = 1/divisions_per_inch
y_spacing = x_spacing
radius = (x_spacing/2)-padding
x_count = int(width_in * divisions_per_inch)
y_count = int(height_in * divisions_per_inch)
trace_style = "stroke: rgb(200,200,200); fill: none;"

f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write(f'<svg width="{width_in}in" height="{height_in}in"  xmlns="http://www.w3.org/2000/svg">\n')

for row in range(1,y_count):
    y_cord = offsetY+(row*(y_spacing))
    for col in range(1, x_count):
        x_cord = offsetX+(col*(x_spacing))
        if tight_packed:
            x_cord = x_cord + (row%2 * x_spacing/2)
        f.write(f'\t<circle cx="{x_cord}in" cy="{y_cord}in" r="{radius}in" style="{trace_style}"/>\n')

f.write('</svg>')
f.close()
