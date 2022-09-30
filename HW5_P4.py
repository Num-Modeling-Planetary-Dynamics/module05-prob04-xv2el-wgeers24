import matplotlib.pyplot as plt
import numpy as np
import csv
with open('./id000002-XV.csv', 'r') as file:
    csvreader= csv.reader(file)
header=[]
header=next(csvreader)
writer.writerow(["t", "a", "e", "inclination", "lon_asc_node", "arg_peri", "true_anom"])

rows=[]
for row in csvreader:
    rows.append(row)
def xv2el(mu,x,v):

    rMag=np.linalg.norm(x)
    mu=-G(m1+m2)
    vMag=np.linalg.norm(v)
    h=np.cross(x,v)
    hMag=np.linalg.norm(h)

    a=((2/rMag)-(vMag**2)/mu)**-1

    e=np.sqrt(1-(hMag**2/(mu*a)))
    I=np.arccos(h[2]/hMag)
    omega=np.arcsin(h[0]/(hMag*np.sin(I)))

    peri=np.arcsin(x[2]/(x*np.sin(I)))-f
    f=np.arccos((1/e)*((a*(1-e**2))/rMag)-1)


with open("../data/id000002-EL.csv", 'w') as f:

    plt.plot(t,a)
    plt.xlabel('Time(Myr)')
    plt.ylabel('semi-major axis(a)')
    plt.savefig('../plots/module05-prob04-a_vs_t_02.png')

    plt.plot(t,I)
    plt.xlabel('Time(Myr)')
    plt.ylabel('Inclination')
    plt.savefig('../plots/module05-prob04-I_vs_t_02.png')

