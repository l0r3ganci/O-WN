#build a sofwaere abstraction of a PCM system
#one of the paramaters that characterize the adc converter is sampling time Ts
#it is the period of time that intercur by two measure of the input signal
#another important parameter is the range value of input signal= input range[Vmin,Vmax]
import math

import numpy as np
import matplotlib.pyplot as plt

#parte 1 defining the ADC and BSC parameter
nbit=np.array([2,3,4,6,8,10,12,14,16],dtype='int64')
Pe=np.linspace(1e-12,1,10000)
def snr(P,nbit):
    M2=2**(2*nbit)
    snrtot=np.empty([len(P),1],dtype='int64')
    for i in range(len(P)):
        snr1=M2/(1+4*(M2-1)*P[i])
        snrtot[i]=snr1
    return snrtot
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
col=['r','b','g','k','w','m','k','c','0.8']
#plot the SNR total with different value of nbit of adc
#parte2
#defining attribute for PMC classes
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

#PART 3
#we consider now a signal with bandwith of 22KHz
#SNR that we want to obtain is 80 dB with Pe=3.8e^-7
#nbit_ADC?

Bf=23
SNR_want=80
Pe1=3.8e-7
SNRb=math.log(1/4*Pe1)
SNRq=SNR_want-SNRb
nbit=int(SNRq/6)
print('Number of bits of ADC : ',nbit)
f_step=2.75625
f_shannon=int(2*Bf/f_step)
print(f_shannon)
f_adc=f_step*f_shannon
print('The f_sampling of adc( is a multiple of value f_step= 2.74625) is: ', f_adc)
Pe_crit=1/(4*(2**(2*nbit)-1))
print('Pe critical is : ', Pe_crit)
SNReffective=6*nbit
print(SNReffective,'dB')
result=snr1(Pe,16)
plt.figure()
plt.plot(Pe,result[0],label='Effective SNRtotal for ADC with nbit=16')
plt.grid()
plt.xscale('log')
plt.axvline(x=result[1])
plt.savefig('SNR_total_effective.jpg')
plt.show()