import math
import random
error_ratio = 0.1
# num_of_chunk = how many chunks you have in your file if your file is 5Kib and packet size is 100bytes
def error_or_not(num_of_chunk): # num_of_chunk = 5Kib / 100bytes
    sq = int(math.sqrt(num_of_chunk))
    ra = random.randrange(0,sq)
    if(ra <= sq*error_ratio):
        return True # there is an error
    return False# there is no error

