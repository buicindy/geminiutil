# Small utilities scripts

def parse_binning_information(binning_information):
  """ This function parses binning information, given as a string (e.g. "2 2"),
  to to two ints (2, 2).
  """

  # Split the string & convert to integers to be returned 
  x_binning, y_binning = (int(n) for n in binning_information.split())
  
  return x_binning, y_binning
