

def main():
    #  import data from txt file
    with open("input.txt", 'r') as file:
        input = file.readlines()
        

    formatted = format_info(input)
    surface_area = calc_surface_area(formatted)
    extra_paper = calc_extra_paper(formatted)
    wrapping_paper_needed = calc_total_paper(surface_area, extra_paper)

    print(f'surface_area: {surface_area}, extra: {extra_paper}, Total needed: {wrapping_paper_needed}')
   



def format_info(data):

    dimensions = []
    for x in data:
        # split items in list removing x
        new_list = x.strip().split('x')

        # convert each measurement into integer
        dimensions.append(list(map(int, new_list)))

    return dimensions


def calc_surface_area(data):

    surface_area_list = []
   
    for l, w, h in data:
        surface_area_list.append(2 * ((l * w) + (w * h) + (h * l))) 

    surface_area_sum = sum(surface_area_list)
    return surface_area_sum

    
def calc_extra_paper(data):

    areas = []

    while data:
        smallest = data.pop(0)
        smallest_side = sorted(smallest)
        area = (smallest_side[0] * smallest_side[1])
        areas.append(area)

    area_sum = sum(areas)
    return area_sum

def calc_total_paper(surface, smallest_side):
    return surface + smallest_side



if __name__ == "__main__":
    main()