from calendar import leapdays
from dataclasses import dataclass
import os
from sqlite3 import Timestamp
import pandas as pd
import numpy as np
import pyxdf
import sys

# CORE FUNCTION =>
# Read XDF and transfer it into mp4 video


def main(argv):
    data, header = pyxdf.load_xdf(argv)

    frame_number = []
    timestamp = []
    for i in range(len(data[0]['time_series'])):
        frame_number.append(data[0]['time_series'][i][0])
        timestamp.append(data[0]['time_series'][i][1])
    
    dataframe= {'Frame Number': frame_number, 'TimeStamp': timestamp}
    df = pd.DataFrame(data=dataframe)
    df.to_csv('out.csv')



if __name__ == "__main__":
    if os.path.exists(sys.argv[1]):
        main(sys.argv[1])