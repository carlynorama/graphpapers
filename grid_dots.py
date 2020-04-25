centerX = 10
centerY = 10
radius = 3
style = "fill:rgb(200,200,255);"

f = open('helloworld.svg','w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write('<svg width="8.5in" height="11in" xmlns="http://www.w3.org/2000/svg">\n')

for y in range(0,20):
    y_cord = centerY+(y*((radius*2)+5))
    for x in range(0, 12):
        x_cord = centerX+(x*((radius*2)+5))
        f.write(f'\t<circle cx="{x_cord}" cy="{y_cord}" r="{radius}" style="{style}"/>\n')

f.write('</svg>')
f.close()
