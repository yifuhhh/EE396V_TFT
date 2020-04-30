import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():

    root_1 = "/Users/yifuhhh/TFT_Projects/Prj_2/Data/prg_1_interface"
    root_2 = "/Users/yifuhhh/TFT_Projects/Prj_2/Data/prg_2_bulkshallow"
    root_3 = "/Users/yifuhhh/TFT_Projects/Prj_2/Data/prg_3_bulkdeep"
    root_4 = "/Users/yifuhhh/TFT_Projects/Prj_2/Data/prg_4_channel"

    name_1 = "interface"
    name_2 = "bulkshallow"
    name_3 = "bulkdeep"
    name_4 = "channel"

    files_1 = os.listdir(root_1)
    transferNeg_1 = list(filter(lambda x: x[14 : 17]=='Neg', files_1))
    transferPos_1 = list(filter(lambda x: x[14 : 17]=='Pos', files_1))
    trap_int = list(filter(lambda x: x[0 : 3]=='int', files_1))

    files_2 = os.listdir(root_2)
    transferNeg_2 = list(filter(lambda x: x[14 : 17]=='Neg', files_2))
    transferPos_2 = list(filter(lambda x: x[14 : 17]=='Pos', files_2))

    files_3 = os.listdir(root_3)
    transferNeg_3 = list(filter(lambda x: x[14 : 17]=='Neg', files_3))
    transferPos_3 = list(filter(lambda x: x[14 : 17]=='Pos', files_3))

    files_4 = os.listdir(root_4)
    transferNeg_4 = list(filter(lambda x: x[14 : 17]=='Neg', files_4))
    transferPos_4 = list(filter(lambda x: x[14 : 17]=='Pos', files_4))

    plot_trap_1(root_1, trap_int, name_1)

    # plot_transfer(root_1, transferNeg_1, transferPos_1, name_1)
    # plot_transfer(root_2, transferNeg_2, transferPos_2, name_2)
    # plot_transfer(root_3, transferNeg_3, transferPos_3, name_3)
    # plot_transfer(root_4, transferNeg_4, transferPos_4, name_4)

    # c = pd.read_table(file_1, header = None, skiprows = 17)

def plot_trap_1(root, files, name):

    sweep_label = ['nta = 0.5e12', 'nta = 2e12', 'nta = 8e12']
    X = np.zeros((24, 3), dtype = float)
    trap = np.zeros((24, 3), dtype = float)

    for file in files:
        num = int(file[-5])
        tmp = pd.read_table(root + '/' + file, header = None, skiprows = 17)
        tmp = np.array(tmp)
        s = np.size(tmp)
        i = 0
        while i < s:
            X[i, num - 1] = float(tmp[i][0][4 : 16])
            trap[i, num - 1] = float(tmp[i][0][18 : 30])
            i = i + 1

    plt.figure(5, figsize = (10, 8))
    i = 0
    while i < 3:
        plt.plot (X[:, i], trap[:, i], linewidth = 2, label = sweep_label[i])
        i = i + 1
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_yscale("log")
    plt.title('Trap density for sweep of ' + name, fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Position (um)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Trap density (cm^-3)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_2/Plots/' + 'Fig0_' + name + '.png')
    plt.show()


def plot_transfer(root, transferNeg, transferPos, name):

    # print(transferNeg)
    # print(root)
    sweep_label = ['0', '0', '0']
    Vth = np.zeros((1, 3), dtype = np.float)
    sweep = np.zeros((1, 3), dtype = np.float)
    if name == "interface":
        sweep_label[0] = "nta = 0.5e12"
        sweep_label[1] = "nta = 2e12"
        sweep_label[2] = "nta = 8e12"
        sweep[0, 0] = 0.5e12
        sweep[0, 1] = 2e12
        sweep[0, 2] = 8e12
        sweep_name = "nta"
    elif name == "bulkshallow":
        sweep_label[0] = "nta & ntd= 0.5e21"
        sweep_label[1] = "nta & ntd= 2e21"
        sweep_label[2] = "nta & ntd= 8e21"
        sweep[0, 0] = 0.5e21
        sweep[0, 1] = 2e21
        sweep[0, 2] = 8e21
        sweep_name = "nta & ntd"
    elif name == "bulkdeep":
        sweep_label[0] = "ngd = 0.5e16"
        sweep_label[1] = "ngd = 2e16"
        sweep_label[2] = "ngd = 8e16"
        sweep[0, 0] = 0.5e16
        sweep[0, 1] = 2e16
        sweep[0, 2] = 8e16
        sweep_name = "ngd"
    else:
        sweep_label[0] = "Channel length = 15 um"
        sweep_label[1] = "Channel length = 30 um"
        sweep_label[2] = "Channel length = 60 um"
        sweep[0, 0] = 15
        sweep[0, 1] = 30
        sweep[0, 2] = 60
        sweep_name = "Channel length"

    Vg = np.zeros((160, 3), dtype = np.float)
    Id = np.zeros((160, 3), dtype = np.float)
    row = np.zeros((1, 3), dtype = np.integer)
    # parameter = np.zeros((1, 3), dtype = np.float)

    for file in transferNeg:
        num = int(file[-5])
        # para = 2^(2 * num - 3)
        tmp = pd.read_csv(root + '/' + file)
        tmp = np.array(tmp)
        r = tmp.shape[0] - 1
        row[0, num - 1] = r
        Vg[59 : 59 - r : -1, num - 1] = tmp[0 : r, 0]
        Id[59 : 59 - r : -1, num - 1] = tmp[0 : r, 8]

    for file in transferPos:
        num = int(file[-5])
        # para = 2^(2 * num - 3)
        tmp = pd.read_csv(root + '/' + file)
        tmp = np.array(tmp)
        Vg[60 :, num - 1] = tmp[:, 0]
        Id[60 :, num - 1] = tmp[:, 8]
        parameter = np.polyfit(Vg[100 :, num - 1], Id[100 :, num - 1], 1)
        f = np.poly1d(parameter)
        Vth[0, num - 1] = f.r
        # print(f)

    # print(Vth)

    plt.figure(1, figsize = (10, 8))
    i = 0
    while i < 3:
        r = row[0, i]
        plt.plot (Vg[60 - r :, i], Id[60 - r :, i], linewidth = 2, label = sweep_label[i])
        # plt.plot(Vg[61 :, 0], f(Vg[61 :, 0]), "r--", linewidth = 1.5)
        i = i + 1
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Transfer curve for sweep of ' + name, fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_2/Plots/' + 'Fig1_' + name + '.png')
    plt.show()

    plt.figure(2, figsize = (10, 8))
    i = 0
    while i < 3:
        r = row[0, i]
        plt.plot (Vg[60 - r :, i], Id[60 - r :, i], linewidth = 2, label = sweep_label[i])
        i = i + 1
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_yscale("log")
    plt.title('Transfer curve for sweep of ' + name, fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_2/Plots/' + 'Fig2_' + name + '.png')
    plt.show()

    plt.figure(3, figsize = (10, 8))

    plt.plot (sweep[0, :], Vth[0, :], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_xscale("log")
    plt.title('Threshold voltage for sweep of ' + name, fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel(sweep_name, fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Vth (V)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    # plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_2/Plots/' + 'Fig3_' + name + '.png')
    plt.show()


if __name__ == "__main__":
    main()
