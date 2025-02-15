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
    trap_bulk = list(filter(lambda x: x[0 : 4]=='bulk', files_2))

    files_3 = os.listdir(root_3)
    transferNeg_3 = list(filter(lambda x: x[14 : 17]=='Neg', files_3))
    transferPos_3 = list(filter(lambda x: x[14 : 17]=='Pos', files_3))
    trap_bulk_acc = list(filter(lambda x: x[0 : 8]=='bulk_acc', files_3))
    trap_bulk_don = list(filter(lambda x: x[0 : 8]=='bulk_don', files_3))

    files_4 = os.listdir(root_4)
    transferNeg_4 = list(filter(lambda x: x[14 : 17]=='Neg', files_4))
    transferPos_4 = list(filter(lambda x: x[14 : 17]=='Pos', files_4))

    plot_trap_1(root_1, trap_int, name_1)
    plot_trap_2(root_2, trap_bulk_acc, trap_bulk_don, name_2)
    plot_trap_2(root_3, trap_bulk_acc, trap_bulk_don, name_3)

    plot_transfer(root_1, transferNeg_1, transferPos_1, name_1)
    plot_transfer(root_2, transferNeg_2, transferPos_2, name_2)
    plot_transfer(root_3, transferNeg_3, transferPos_3, name_3)
    plot_transfer(root_4, transferNeg_4, transferPos_4, name_4)


