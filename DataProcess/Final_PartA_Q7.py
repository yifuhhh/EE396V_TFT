import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def main():
    root = "/Users/yifuhhh/TFT_Projects/FinalExam/PartA"
    file = "Take_Home_Exam_Part A_Q7_Id_Vg_data.csv"
    df = pd.read_csv(root + '/' + file)
    tmp = np.array(df)
    s = int(np.size(tmp)/2)
    Vg = np.arange(s).reshape(s, 1)
    Vg.dtype = np.float
    Id = np.arange(s).reshape(s, 1)
    Id.dtype = np.float
    Id_log = np.arange(s).reshape(s, 1)
    Id_log.dtype = np.float
    Vg[:, 0] = tmp[:, 0]
    Id[:, 0] = tmp[:, 1]
    i = 0
    while i < s:
        Id_log[i, 0] = math.log(Id[i, 0])
        i = i + 1

    parameter = np.polyfit(Vg[s - 5 : s, 0], Id[s - 5 : s, 0], 1)
    f = np.poly1d(parameter)
    Vth = -parameter[1]/parameter[0]
    print("Vth = " + str(Vth))

    plt.figure(1, figsize = (10, 8))
    plt.plot (Vg[:, 0], Id[:, 0], color = 'royalblue', linewidth = 2)
    plt.plot(Vg[45:, 0], f(Vg[45:, 0]), "r--", linewidth = 1.5)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    plt.title('Id - Vg characteristics', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    # plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/PartA/Fig7_1a.png')
    plt.show()

    parameter_Von = np.polyfit(Vg[10 : 12, 0], Id_log[10 : 12, 0], 1)
    f_Von = np.poly1d(parameter_Von)
    SS = 1/parameter_Von[0]
    print("SS = " + str(SS))

    parameter_Von = np.polyfit(Vg[10 : 12, 0], Id[10 : 12, 0], 1)
    f_Von = np.poly1d(parameter_Von)
    Von = -parameter_Von[1]/parameter_Von[0]
    print("Von = " + str(Von))

    plt.figure(2, figsize = (10, 8))
    plt.plot (Vg[:, 0], Id[:, 0], color = 'royalblue', linewidth = 2)
    # plt.plot(Vg[10 : 18, 0], f_Von(Vg[10 : 18, 0]), "r--", linewidth = 1.5)
    ax = plt.gca()
    ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
    ax.set_yscale("log")
    plt.title('Id - Vg characteristics', fontdict={'family':'Times New Roman', 'size':16})
    plt.xlabel('Vgs (V)', fontdict={'family':'Times New Roman', 'size':16})
    plt.ylabel('Id (A)', fontdict={'family':'Times New Roman', 'size': 16})
    plt.yticks(fontproperties = 'Times New Roman', size = 14)
    plt.xticks(fontproperties = 'Times New Roman', size = 14)
    # plt.savefig('/Users/yifuhhh/TFT_Projects/FinalExam/PartA/Fig7_1b_2.png')
    plt.show()

    W = 20e-4 # cm
    L = 1e-4 # cm
    Vgs = 10
    t = 90e-7 # cm
    epilson = 25
    epilson0 = 8.85e-14 # F/cm
    Cg = epilson * epilson0 / t
    k = 1.3806504e-23 # m^2 kg s^-2 K-1, J/K
    T = 300 # K
    q = 1.602176487e-19 # C
    u_on = (2 * Id[s - 1, 0] * L) / (W * Cg * (Vg[s - 1, 0] - Von) * (Vg[s - 1, 0] - Von))
    u_Vth = (2 * Id[s - 1, 0] * L) / (W * Cg * (Vg[s - 1, 0] - Vth) * (Vg[s - 1, 0] - Vth))
    N = (((SS * q)/(k * T * math.log(10)) - 1) * Cg * q) / (q * q)
    v = u_on * Vgs / L

    print("u_on = " + str(u_on))
    print("u_Vth = " + str(u_Vth))
    print("velocity = " + str(v))
    print("trap DOS = " + str(N))

if __name__ == "__main__":
    main()
