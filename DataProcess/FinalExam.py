import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def main():
    root_1 = "/Users/yifuhhh/TFT_Projects/FinalExam/Data/TFT_old"
    root_2 = "/Users/yifuhhh/TFT_Projects/FinalExam/Data/ChannelHeight"
    root_3 = "/Users/yifuhhh/TFT_Projects/FinalExam/Data/ChannelLength"
    root_4 = "/Users/yifuhhh/TFT_Projects/FinalExam/Data/DielectricThickness"
    root_5 = "/Users/yifuhhh/TFT_Projects/FinalExam/Data/BestDesign"

    # name_1 = "TFT_old"
    # name_2 = "Height"
    # name_3 = "Length"
    # name_4 = "DielectricThickness"

    files_1 = os.listdir(root_1)
    transferNeg_1 = "transfer_10_Neg.csv"
    transferPos_1 = "transfer_10_Pos.csv"

    files_2 = os.listdir(root_2)
    transferNeg_2 = list(filter(lambda x: x[11 : 14]=='Neg', files_2))
    transferPos_2 = list(filter(lambda x: x[11 : 14]=='Pos', files_2))

    files_3 = os.listdir(root_3)
    transferNeg_3 = list(filter(lambda x: x[11 : 14]=='Neg', files_3))
    transferPos_3 = list(filter(lambda x: x[11 : 14]=='Pos', files_3))

    files_4 = os.listdir(root_4)
    transferNeg_4 = list(filter(lambda x: x[13 : 16]=='Neg', files_4))
    transferPos_4 = list(filter(lambda x: x[13 : 16]=='Pos', files_4))

    files_5 = os.listdir(root_1)
    transferNeg_5 = "transfer_10_Neg.csv"
    transferPos_5 = "transfer_10_Pos.csv"

    solve_1(root_1, transferNeg_1, transferPos_1)
    solve_2(root_2, transferNeg_2, transferPos_2)
    solve_3(root_3, transferNeg_3, transferPos_3)
    solve_4(root_4, transferNeg_4, transferPos_4)
    solve_1(root_5, transferNeg_5, transferPos_5)


