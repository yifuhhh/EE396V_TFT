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
    # print(df_1.tail())
    tmp = np.array(df)
    Vg = tmp[0 : 50, 0]
    Id = tmp[0 : 50, 8]

    plt.plot (Vg, Id, color = 'orangered', linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    plt.title('Transfer curve (negative)', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig1.png')
    plt.show()


    df = pd.read_csv(root + '/' + file_2)
    tmp = np.array(df)
    Vg= tmp[0 : 50, 0]
    Id = tmp[0 : 50, 8]

    plt.plot (Vg, Id, color = 'orangered', linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    plt.title('Transfer curve (Positive)', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig2.png')
    plt.show()


    df = pd.read_csv(root + '/' + file_3)
    tmp = np.array(df)
    Vd = tmp[0 : 40, 6]
    Id_4 = tmp[0 : 40, 8]

    plt.plot (Vd, Id_4, color = 'orangered', linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    plt.title('Output curve, Vgs = +4V', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vds (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig3.png')
    plt.show()


    df = pd.read_csv(root + '/' + file_4)
    tmp = np.array(df)
    Vd = tmp[0 : 40, 6]
    Id_8 = tmp[0 : 40, 8]

    plt.plot (Vd, Id_8, color = 'orangered', linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    plt.title('Output curve, Vgs = +8V', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vds (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig4.png')
    plt.show()


    df = pd.read_csv(root + '/' + file_5)
    tmp = np.array(df)
    Vd = tmp[0 : 40, 6]
    Id_12 = tmp[0 : 40, 8]

    plt.plot (Vd, Id_12, color = 'orangered', linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    plt.title('Output curve, Vgs = +12V', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vds (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig5.png')
    plt.show()


    df = pd.read_csv(root + '/' + file_6)
    tmp = np.array(df)
    Vd = tmp[0 : 40, 6]
    Id_16 = tmp[0 : 40, 8]

    plt.plot (Vd, Id_16, color = 'orangered', linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    plt.title('Output curve, Vgs = +16V', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vds (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig6.png')
    plt.show()


    df = pd.read_csv(root + '/' + file_7)
    tmp = np.array(df)
    Vd = tmp[0 : 40, 6]
    Id_20 = tmp[0 : 40, 8]

    plt.plot (Vd, Id_20, color = 'orangered', linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    plt.title('Output curve, Vgs = +20V', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vds (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig7.png')
    plt.show()


    plt.plot (Vd, Id_4, linewidth = 2, label = "Vgs = +4V")
    plt.plot (Vd, Id_8, linewidth = 2, label = "Vgs = +8V")
    plt.plot (Vd, Id_12, linewidth = 2, label = "Vgs = +12V")
    plt.plot (Vd, Id_16, linewidth = 2, label = "Vgs = +16V")
    plt.plot (Vd, Id_20, linewidth = 2, label = "Vgs = +20V")
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0,1))
    plt.title('Output curve comparison', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vds (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig8.png')
    plt.show()


if __name__ == "__main__":
    main()
