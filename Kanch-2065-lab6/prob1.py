"""
Kanch Ruansiripiyakul 633040206-5
"""
tuple = (2, 123.4567, 10000, 12345.67)
text = "file_{0:03d}:  {1:.2f}, {2:.2e}, {3:.3e}".format(
    tuple[0], tuple[1], tuple[2], tuple[3])
print(text)
