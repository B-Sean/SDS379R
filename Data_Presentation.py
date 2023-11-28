#After all the data has been exported and combined into one Excel, this code was written to display the outputted data for easy comparison.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from ResSimPostProc import SimOutput
from plotpxdiag import plot_pxdiag
from plotptdiag import plot_ptdiag
from postprocessor import *
from preprocessor import *
from scipy.optimize import minimize
import json5 as jsonr
from scipy.interpolate import UnivariateSpline
import os
import jpype
import asposecells
import xlsxwriter as xl

mpl.rcParams['axes.linewidth']  = 2.
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['axes.edgecolor']  = 'gray'
mpl.rcParams['font.size']       = 15
mpl.rcParams['font.family']     = 'sans'

Data = pd.read_excel('Result_collection.xlsx')
pw_22 = Data['Pw_22']
r_22 = Data['R_22']
mw3_22 = Data['Mw3_22']
nbbl_22 = Data['Nbbl_22']
n2ing_22 = Data['N2inG_22']
n2inw_22 = Data['N2inW_22']
xn2wnc_22 = Data['XN2wnc_22']
gw_22 = Data['G/W_22']
area_22 = Data['Area_22']
ift_22 = Data['IFT_22']
pcap_22 = Data['Pcap_22']
fb_22 = Data['Buoyancy_22']
purev_22 = Data['pure_velocity_22']
aqv_22 = Data['Aq_velocity_22']

pw_10 = Data['Pw_10']
r_10 = Data['R_10']
mw3_10 = Data['Mw3_10']
nbbl_10 = Data['Nbbl_10']
n2ing_10 = Data['N2inG_10']
n2inw_10 = Data['N2inW_10']
xn2wnc_10 = Data['XN2wnc_10']
gw_10 = Data['G/W_10']
area_10 = Data['Area_10']
ift_10 = Data['IFT_10']
pcap_10 = Data['Pcap_10']
fb_10 = Data['Buoyancy_10']
purev_10 = Data['pure_velocity_10']
aqv_10 = Data['Aq_velocity_10']

pw_50 = Data['Pw_50']
r_50 = Data['R_50']
mw3_50 = Data['Mw3_50']
nbbl_50 = Data['Nbbl_50']
n2ing_50 = Data['N2inG_50']
n2inw_50 = Data['N2inW_50']
xn2wnc_50 = Data['XN2wnc_50']
gw_50 = Data['G/W_50']
area_50 = Data['Area_50']
ift_50 = Data['IFT_50']
pcap_50 = Data['Pcap_50']
fb_50 = Data['Buoyancy_50']
purev_50 = Data['pure_velocity_50']
aqv_50 = Data['Aq_velocity_50']

pw_minus = Data['Pw_minus']
r_minus = Data['R_minus']
mw3_minus = Data['Mw3_minus']
nbbl_minus = Data['Nbbl_minus']
n2ing_minus = Data['N2inG_minus']
n2inw_minus = Data['N2inW_minus']
xn2wnc_minus = Data['XN2wnc_minus']
gw_minus = Data['G/W_minus']
area_minus = Data['Area_minus']
ift_minus = Data['IFT_minus']
pcap_minus = Data['Pcap_minus']
fb_minus = Data['Buoyancy_minus']
purev_minus = Data['pure_velocity_minus']
aqv_minus = Data['Aq_velocity_minus']

pw_plus = Data['Pw_plus']
r_plus = Data['R_plus']
mw3_plus = Data['Mw3_plus']
nbbl_plus = Data['Nbbl_plus']
n2ing_plus = Data['N2inG_plus']
n2inw_plus = Data['N2inW_plus']
xn2wnc_plus = Data['XN2wnc_plus']
gw_plus = Data['G/W_plus']
area_plus = Data['Area_plus']
ift_plus = Data['IFT_plus']
pcap_plus = Data['Pcap_plus']
fb_plus = Data['Buoyancy_plus']
purev_plus = Data['pure_velocity_plus']
aqv_plus = Data['Aq_velocity_plus']