def plot_trap_1(root, files, name):

    sweep_label = ['nta = 0.5e12', 'nta = 2e12', 'nta = 8e12']
    energy = np.zeros((24, 3), dtype = float)
    trap = np.zeros((24, 3), dtype = float)

    for file in files:
        num = int(file[-5])
        tmp = pd.read_table(root + '/' + file, header = None, skiprows = 17)
        tmp = np.array(tmp)
        s = np.size(tmp)
        i = 0
        while i < s:
            energy[i, num - 1] = float(tmp[i][0][4 : 16])
            trap[i, num - 1] = float(tmp[i][0][46 : 58])
            i = i + 1

    ## Plot trap density for interface sweep
    plt.figure(5, figsize = (10, 8))
    i = 0
    while i < 3:
        plt.plot (energy[:, i], trap[:, i], linewidth = 2, label = sweep_label[i])
        i = i + 1
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_yscale("log")
    plt.title('Trap density for sweep of ' + name, fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('State energy from Ec (eV)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Trap density (cm^-3)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 1, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_2/Plots/' + 'Fig0_' + name + '.png')
    plt.show()


def plot_trap_2(root, files_acc, files_don, name):

    sweep_label = ['nta = 0.5e12', 'nta = 2e12', 'nta = 8e12']
    energy = np.zeros((64, 3), dtype = float)
    trap_acc = np.zeros((64, 3), dtype = float)
    trap_don = np.zeros((64, 3), dtype = float)
    trap = np.zeros((64, 3), dtype = float)

    for file_d in files_don:
        num = int(file_d[-5])
        file_a = 'a'
        for file_tmp in files_acc:
            if int(file_tmp[-5]) == num:
                file_a = file_tmp
        tmp_d = pd.read_table(root + '/' + file_d, header = None, skiprows = 17)
        tmp_d = np.array(tmp_d)
        tmp_a = pd.read_table(root + '/' + file_a, header = None, skiprows = 17)
        tmp_a = np.array(tmp_a)
        s_d = np.size(tmp_d)
        s_a = np.size(tmp_a)
        # print(s_d)
        i = 0
        while i < s_d:
            energy[i, num - 1] = float(tmp_d[i][0][4 : 16])
            trap_don[i, num - 1] = float(tmp_d[i][0][46 : 58])
            j = 0
            while j < s_a:
                if tmp_a[j][0][4 : 16] == tmp_d[i][0][4 : 16]:
                    trap_acc[s_d - i - 1, num - 1] = float(tmp_a[j][0][46 : 58])
                j = j + 1
            i = i + 1
        i = 0
        while i < s_d:
            trap[i, num - 1] = trap_acc[i, num - 1] + trap_don[i, num - 1]
            i = i + 1

    print(trap_don)
    print(trap_acc)

    ## Plot trap density for bulkdeep & bulkshallow sweep
    plt.figure(5, figsize = (10, 8))
    i = 0
    while i < 3:
        plt.plot (energy[:, i], trap[:, i], linewidth = 2, label = sweep_label[i])
        i = i + 1
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_yscale("log")
    plt.title('Trap density for sweep of ' + name, fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('State energy from Ev (eV)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Trap density (cm^-3)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 1, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_2/Plots/' + 'Fig0_' + name + '.png')
    plt.show()


def plot_transfer(root, transferNeg, transferPos, name):

    # print(transferNeg)
    # print(root)
    sweep_label = ['0', '0', '0']
    sweep = np.zeros((1, 3), dtype = np.float)
    Vth = np.zeros((1, 3), dtype = np.float)
    ss = np.zeros((1, 3), dtype = np.float)
    if name == "interface":
        sweep_label[0] = "nta = 0.5e12"
        sweep_label[1] = "nta = 2e12"
        sweep_label[2] = "nta = 8e12"
        sweep[0, 0] = 0.5e12
        sweep[0, 1] = 2e12
        sweep[0, 2] = 8e12
        Vth[0, 0] = 9.6749
        Vth[0, 1] = 10.0399
        Vth[0, 2] = 10.8379
        ss[0, 0] = -0.0632903
        ss[0, 1] = -0.0674847
        ss[0, 2] = -0.132793
        sweep_name = "nta"
    elif name == "bulkshallow":
        sweep_label[0] = "nta & ntd= 0.5e21"
        sweep_label[1] = "nta & ntd= 2e21"
        sweep_label[2] = "nta & ntd= 8e21"
        sweep[0, 0] = 0.5e21
        sweep[0, 1] = 2e21
        sweep[0, 2] = 8e21
        Vth[0, 0] = 7.34496
        Vth[0, 1] = 10.1087
        Vth[0, 2] = 6.91284
        ss[0, 0] = -0.0791958
        ss[0, 1] = -0.078234
        ss[0, 2] = -0.078953
        sweep_name = "nta & ntd"
    elif name == "bulkdeep":
        sweep_label[0] = "ngd = 0.5e16"
        sweep_label[1] = "ngd = 2e16"
        sweep_label[2] = "ngd = 8e16"
        sweep[0, 0] = 0.5e16
        sweep[0, 1] = 2e16
        sweep[0, 2] = 8e16
        Vth[0, 0] = 10.1007
        Vth[0, 1] = 10.0853
        Vth[0, 2] = 10.025
        ss[0, 0] = -0.0800555
        ss[0, 1] = -0.0539751
        ss[0, 2] = -0.0934905
        sweep_name = "ngd"
    else:
        sweep_label[0] = "Channel length = 15 um"
        sweep_label[1] = "Channel length = 30 um"
        sweep_label[2] = "Channel length = 60 um"
        sweep[0, 0] = 15
        sweep[0, 1] = 30
        sweep[0, 2] = 60
        Vth[0, 0] = 10.0271
        Vth[0, 1] = 10.0399
        Vth[0, 2] = 10.0463
        ss[0, 0] = -0.0807894
        ss[0, 1] = -0.0674847
        ss[0, 2] = -0.0773198
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

    ## Plot transfer curve, linear scale
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

    ## Plot transfer curve, log scale
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

    ## Plot threshold voltage
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

    ## Plot subthreshold swing
    plt.figure(4, figsize = (10, 8))
    plt.plot (sweep[0, :], ss[0, :], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_xscale("log")
    plt.title('Subthreshold swing for sweep of ' + name, fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel(sweep_name, fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Subthreshold swing (V/decade)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    # plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/Prj_2/Plots/' + 'Fig4_' + name + '.png')
    plt.show()


if __name__ == "__main__":
    main()
