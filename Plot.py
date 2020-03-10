import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():

## Data processing for Project 1
    root = "/Users/yifuhhh/TFT_Projects/Prj_1"
    file_1 = "tftexTransfer_Neg.csv"
    file_2 = "tftexTransfer_Pos.csv"
    file_3 = "tftexOut_2.csv"
    file_4 = "tftexOut_3.csv"
    file_5 = "tftexOut_4.csv"
    file_6 = "tftexOut_5.csv"
    file_7 = "tftexOut_6.csv"

    df = pd.read_csv(root + '/' + file_1)
    # print(df_1.columns.values.tolist())
    # print(df_1.head())
    print(df.tail())
    tmp = np.array(df)
    Vg = np.arange(152).reshape(152, 1)
    Vg.dtype = np.float
    Id = np.arange(152).reshape(152, 1)
    Id.dtype = np.float
    Vg[0 : 50, 0] = tmp[50 : 0 : -1, 0]
    Id[0 : 50, 0] = tmp[50 : 0 : -1, 8]
    Vg[50, 0] = 0
    Id[50, 0] = tmp[0, 8]

    df = pd.read_csv(root + '/' + file_2)
    tmp = np.array(df)
    Vg[51 : 151, 0] = tmp[0 : 100, 0]
    Id[51 : 151, 0] = tmp[0 : 100, 8]

    print(Vg)

    plt.plot (Vg[0 : 151, 0], Id[0 : 151, 0], color = 'orangered', linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Transfer curve', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig1.png')
    plt.show()


    df = pd.read_csv(root + '/' + file_3)
    tmp = np.array(df)
    Vd = tmp[0 : 40, 6]
    Id_4 = tmp[0 : 40, 8]

    df = pd.read_csv(root + '/' + file_4)
    tmp = np.array(df)
    Id_8 = tmp[0 : 40, 8]

    df = pd.read_csv(root + '/' + file_5)
    tmp = np.array(df)
    Id_12 = tmp[0 : 40, 8]

    df = pd.read_csv(root + '/' + file_6)
    tmp = np.array(df)
    Id_16 = tmp[0 : 40, 8]

    df = pd.read_csv(root + '/' + file_7)
    tmp = np.array(df)
    Id_20 = tmp[0 : 40, 8]

    plt.plot (Vd, Id_4, linewidth = 2, label = "Vgs = +4V")
    plt.plot (Vd, Id_8, linewidth = 2, label = "Vgs = +8V")
    plt.plot (Vd, Id_12, linewidth = 2, label = "Vgs = +12V")
    plt.plot (Vd, Id_16, linewidth = 2, label = "Vgs = +16V")
    plt.plot (Vd, Id_20, linewidth = 2, label = "Vgs = +20V")
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Output curve', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vds (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig2.png')
    plt.show()


if __name__ == "__main__":
    main()