def solve_1(root, file_Neg, file_Pos):
    df_N = pd.read_csv(root + '/' + file_Neg)
    tmp_N = np.array(df_N)
    tmp_N = np.flipud(tmp_N)
    s_Neg = int(np.size(tmp_N)/10) - 1
    df_P = pd.read_csv(root + '/' + file_Pos)
    tmp_P = np.array(df_P)
    s_Pos = int(np.size(tmp_P)/10) - 4
    s = s_Neg + s_Pos
    Vg = np.arange(s).reshape(s, 1)
    Vg.dtype = np.float
    Id = np.arange(s).reshape(s, 1)
    Id.dtype = np.float
    Id_log = np.arange(s).reshape(s, 1)
    Id_log.dtype = np.float
    Vg[0 : s_Neg, 0] = tmp_N[1 :, 0]
    Id[0 : s_Neg, 0] = tmp_N[1 :, 8]
    Vg[s_Neg :, 0] = tmp_P[0 : s_Pos, 0]
    Id[s_Neg :, 0] = tmp_P[0 : s_Pos, 8]

    i = 0
    while i < s:
        Id_log[i, 0] = math.log10(Id[i, 0])
        i = i + 1

    plt.figure(1, figsize = (10, 8))
    plt.plot (Vg[:, 0], Id[:, 0], color = 'royalblue', linewidth = 2)
    # plt.plot(Vg[45:, 0], f(Vg[45:, 0]), "r--", linewidth = 1.5)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    # ax.set_yscale("log")
    plt.title('Id - Vg characteristics', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vg (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/Fig0_transfer.png')
    plt.show()

    plt.figure(2, figsize = (10, 8))
    plt.plot (Vg[:, 0], Id_log[:, 0], color = 'royalblue', linewidth = 2)
    # plt.plot(Vg[10 : 18, 0], f_Von(Vg[10 : 18, 0]), "r--", linewidth = 1.5)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    # ax.set_yscale("log")
    plt.title('Id - Vg characteristics', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    # plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/PartA/Fig7_1b_2.png')
    plt.show()

    L = 12.5e-6 # m
    H = 80e-9 # m
    t = 100e-9 # m

    SS = solve_SS(Id_log, Vg, s)
    (J, u_FE) = solve_param(Id, Vg, s, L, H, t)

    print("J = " + str(J))
    print("u_FE = " + str(u_FE))
    print("SS = " + str(SS) + "V/decade")


def solve_2(root, files_Neg, files_Pos):
    L = 50e-6
    H = np.arange(6).reshape(6, 1)
    H.dtype = np.float
    H[0, 0] = 20e-9
    H[1, 0] = 40e-9
    H[2, 0] = 80e-9
    H[3, 0] = 160e-9
    H[4, 0] = 200e-9
    H[5, 0] = 300e-9
    t = 200e-9

    n = np.size(files_Neg)
    J = np.arange(n).reshape(n, 1)
    J.dtype = np.float
    u_FE = np.arange(n).reshape(n, 1)
    u_FE.dtype = np.float
    SS = np.arange(n).reshape(n, 1)
    SS.dtype = np.float

    plt.figure(1, figsize = (10, 8))
    for file_N in files_Neg:
        num = int(file_N[-5])
        df_N = pd.read_csv(root + '/' + file_N)
        tmp_N = np.array(df_N)
        tmp_N = np.flipud(tmp_N)
        s_Neg = int(np.size(tmp_N)/10) - 1
        for f_P in files_Pos:
            if int(f_P[-5]) == num:
                file_P = f_P
        df_P = pd.read_csv(root + '/' + file_P)
        tmp_P = np.array(df_P)
        s_Pos = int(np.size(tmp_P)/10) - 4
        s = s_Neg + s_Pos
        Vg = np.arange(s).reshape(s, 1)
        Vg.dtype = np.float
        Id = np.arange(s).reshape(s, 1)
        Id.dtype = np.float
        Id_log = np.arange(s).reshape(s, 1)
        Id_log.dtype = np.float
        Vg[0 : s_Neg, 0] = tmp_N[1 :, 0]
        Id[0 : s_Neg, 0] = tmp_N[1 :, 8]
        i = 0
        while i < s:
            if Id[i, 0] < 0:
                Id[i, 0] = (Id[i - 1, 0] + Id[i + 1, 0])/2
            i = i + 1
        Vg[s_Neg :, 0] = tmp_P[0 : s_Pos, 0]
        Id[s_Neg :, 0] = tmp_P[0 : s_Pos, 8]
        # print(Id)

        i = 0
        while i < s:
            Id_log[i, 0] = math.log10(Id[i, 0])
            i = i + 1

        lb = "H = " + str(int(H[num - 1, 0] * 1e9)) + " nm"
        plt.plot (Vg[:, 0], Id[:, 0], linewidth = 2, label = lb)

        SS[num - 1] = solve_SS(Id_log, Vg, s)
        (J[num -1], u_FE[num - 1]) = solve_param(Id, Vg, s, L, H[num - 1], t)

    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_yscale("log")
    plt.title('Id - Vg characteristics', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vg (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/Fig1_transfer.png')
    plt.show()

    print(SS)
    print(J)
    print(u_FE)

    H = H * 1000000000

    plt.figure(2, figsize = (10, 8))
    plt.plot (H[:, 0], SS[:, 0], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Subthreshold swing for sweep of channel height', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Channel height (nm)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Subthreshold swing (V/decade)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/' + 'Fig1_SS.png')
    plt.show()

    plt.figure(3, figsize = (10, 8))
    plt.plot (H[:, 0], J[:, 0], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('On-current density for sweep of channel height', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Channel height (nm)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('On-current density (A/cm^2)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/' + 'Fig1_J.png')
    plt.show()

    plt.figure(4, figsize = (10, 8))
    plt.plot (H[:, 0], u_FE[:, 0], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Field effect mobility for sweep of channel height', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Channel height (nm)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Field effect mobility (cm^2/V-s)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/' + 'Fig1_uFE.png')
    plt.show()


def solve_3(root, files_Neg, files_Pos):
    # 12.5,25,37.5,50,62.5
    L = np.arange(5).reshape(5, 1)
    L.dtype = np.float
    L[0, 0] = 12.5e-6
    L[1, 0] = 25e-6
    L[2, 0] = 37.5e-6
    L[3, 0] = 50e-6
    L[4, 0] = 62.5e-6
    H = 200e-9
    t = 200e-9

    n = np.size(files_Neg)
    J = np.arange(n).reshape(n, 1)
    J.dtype = np.float
    u_FE = np.arange(n).reshape(n, 1)
    u_FE.dtype = np.float
    SS = np.arange(n).reshape(n, 1)
    SS.dtype = np.float

    plt.figure(1, figsize = (10, 8))
    for file_N in files_Neg:
        num = int(file_N[-5])
        df_N = pd.read_csv(root + '/' + file_N)
        tmp_N = np.array(df_N)
        tmp_N = np.flipud(tmp_N)
        s_Neg = int(np.size(tmp_N)/10) - 1
        for f_P in files_Pos:
            if int(f_P[-5]) == num:
                file_P = f_P
        df_P = pd.read_csv(root + '/' + file_P)
        tmp_P = np.array(df_P)
        s_Pos = int(np.size(tmp_P)/10) - 4
        s = s_Neg + s_Pos
        Vg = np.arange(s).reshape(s, 1)
        Vg.dtype = np.float
        Id = np.arange(s).reshape(s, 1)
        Id.dtype = np.float
        Id_log = np.arange(s).reshape(s, 1)
        Id_log.dtype = np.float
        Vg[0 : s_Neg, 0] = tmp_N[1 :, 0]
        Id[0 : s_Neg, 0] = tmp_N[1 :, 8]
        Vg[s_Neg :, 0] = tmp_P[0 : s_Pos, 0]
        Id[s_Neg :, 0] = tmp_P[0 : s_Pos, 8]
        i = 0
        while i < s:
            if Id[i, 0] < 0:
                Id[i, 0] = abs(Id[i, 0])
            i = i + 1
        # print(Id)
        #
        i = 0
        while i < s:
            Id_log[i, 0] = math.log10(Id[i, 0])
            i = i + 1

        lb = "L = " + str(L[num - 1, 0] * 1e6) + " um"
        plt.plot (Vg[:, 0], Id[:, 0], linewidth = 2, label = lb)

        SS[num - 1] = solve_SS(Id_log, Vg, s)
        (J[num -1], u_FE[num - 1]) = solve_param(Id, Vg, s, L[num - 1], H, t)

    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_yscale("log")
    plt.title('Id - Vg characteristics', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vg (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/Fig2_transfer.png')
    plt.show()

    print(SS)
    print(J)
    print(u_FE)

    L = L * 1000000

    plt.figure(2, figsize = (10, 8))
    plt.plot (L[:, 0], SS[:, 0], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Subthreshold swing for sweep of channel length', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Channel length (um)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Subthreshold swing (V/decade)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/' + 'Fig2_SS.png')
    plt.show()

    plt.figure(3, figsize = (10, 8))
    plt.plot (L[:, 0], J[:, 0], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('On-current density for sweep of channel length', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Channel length (um)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('On-current density (A/cm^2)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/' + 'Fig2_J.png')
    plt.show()

    plt.figure(4, figsize = (10, 8))
    plt.plot (L[:, 0], u_FE[:, 0], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Field effect mobility for sweep of channel length', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Channel length (um)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Field effect mobility (cm^2/V-s)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/' + 'Fig2_uFE.png')
    plt.show()


def solve_4(root, files_Neg, files_Pos):
    # 100,150,200,250,300
    L = 50e-6
    H = 200e-9
    t = np.arange(5).reshape(5, 1)
    t.dtype = np.float
    t[0, 0] = 100e-9
    t[1, 0] = 150e-9
    t[2, 0] = 200e-9
    t[3, 0] = 250e-9
    t[4, 0] = 300e-9

    n = np.size(files_Neg)
    J = np.arange(n).reshape(n, 1)
    J.dtype = np.float
    u_FE = np.arange(n).reshape(n, 1)
    u_FE.dtype = np.float
    SS = np.arange(n).reshape(n, 1)
    SS.dtype = np.float

    plt.figure(1, figsize = (10, 8))
    for file_N in files_Neg:
        num = int(file_N[-5])
        df_N = pd.read_csv(root + '/' + file_N)
        tmp_N = np.array(df_N)
        tmp_N = np.flipud(tmp_N)
        s_Neg = int(np.size(tmp_N)/10) - 1
        for f_P in files_Pos:
            if int(f_P[-5]) == num:
                file_P = f_P
        df_P = pd.read_csv(root + '/' + file_P)
        tmp_P = np.array(df_P)
        s_Pos = int(np.size(tmp_P)/10) - 4
        s = s_Neg + s_Pos
        Vg = np.arange(s).reshape(s, 1)
        Vg.dtype = np.float
        Id = np.arange(s).reshape(s, 1)
        Id.dtype = np.float
        Id_log = np.arange(s).reshape(s, 1)
        Id_log.dtype = np.float
        Vg[0 : s_Neg, 0] = tmp_N[1 :, 0]
        Id[0 : s_Neg, 0] = tmp_N[1 :, 8]
        i = 0
        Vg[s_Neg :, 0] = tmp_P[0 : s_Pos, 0]
        Id[s_Neg :, 0] = tmp_P[0 : s_Pos, 8]
        while i < s:
            if Id[i, 0] < 0:
                Id[i, 0] = (Id[i - 1, 0] + Id[i + 1, 0])/2
            i = i + 1
        # print(Id)

        i = 0
        while i < s:
            Id_log[i, 0] = math.log10(Id[i, 0])
            i = i + 1

        lb = "tdi = " + str(int(t[num - 1, 0] * 1e9)) + " nm"
        plt.plot (Vg[:, 0], Id[:, 0], linewidth = 2, label = lb)

        SS[num - 1] = solve_SS(Id_log, Vg, s)
        (J[num -1], u_FE[num - 1]) = solve_param(Id, Vg, s, L, H, t[num - 1])

    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_yscale("log")
    plt.title('Id - Vg characteristics', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vg (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.legend(loc = 2, prop={'family':'Times New Roman', 'size':12})
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/Fig3_transfer.png')
    plt.show()

    print(SS)
    print(J)
    print(u_FE)

    t = t * 1000000000

    plt.figure(2, figsize = (10, 8))
    plt.plot (t[:, 0], SS[:, 0], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Subthreshold swing for sweep of dielectric thickness', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Dielectric thickness (nm)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Subthreshold swing (V/decade)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/' + 'Fig3_SS.png')
    plt.show()

    plt.figure(3, figsize = (10, 8))
    plt.plot (t[:, 0], J[:, 0], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('On-current density for sweep of dielectric thickness', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Dielectric thickness (nm)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('On-current density (A/cm^2)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/' + 'Fig3_J.png')
    plt.show()

    plt.figure(4, figsize = (10, 8))
    plt.plot (t[:, 0], u_FE[:, 0], linewidth = 2)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Field effect mobility for sweep of dielectric thickness', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Dielectric thickness (nm)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Field effect mobility (cm^2/V-s)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/Plots/' + 'Fig3_uFE.png')
    plt.show()


def solve_param(Id, Vg, s, L, H, t):
    W = 180e-6 # m
    Vds = 10
    epilson = 3.9
    epilson0 = 8.85e-12 # F/m
    Cg = epilson * epilson0 / t
    J = Id[s - 51, 0]/(W * H * 10000)
    parameter_gm = np.polyfit(Vg[s - 26 : s - 24, 0], Id[s - 26 : s - 24, 0], 1)
    gm = parameter_gm[0]
    u_FE = (gm / ((W / L) * Cg * Vds)) * 10000
    return(J, u_FE)

def solve_SS(Id_log, Vg, s):
    i = 0
    SS_min = 10000
    SS = np.zeros((1, s - 1), dtype = float)
    while i < s - 1:
        parameter = np.polyfit(Vg[i: i + 2, 0], Id_log[i: i + 2, 0], 1)
        SS[0, i] = 1 / parameter[0]
        if SS_min > SS[0, i]:
            if SS[0, i] > 0:
                SS_min = SS[0, i]
        i = i + 1

    return(SS_min)


if __name__ == "__main__":
    main()
