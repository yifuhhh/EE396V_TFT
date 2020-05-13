clear all

Nt = 2.87e12;
Tta = 400;
hbar = 1.054e-34;
m0 = 9.1e-31;
meff = 0.2*m0;
kb = 8.61e-5;
T = 300;
Ec = 0;
Ef = -0.05 : 0.001 : 0.05;
KT = kb * 300;
gband = meff/(3.14 * hbar * hbar) / 10000 * (1.6e-19);

for i = 1:1:101

ef=Ef(1,i);
Fermi_band = @(x) gband*(exp((x-ef)/KT)+1).^(-1);
Fermi_trap = @(x) Nt/(kb*Tta)*exp(-(Ec-x)/(kb*Tta)).*(exp((x-ef)/KT)+1).^(-1);

nband(1,i) = integral(Fermi_band,0,Inf);
ntrap(1,i) = integral(Fermi_trap,-Inf,0);
Vov(1,i) = ((nband(1,i)+ntrap(1,i))*1.6e-19)/4e-8-ef

end

V0 = Vov(1,51);
Vov = Vov - V0;

Pmtr=nband./(nband + ntrap);
plot(Ef, Pmtr, '-r', 'LineWidth', 2)
xlabel('E_f [eV]') 
ylabel('P_{mtr} = n_{band}/(n_{band} + n_{trap})')