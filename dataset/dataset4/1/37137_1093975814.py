val = mean(vals)
bad_vals = sum([val < 0.0 or val > 1.0 for val in vals])