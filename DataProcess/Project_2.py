import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():

    root = "/Users/yifuhhh/TFT_Projects/Prj_2/Data"
    files = os.listdir(root)
    files_IdVd = list(filter(lambda x: x[0 : 8]=='tftexOut', files))
    file_1 = "tftexTransfer_Neg.csv"
    file_2 = "tftexTransfer_Pos.csv"
    plot_Q1(root, file_1, file_2)
    plot_Q2(root, files_IdVd)


if __name__ == "__main__":
main()
