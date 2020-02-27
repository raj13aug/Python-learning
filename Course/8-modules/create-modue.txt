
# If program grow should split our code across multiple files.
# A module is a file that contains some python code.


##################### Method 1 #####################

import sales
from sales import cal_shipping, calc_tax

cal_shipping()
calc_tax()

###############   Method 2   ###################################

sales.cal_shipping

# Basically you can either import the entire module as an object or your import specific objects from that modules
