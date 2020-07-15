width_in = 8.5
height_in = 11
divisions_per_inch = 5
offsetX = 0
offsetY = 0
#radius = 0.015625#1/64th

save_file_directory = "papers"
save_file_name = "circles_" + str(divisions_per_inch) + "_per_inch"
save_file_full_path = save_file_directory + "/" + save_file_name
#margin = 0.5
#spacing = radius*2 + margin
x_spacing = 1/divisions_per_inch
y_spacing = x_spacing
radius = x_spacing/2
x_count = int(width_in * divisions_per_inch)
y_count = int(height_in * divisions_per_inch)
trace_style = "stroke: rgb(200,200,200); fill: none;"

f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write(f'<svg width="{width_in}in" height="{height_in}in"  xmlns="http://www.w3.org/2000/svg">\n')

for y in range(1,y_count):
    y_cord = offsetY+(y*(y_spacing))
    for x in range(1, x_count):
        x_cord = offsetX+(x*(x_spacing))
        f.write(f'\t<circle cx="{x_cord}in" cy="{y_cord}in" r="{radius}in" style="{trace_style}"/>\n')

f.write('</svg>')
f.close()
