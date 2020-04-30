import math

def triangle(origin_x, origin_y):
      A_x = triangle_half_base + origin_x
      A_y = origin_y
      B_x = triangle_side + origin_x
      B_y = origin_y + triangle_height
      C_x = origin_x
      C_y = origin_y + triangle_height

      f.write('\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (A_x, A_y, B_x, B_y, line_style))
      f.write('\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (B_x, B_y, C_x, C_y, line_style))
      f.write('\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (C_x, C_y, A_x, A_y, line_style))

viewBoxWidth = 2550
viewBoxHeight = 3300
#width_in = 8.5
#height_in = 11
divisions_per_inch = 5
offsetX = 0
offsetY = 0

# half an equalteral triangle is a 30-60-90 triangle
# length of base = x
# length of height = x * math.sqrt(3)
# length of hypotenuse = 2x (same as orig side of trianlge)
# height of an equalat. given the side length a -> h = math.sqrt(3) / 2 * a


triangle_side = float(viewBoxWidth/(8.5*divisions_per_inch))
triangle_height = float(float(math.sqrt(3)) * triangle_side * float(0.5))
triangle_half_base = float(triangle_side/2)
home_x = 0
home_y = 0

save_file_directory = "papers"
save_file_name = "triangle_lines_" + str(divisions_per_inch) + "_per_inch"
save_file_full_path = save_file_directory + "/" + save_file_name




line_style = "stroke:rgb(0,0,0);stroke-width:0.5"

f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))

f.write('<g id="triangle mesh" transform="translate(%s, %s)">\n' % ("0", "0"))

for r in range(int(viewBoxHeight/triangle_height)):
    for c in range(int(viewBoxWidth/triangle_side)):
        start_x = float(float(triangle_side*c) + float(r%2 * triangle_half_base))
        start_y = float(triangle_height*r)
        triangle(start_x, start_y)

f.write('\t</g>\n') #end grid
f.write('</svg>')
f.close()
