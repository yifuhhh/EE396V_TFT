import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():

    root = "/Users/yifuhhh/TFT_Projects/Prj_1/Data"
    files = os.listdir(root)
    files_IdVd = list(filter(lambda x: x[0 : 8]=='tftexOut', files))
    file_1 = "tftexTransfer_Neg.csv"
    file_2 = "tftexTransfer_Pos.csv"
    plot_Q1(root, file_1, file_2)
    plot_Q2(root, files_IdVd)


def plot_Q1(root, file_1, file_2):

    df = pd.read_csv(root + '/' + file_1)
    # print(df_1.columns.values.tolist())
    # print(df_1.head())
    # print(df.tail())
    tmp = np.array(df)
    Vg = np.arange(152).reshape(152, 1)
    Vg.dtype = np.float
    Id = np.arange(152).reshape(152, 1)
    Id.dtype = np.float
    Vg[0 : 50, 0] = tmp[50 : 0 : -1, 0]
    Id[0 : 50, 0] = tmp[50 : 0 : -1, 8]
    Vg[50, 0] = tmp[0, 0]
    Id[50, 0] = tmp[0, 8]

    df = pd.read_csv(root + '/' + file_2)
    tmp = np.array(df)
    Vg[51 : 151, 0] = tmp[0 : 100, 0]
    Id[51 : 151, 0] = tmp[0 : 100, 8]

    # print(Vg[100 : 151, 0])
    parameter = np.polyfit(Vg[100 : 151, 0], Id[100 : 151, 0], 1)
    f = np.poly1d(parameter)
    print(parameter)

    plt.figure(1)
    plt.plot (Vg[0 : 151, 0], Id[0 : 151, 0], color = 'royalblue', linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Transfer curve', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig1.png')
    plt.show()

    plt.figure(3)
    plt.plot (Vg[0 : 151, 0], Id[0 : 151, 0], color = 'royalblue', linewidth = 2)
    plt.plot(Vg[61 : 151, 0], f(Vg[61 : 151, 0]), "r--", linewidth = 1.5)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Transfer curve', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig3.png')
    plt.show()


def plot_Q2(root, files_IdVd):

    data = np.arange(902).reshape(41, 22)
    data.dtype = np.float
    for file in files_IdVd:
        Vg = int(file[-5])
        if file[-6] == '1':
            Vg = Vg + 10
        else:
            if file[-6] == '2':
                Vg = Vg + 20
        tmp = pd.read_csv(root + '/' + file)
        tmp = np.array(tmp)
        data[:, 21] = tmp [:, 6]
        data[:, Vg] = tmp[:, 8]

    plt.figure(2)
    plt.plot (data[:, 21], data[:, 4], linewidth = 2, label = "Vgs = +4V")
    plt.plot (data[:, 21], data[:, 8], linewidth = 2, label = "Vgs = +8V")
    plt.plot (data[:, 21], data[:, 12], linewidth = 2, label = "Vgs = +12V")
    plt.plot (data[:, 21], data[:, 16], linewidth = 2, label = "Vgs = +16V")
    plt.plot (data[:, 21], data[:, 20], linewidth = 2, label = "Vgs = +20V")
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

    plt.figure(4)
    i = 0
    p = np.arange(42).reshape(21, 2)
    p.dtype = np.float
    while i < 21:
        p[i, :] = np.polyfit(data[0 : 5, 21], data[0 : 5, i], 1)
        f = np.poly1d(p[i, :])
        plt.plot(data[0 : 5, 21], f(data[0 : 5, 21]), linewidth = 1.5, label = "Vgs = " + str(i) + "V")
        i = i + 1
    print(p[:, 0])
    plt.title('Output conductance', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vds (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':8})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig4.png')
    plt.show()

    plt.figure(5)
    i = 3
    ZL = 6
    Cg = 0.0003453133249
    Vt = 2.233457612
    u_eff = np.arange(42).reshape(21, 2)
    u_eff.dtype = np.float
    while i < 21:
        u_eff[i, 1] = p[i, 0]/(ZL * Cg * (i - Vt))
        u_eff[i, 0] = i
        i = i + 1
    plt.plot(u_eff[3:, 0], u_eff[3:, 1], linewidth = 1.5, label = "Mobility")
    plt.title('Mobility', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Mobility (m^2/(V*s))', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    # plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':8})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_1/Plots/Fig5.png')
    plt.show()



if __name__ == "__main__":
    main()