figtxtx = [0.09, 0.57]*4
figtxty = [0.765]*4+[0.52]*4+[0.270]*4+[0.025]*4

plt.rcParams.update({'legend.fontsize': 'small'})
fig,((ax1,ax2),(ax3,ax4),(ax5,ax6), (ax7, ax8), (ax9, ax10))=plt.subplots(5,2,figsize=(10,20))
# fig,((ax1,ax2),(ax3,ax4),(ax5,ax6), (ax7, ax8), (ax9, ax10))=plt.subplots(5,2,figsize=(15,22))

ax1.plot(pw_10, mw3_10, 'k--', label = '10C')
ax1.plot(pw_22, mw3_22, 'k-', label = '22C')
ax1.plot(pw_50, mw3_50,'k:', label = '50C')
ax1.scatter(pw_10, mw3_10, marker='o', facecolor='None',edgecolor='k')
ax1.scatter(pw_22, mw3_22, marker='o', facecolor='None',edgecolor='k')
ax1.scatter(pw_50, mw3_50, marker='o', facecolor='None',edgecolor='k')
ax1.set_xlabel('$P_L$, bar')
ax1.set_ylabel('$m_{w3}$, g')
ax1.set_ylim((13.5, 13.75))
ax1.set_title('a)', loc = 'left', fontsize = 15)
#ax1.legend()

ax2.plot(pw_10, r_10, 'k--',label = '10C')
ax2.plot(pw_22, r_22, 'k-',label = '22C')
ax2.plot(pw_50, r_50, 'k:',label = '50C')
ax2.scatter(pw_10, r_10, marker='o', facecolor='None',edgecolor='k')
ax2.scatter(pw_22, r_22, marker='o',facecolor='None',edgecolor='k')
ax2.scatter(pw_50, r_50, marker='o',facecolor='None',edgecolor='k')
ax2.set_xlabel('$P_L$, bar')
ax2.set_ylabel('$r$, nm')
ax2.set_title('b)', loc = 'left', fontsize = 15)
ax2.set_ylim((0,100))

ax3.plot(pw_10, nbbl_10, 'k--',label = '10C')
ax3.plot(pw_22, nbbl_22, 'k-',label = '22C')
ax3.plot(pw_50, nbbl_50, 'k:',label = '50C')
ax3.scatter(pw_10, nbbl_10, marker='o', facecolor='None',edgecolor='k')
ax3.scatter(pw_22, nbbl_22, marker='o', facecolor='None',edgecolor='k')
ax3.scatter(pw_50, nbbl_50, marker='o', facecolor='None',edgecolor='k')
ax3.set_xlabel('$P_L$, bar')
ax3.set_ylabel('Number density, 1/mL')
ax3.set_yscale('log')
ax3.set_title('c)', loc = 'left', fontsize = 15)
ax3.set_ylim((10**10, 10**16))



ax4.plot(pw_10, 100*n2ing_10, 'k--',label = '10C')
ax4.plot(pw_22, 100*n2ing_22, 'k-',label = '22C')
ax4.plot(pw_50, 100*n2ing_50, 'k:',label = '50C')
ax4.scatter(pw_10, 100*n2ing_10, marker='o', facecolor='None',edgecolor='k')
ax4.scatter(pw_22, 100*n2ing_22, marker='o', facecolor='None',edgecolor='k')
ax4.scatter(pw_50, 100*n2ing_50, marker='o', facecolor='None',edgecolor='k')
ax4.set_xlabel('$P_L$, bar')
ax4.set_ylabel('N$_2$ content in gas, mol%')
ax4.set_title('d)', loc = 'left', fontsize = 15)
ax4.set_ylim((0, 0.2))

