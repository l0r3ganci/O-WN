import math

import numpy as np
import matplotlib.pyplot as plt


def snr1(P,bit):
    SNRt=np.empty([len(P)],dtype='int64')
    SNRq=2**(2*bit)
    for j in range(len(P)):
            qc=(SNRq)/(1+4*(SNRq-1)*P[j])
            SNRt[j]=(10*math.log(qc))
    print('SNRtotal point',SNRt)
    print('\n')
    Pcrit=1/(4*(2**(2*bit)-1))
    return SNRt,Pcrit

#parte2
#defining attribute for PMC classes
col=['r','b','g','k','w','m','k','c','0.8']
Bin=44.5
nbit_adc=[2,4,8,16]
Pe_bsc=np.linspace(1e-12,1,1000)
SNRtotal=np.empty(len(Pe_bsc),dtype='int64')
#snr total for all case of nbit



print('\nGenerating figure plot of total SNR\n')
plt.figure('SNR total')
for i in range(len(nbit_adc)):
    result=snr1(Pe_bsc,nbit_adc[i])
    Pe_critical=result[1]
    print('Probability error critical value for nbit_acd(2,4,8,16) :\n')
    print(Pe_critical)
    SNRtotal=result[0]
    plt.plot(Pe_bsc,SNRtotal,label='SNRtotal for the CSN', color=col[i],linewidth=2)
    plt.axvline(x=Pe_critical, color=col[i])
plt.xlabel('Pe probability error')
plt.ylabel('SNR total [dB]')
plt.xscale('log')
plt.grid()

plt.title('SNR total for nbits cases')
plt.savefig('TOTAL_snr.jpg')
plt.show()