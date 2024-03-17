import math

def paint_calc(height, width, cover):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  print(f"You' ll need {round_up_cans} cans of paint. ")



test_h = int(input("Enter the height of the wall")) # Height of wall (m)
test_w = int(input("Enter the width of the wall")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)