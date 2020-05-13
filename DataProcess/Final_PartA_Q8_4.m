clear all
Vov = 7
W_L = 10
u = 30 % cm2/V-s
Vd = 0 : 1 : 30

plot(T, Pmtr, '-r', 'LineWidth', 2)
xlabel('T [K]') 
ylabel('P_{mtr} = n_{band}/(n_{band} + n_{trap})')