ax5.plot(pw_10, 100*n2inw_10, 'k--',label = '10C')
ax5.plot(pw_22, 100*n2inw_22, 'k-',label = '22C')
ax5.plot(pw_50, 100*n2inw_50, 'k:',label = '50C')
ax5.scatter(pw_10, 100*n2inw_10, marker='o', facecolor='None',edgecolor='k')
ax5.scatter(pw_22, 100*n2inw_22, marker='o', facecolor='None',edgecolor='k')
ax5.scatter(pw_50, 100*n2inw_50, marker='o', facecolor='None',edgecolor='k')
ax5.set_xlabel('$P_L$, bar')
ax5.set_ylabel('N$_2$ content in aqueous, mol%')
ax5.set_title('e)', loc = 'left', fontsize = 15)
ax5.set_ylim((0, 0.5))

ax6.plot(pw_10, 100*xn2wnc_10, 'k--',label = '10C')
ax6.plot(pw_22, 100*xn2wnc_22, 'k-',label = '22C')
ax6.plot(pw_50, 100*xn2wnc_50, 'k:',label = '50C')
ax6.scatter(pw_10, 100*xn2wnc_10, marker='o', facecolor='None',edgecolor='k')
ax6.scatter(pw_22, 100*xn2wnc_22, marker='o', facecolor='None',edgecolor='k')
ax6.scatter(pw_50, 100*xn2wnc_50, marker='o', facecolor='None',edgecolor='k')
ax6.set_xlabel('$P_L$, bar')
ax6.set_ylabel('N$_2$ content in saturation, mol%')
ax6.set_title('f)', loc = 'left', fontsize = 15)
ax6.set_ylim((0, 0.5))

ax7.plot(pw_10, gw_10, 'k--',label = '10C')
ax7.plot(pw_22, gw_22, 'k-',label = '22C')
ax7.plot(pw_50, gw_50, 'k:',label = '50C')
ax7.scatter(pw_10, gw_10, marker='o', facecolor='None',edgecolor='k')
ax7.scatter(pw_22, gw_22, marker='o', facecolor='None',edgecolor='k')
ax7.scatter(pw_50, gw_50, marker='o', facecolor='None',edgecolor='k')
ax7.set_xlabel('$P_L$, bar')
ax7.set_ylabel('Fraction of N$_2$ in bubbles')
ax7.set_title('g)', loc = 'left', fontsize = 15)
ax7.set_ylim((0.05, 0.3))


ax8.plot(pw_10, area_10, 'k--',label = '10C')
ax8.plot(pw_22, area_22, 'k-',label = '22C')
ax8.plot(pw_50, area_50, 'k:',label = '50C')
ax8.scatter(pw_10, area_10, marker='o', facecolor='None',edgecolor='k')
ax8.scatter(pw_22, area_22, marker='o', facecolor='None',edgecolor='k')
ax8.scatter(pw_50, area_50, marker='o', facecolor='None',edgecolor='k')
ax8.set_xlabel('$P_L$, bar')
ax8.set_ylabel('$a$, m$^2$/mL')
ax8.set_yscale('log')
ax8.set_title('h)', loc = 'left', fontsize = 15)
ax8.set_ylim((10**-2, 4))

ax9.plot(pw_10, ift_10, 'k--',label = '10C')
ax9.plot(pw_22, ift_22, 'k-',label = '22C')
ax9.plot(pw_50, ift_50, 'k:',label = '50C')
ax9.scatter(pw_10, ift_10, marker='o', facecolor='None',edgecolor='k')
ax9.scatter(pw_22, ift_22, marker='o', facecolor='None',edgecolor='k')
ax9.scatter(pw_50, ift_50, marker='o', facecolor='None',edgecolor='k')
ax9.set_xlabel('$P_L$, bar')
ax9.set_ylabel('IFT, mN/m')
ax9.set_title('i)', loc = 'left', fontsize = 15)
ax9.set_ylim((50, 75))

ax10.plot(pw_10, pcap_10, 'k--',label = '10C')
ax10.plot(pw_22, pcap_22, 'k-',label = '22C')
ax10.plot(pw_50, pcap_50, 'k:',label = '50C')
ax10.scatter(pw_10, pcap_10, marker='o', facecolor='None',edgecolor='k')
ax10.scatter(pw_22, pcap_22, marker='o', facecolor='None',edgecolor='k')
ax10.scatter(pw_50, pcap_50, marker='o', facecolor='None',edgecolor='k')
ax10.set_xlabel('$P_L$, bar')
ax10.set_ylabel('$P_{c}$, bar')
ax10.set_title('j)', loc = 'left', fontsize = 15)
ax10.set_ylim((0, 200))
'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for x, y, l in zip(figtxtx, figtxty, letters):
    fig.text(x, y, '('+l+')')
