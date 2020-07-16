import math


def draw_polar_line(origin_x, origin_y, radius, rad_angle):
    end_x = math.cos(rad_angle)*radius + origin_x
    end_y = math.sin(rad_angle)*radius + origin_y
    f.write(f'\t\t<line x1="{origin_x}" y1="{origin_y}" x2="{end_x}" y2="{end_y}" style="{line_style}"/>\n')

def draw_hypotanuse(origin_x, origin_y, height, width):
    start_x = origin_x
    start_y = side1 + origin_y
    end_x = origin_x + width
    end_y = origin_y
    f.write(f'\t\t<line x1="{start_x}" y1="{start_y}" x2="{end_x}" y2="{end_y}" style="{line_style}"/>\n')

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False



# def radial_burst(cx, cy, number_of_rays, exterior_radius, interior_offset):
#     line_length = float(exterior_radius) - float(interior_offset)
#     degree_step = float(float(360)/number_of_rays)
#     f.write(f'\t<g>\n')
#     for a in range(0, number_of_rays):
#         radians = math.radians(float(a)*degree_step) + radial_offset
#         interior_x = math.cos(radians)*float(interior_offset) + float(cx)
#         interior_y = math.sin(radians)*float(interior_offset) + float(cy)
#         line_at_angle(float(interior_x), float(interior_y), float(line_length), radians)
#     f.write(f'\t</g>\n')

line_style = "stroke:rgb(100,100,100);stroke-width:1"

pxPerInch = float(300)
width_in = float(8.5)
height_in = float(11)
viewBoxWidth = width_in * pxPerInch
viewBoxHeight = height_in * pxPerInch

tight_packed = True

intervals_per_inch = float(5)
x_spacing = float(pxPerInch/intervals_per_inch)
y_spacing = float(x_spacing)
offsetX = float(0)
offsetY = float(0)
x_count = int(viewBoxWidth/x_spacing)
y_count = int(viewBoxHeight/y_spacing)

number_of_lines = 3
line_angles = [math.radians(60), math.radians(-60), math.radians(0) ]
line_spacings = [x_spacing, x_spacing, x_spacing]
line_offsets = [0, 0, 0]
bounding_rect = [200, 200, viewBoxWidth-200, viewBoxHeight-200]


save_file_directory = "papers"
save_file_name = "lined_" + str(number_of_lines) + "_lines"

save_file_full_path = save_file_directory + "/" + save_file_name







f = open('%s.svg' % save_file_full_path, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))

f.write('<g id="graph mesh" transform="translate(%s, %s)">\n' % ("0", "0"))



for a in line_angles:
    draw_polar_line(bounding_rect[0], bounding_rect[1], viewBoxWidth, a)

L1 = line([0,1], [2,3])
L2 = line([2,3], [0,4])

R = intersection(L1, L2)
if R:
    print("Intersection detected:", R)
else:
    print("No single intersection point detected")


f.write('\t</g>\n') #end grid
f.write('</svg>')
f.close()
