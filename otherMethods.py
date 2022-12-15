# Code written by F226093
# Method for generating random time
from datetime import datetime
from datetime import timedelta
import random
def createRandomTime(start, end):
    diff = end - start
    allSeconds = diff.total_seconds()
    randomSecond = random.randrange(allSeconds)
    return start + timedelta(seconds=randomSecond)