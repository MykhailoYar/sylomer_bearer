from Start import comparison_table

# design rules
dim_sr = [100]                          # cutting step, mm
energy = [80, 100]                      # allowed power of bearing, from-to
all_distance = [100, 400]               # allowed distance between bearings, from-to, mm
numbers = 99                            # max possible numbers of bearings
sylomer_type = [28, 42, 55, 110]        # list of SR marks
# sylomer_types = [18, 28, 42, 55, 110, 220, 850, 1200]   # full list of SR marks

# current price euro/m2
price = {18: 155.93, 28: 183.77, 42: 215.33, 55: 258.02, 110: 178.2,
         220: 415.8, 850: 714.66, 1200: 770.35}

# prepare comparison table
comparison_table(dim_sr, all_distance, energy, sylomer_type, numbers, price)
