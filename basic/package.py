# import travel.thailand

# trip_to = travel.thailand.ThailandPacakage()
# trip_to.detail()

# print("================================================")

# from travel.thailand import ThailandPacakage

# trip_to = ThailandPacakage()
# trip_to.detail()

# print("================================================")

# from travel import vietnam

# trip_to = vietnam.VietnamPacakage()
# trip_to.detail()

# print("================================================")

from travel import *

# trip_to = vietnam.VietnamPacakage()
# trip_to = thailand.ThailandPacakage()
# trip_to.detail()

# print("================================================")

import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))