'''
ax1.tick_params(which='both', direction='in', axis='both')
ax2.tick_params(which='both', direction='in', axis='both')
ax3.tick_params(which='both', direction='in', axis='both')
ax4.tick_params(which='both', direction='in', axis='both')
ax5.tick_params(which='both', direction='in', axis='both')
ax6.tick_params(which='both', direction='in', axis='both')
ax7.tick_params(which='both', direction='in', axis='both')
ax8.tick_params(which='both', direction='in', axis='both')
ax9.tick_params(which='both', direction='in', axis='both')
ax10.tick_params(which='both', direction='in', axis='both')

fig.tight_layout(pad=1.0)
#bbox_to_anchor=(0.735,1.005)
fig.legend(('T=10C','T=22C', 'T=50C'),fancybox=True,framealpha = 0.0, bbox_to_anchor=(0.799,1.005), ncol=4,columnspacing=4, fontsize=15)

plt.savefig('SMB_results_temp.png',dpi=400)







fig,((ax1),(ax2), (ax3))=plt.subplots(1,3 ,figsize=(18,6))

ax1.plot(pw_10, fb_10, 'k--', label = '10C')
ax1.plot(pw_22, fb_22, 'k-', label = '22C')
ax1.plot(pw_50, fb_50,'k:', label = '50C')
ax1.scatter(pw_10, fb_10, marker='o', facecolor='None',edgecolor='k')
ax1.scatter(pw_22, fb_22, marker='o', facecolor='None',edgecolor='k')
ax1.scatter(pw_50, fb_50, marker='o', facecolor='None',edgecolor='k')
ax1.set_title('a)', loc = 'left')
ax1.set_xlabel('$P_L$, bar')
ax1.set_ylabel('Net Buoyancy Forces, N')
ax1.set_yscale("log")



ax2.plot(pw_10, purev_10, 'k--',label = '10C')
ax2.plot(pw_22, purev_22, 'k-',label = '22C')
ax2.plot(pw_50, purev_50, 'k:',label = '50C')
ax2.scatter(pw_10, purev_10, marker='o', facecolor='None',edgecolor='k')
ax2.scatter(pw_22, purev_22, marker='o',facecolor='None',edgecolor='k')
ax2.scatter(pw_50, purev_50, marker='o',facecolor='None',edgecolor='k')
ax2.set_xlabel('$P_L$, bar')
ax2.set_ylabel('Terminal velocity in pure water, nm/s')
ax2.set_title('b)', loc = 'left', fontsize=15)
ax2.set_yscale("log")



ax3.plot(pw_10, aqv_10, 'k--',label = '10C')
ax3.plot(pw_22, aqv_22, 'k-',label = '22C')
ax3.plot(pw_50, aqv_50, 'k:',label = '50C')
ax3.scatter(pw_10, aqv_10, marker='o', facecolor='None',edgecolor='k')
ax3.scatter(pw_22, aqv_22, marker='o', facecolor='None',edgecolor='k')
ax3.scatter(pw_50, aqv_50, marker='o', facecolor='None',edgecolor='k')
ax3.set_title('c)', loc = 'left', fontsize=15)
ax3.set_xlabel('$P_L$, bar')
ax3.set_ylabel('Terminal velocity in aqeuous fluid, nm/s')
ax3.set_yscale("log")
fig.legend(('T=10C','T=22C', 'T=50C'),fancybox=True, framealpha=0.0,bbox_to_anchor=(0.675,1.009), ncol=4,columnspacing=3, fontsize=15)
fig.tight_layout(pad=2.0)
plt.savefig('SMB_new_results_temp.png',dpi=400)


fig,((ax1,ax2),(ax3,ax4),(ax5,ax6), (ax7, ax8), (ax9, ax10))=plt.subplots(5,2,figsize=(10,20))

ax1.plot(pw_minus, mw3_minus, 'k--', label = '-10% mw2', )
ax1.plot(pw_22, mw3_22, 'k-', label = '22C')
ax1.plot(pw_plus, mw3_plus,'k:', label = '+10% mw2')
ax1.scatter(pw_minus, mw3_minus, marker='o', facecolor='None',edgecolor='k')
ax1.scatter(pw_22, mw3_22, marker='o', facecolor='None',edgecolor='k')
ax1.scatter(pw_plus, mw3_plus, marker='o', facecolor='None',edgecolor='k')
ax1.set_xlabel('$P_L$, bar')
ax1.set_ylabel('$m_{w3}$, g')
ax1.set_ylim((13.5, 13.75))
ax1.set_title('a)', loc = 'left', fontsize=15)
#ax1.legend()

ax2.plot(pw_minus, r_minus, 'k--',label = '-10% mw2')
ax2.plot(pw_22, r_22, 'k-',label = '22C')
ax2.plot(pw_plus, r_plus, 'k:',label = '+10% mw2')
ax2.scatter(pw_minus, r_minus, marker='o', facecolor='None',edgecolor='k')
ax2.scatter(pw_22, r_22, marker='o',facecolor='None',edgecolor='k')
ax2.scatter(pw_plus, r_plus, marker='o',facecolor='None',edgecolor='k')
ax2.set_xlabel('$P_L$, bar')
ax2.set_ylabel('$r$, nm')
ax2.set_title('b)', loc = 'left', fontsize=15)
ax2.set_ylim((0,100))

ax3.plot(pw_minus, nbbl_minus, 'k--',label = '-10% mw2')
ax3.plot(pw_22, nbbl_22, 'k-',label = '22C')
ax3.plot(pw_plus, nbbl_plus, 'k:',label = '+10% mw2')
ax3.scatter(pw_minus, nbbl_minus, marker='o', facecolor='None',edgecolor='k')
ax3.scatter(pw_22, nbbl_22, marker='o', facecolor='None',edgecolor='k')
ax3.scatter(pw_plus, nbbl_plus, marker='o', facecolor='None',edgecolor='k')
ax3.set_xlabel('$P_L$, bar')
ax3.set_ylabel('Number density, 1/mL')
ax3.set_yscale('log')
ax3.set_title('c)', loc = 'left', fontsize=15)
ax3.set_ylim((10**10, 10**16))



ax4.plot(pw_minus, 100*n2ing_minus, 'k--',label = '-10% mw2')
ax4.plot(pw_22, 100*n2ing_22, 'k-',label = '22C')
ax4.plot(pw_plus, 100*n2ing_plus, 'k:',label = '+10% mw2')
ax4.scatter(pw_minus, 100*n2ing_minus, marker='o', facecolor='None',edgecolor='k')
ax4.scatter(pw_22, 100*n2ing_22, marker='o', facecolor='None',edgecolor='k')
ax4.scatter(pw_plus, 100*n2ing_plus, marker='o', facecolor='None',edgecolor='k')
ax4.set_xlabel('$P_L$, bar')
ax4.set_ylabel('N$_2$ content in gas, mol%')
ax4.set_title('d)', loc = 'left', fontsize=15)
ax4.set_ylim((0, 0.2))

ax5.plot(pw_minus, 100*n2inw_minus, 'k--',label = '-10% mw2')
ax5.plot(pw_22, 100*n2inw_22, 'k-',label = '22C')
ax5.plot(pw_plus, 100*n2inw_plus, 'k:',label = '+10% mw2')
ax5.scatter(pw_minus, 100*n2inw_minus, marker='o', facecolor='None',edgecolor='k')
ax5.scatter(pw_22, 100*n2inw_22, marker='o', facecolor='None',edgecolor='k')
ax5.scatter(pw_plus, 100*n2inw_plus, marker='o', facecolor='None',edgecolor='k')
ax5.set_xlabel('$P_L$, bar')
ax5.set_ylabel('N$_2$ content in aqueous, mol%')
ax5.set_title('e)', loc = 'left', fontsize=15)
ax5.set_ylim((0, 0.5))

ax6.plot(pw_minus, 100*xn2wnc_minus, 'k--',label = '-10% mw2')
ax6.plot(pw_22, 100*xn2wnc_22, 'k-',label = '22C')
ax6.plot(pw_plus, 100*xn2wnc_plus, 'k:',label = '+10% mw2')
ax6.scatter(pw_minus, 100*xn2wnc_minus, marker='o', facecolor='None',edgecolor='k')
ax6.scatter(pw_22, 100*xn2wnc_22, marker='o', facecolor='None',edgecolor='k')
ax6.scatter(pw_plus, 100*xn2wnc_plus, marker='o', facecolor='None',edgecolor='k')
ax6.set_xlabel('$P_L$, bar')
ax6.set_ylabel('N$_2$ content in saturation, mol%')
ax6.set_title('f)', loc = 'left', fontsize=15)
ax6.set_ylim((0, 0.5))

ax7.plot(pw_minus, gw_minus, 'k--',label = '-10% mw2')
ax7.plot(pw_22, gw_22, 'k-',label = '22C')
ax7.plot(pw_plus, gw_plus, 'k:',label = '+10% mw2')
ax7.scatter(pw_minus, gw_minus, marker='o', facecolor='None',edgecolor='k')
ax7.scatter(pw_22, gw_22, marker='o', facecolor='None',edgecolor='k')
ax7.scatter(pw_plus, gw_plus, marker='o', facecolor='None',edgecolor='k')
ax7.set_xlabel('$P_L$, bar')
ax7.set_ylabel('Fraction of N$_2$ in bubbles')
ax7.set_title('g)', loc = 'left', fontsize=15)
ax7.set_ylim((0.05, 0.3))


ax8.plot(pw_minus, area_minus, 'k--',label = '-10% mw2')
ax8.plot(pw_22, area_22, 'k-',label = '22C')
ax8.plot(pw_plus, area_plus, 'k:',label = '+10% mw2')
ax8.scatter(pw_minus, area_minus, marker='o', facecolor='None',edgecolor='k')
ax8.scatter(pw_22, area_22, marker='o', facecolor='None',edgecolor='k')
ax8.scatter(pw_plus, area_plus, marker='o', facecolor='None',edgecolor='k')
ax8.set_xlabel('$P_L$, bar')
ax8.set_ylabel('$a$, m$^2$/mL')
ax8.set_yscale('log')
ax8.set_title('h)', loc = 'left', fontsize=15)
ax8.set_ylim((10**-2, 4))

ax9.plot(pw_minus, ift_minus, 'k--',label = '-10% mw2')
ax9.plot(pw_22, ift_22, 'k-',label = '22C')
ax9.plot(pw_plus, ift_plus, 'k:',label = '+10% mw2')
ax9.scatter(pw_minus, ift_minus, marker='o', facecolor='None',edgecolor='k')
ax9.scatter(pw_22, ift_22, marker='o', facecolor='None',edgecolor='k')
ax9.scatter(pw_plus, ift_plus, marker='o', facecolor='None',edgecolor='k')
ax9.set_xlabel('$P_L$, bar')
ax9.set_ylabel('IFT, mN/m')
ax9.set_title('i)', loc = 'left', fontsize=15)
ax9.set_ylim((50, 75))

ax10.plot(pw_minus, pcap_minus, 'k--',label = '-10% mw2')
ax10.plot(pw_22, pcap_22, 'k-',label = '22C')
ax10.plot(pw_plus, pcap_plus, 'k:',label = '+10% mw2')
ax10.scatter(pw_minus, pcap_minus, marker='o', facecolor='None',edgecolor='k')
ax10.scatter(pw_22, pcap_22, marker='o', facecolor='None',edgecolor='k')
ax10.scatter(pw_plus, pcap_plus, marker='o', facecolor='None',edgecolor='k')
ax10.set_xlabel('$P_L$, bar')
ax10.set_ylabel('$P_{c}$, bar')
ax10.set_title('j)', loc = 'left', fontsize=15)
ax10.set_ylim((0, 200))

ax1.tick_params(which='both', direction='in', axis='both')
ax2.tick_params(which='both', direction='in', axis='both')
ax3.tick_params(which='both', direction='in', axis='both')
ax4.tick_params(which='both', direction='in', axis='both')
ax5.tick_params(which='both', direction='in', axis='both')
ax6.tick_params(which='both', direction='in', axis='both')
ax7.tick_params(which='both', direction='in', axis='both')
ax8.tick_params(which='both', direction='in', axis='both')
ax9.tick_params(which='both', direction='in', axis='both')
ax10.tick_params(which='both', direction='in', axis='both')
fig.tight_layout(pad=1.0)
#bbox_to_anchor=(0.735,1.005)
fig.legend(('-10% mw2','Observed mw2', '+10% mw2'),fancybox=True, framealpha=0.0,bbox_to_anchor=(0.869,1.005), ncol=4,columnspacing=5)
plt.savefig('SMB_results_mw2.png',dpi=400)

fig,((ax1),(ax2), (ax3))=plt.subplots(1,3 ,figsize=(18,6))

ax1.plot(pw_minus, fb_minus, 'k--', label = '-10% mw2')
ax1.plot(pw_22, fb_22, 'k-', label = '22C')
ax1.plot(pw_plus, fb_plus,'k:', label = '+10% mw2')
ax1.scatter(pw_minus, fb_minus, marker='o', facecolor='None',edgecolor='k')
ax1.scatter(pw_22, fb_22, marker='o', facecolor='None',edgecolor='k')
ax1.scatter(pw_plus, fb_plus, marker='o', facecolor='None',edgecolor='k')
ax1.set_xlabel('$P_L$, bar')
ax1.set_ylabel('Net Buoyancy Forces, N')
ax1.set_title('a)', loc = 'left', fontsize=15)
ax1.set_yscale("log")



ax2.plot(pw_minus, purev_minus, 'k--',label = '-10% mw2')
ax2.plot(pw_22, purev_22, 'k-',label = '22C')
ax2.plot(pw_plus, purev_plus, 'k:',label = '+10% mw2')
ax2.scatter(pw_minus, purev_minus, marker='o', facecolor='None',edgecolor='k')
ax2.scatter(pw_22, purev_22, marker='o',facecolor='None',edgecolor='k')
ax2.scatter(pw_plus, purev_plus, marker='o',facecolor='None',edgecolor='k')
ax2.set_xlabel('$P_L$, bar')
ax2.set_ylabel('Terminal velocity in pure water, nm/s')
ax2.set_title('b)', loc = 'left', fontsize=15)
ax2.set_yscale("log")



ax3.plot(pw_minus, aqv_minus, 'k--',label = '-10% mw2')
ax3.plot(pw_22, aqv_22, 'k-',label = '22C')
ax3.plot(pw_plus, aqv_plus, 'k:',label = '+10% mw2')
ax3.scatter(pw_minus, aqv_minus, marker='o', facecolor='None',edgecolor='k')
ax3.scatter(pw_22, aqv_22, marker='o', facecolor='None',edgecolor='k')
ax3.scatter(pw_plus, aqv_plus, marker='o', facecolor='None',edgecolor='k')
ax3.set_xlabel('$P_L$, bar')
ax3.set_ylabel('Terminal velocity in aqeuous fluid, nm/s')
ax3.set_title('c)', loc = 'left', fontsize=15)
ax3.set_yscale("log")

fig.tight_layout(pad=2.0)
fig.legend(('-10% mw2','Original mw2', '+10% mw2'),fancybox=True, framealpha=0,bbox_to_anchor=(0.689,1.009), ncol=4,columnspacing=3)
plt.savefig('SMB_new_results_mw2.png',dpi=400)