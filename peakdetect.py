import pandas as pd
import peakutils
import matplotlib.pyplot as plt

############# Getting data from CSV file ####################
bayerdata = pd.read_csv('D:\\acads\\semester4\\thesis\\BAYER data\\T521-22-P.csv', sep = ' ', header = None)
time = bayerdata[0:15000][0]
lvp = bayerdata[0:15000][1]
bp = bayerdata[0:15000][2]
ecg = bayerdata[0:15000][3]
numbers = list(range(0,15000))

time = time.tolist()
lvp = lvp.tolist()
bp = bp.tolist()
ecg = ecg.tolist()

##################### Finding peaks and averaging close-lying peaks to pick single peak ##############
### LVP ###
in_lvp = peakutils.indexes(lvp, thres=0.5, min_dist=0.1)
in_lvp = in_lvp.tolist()
print(len(in_lvp))
#print(in_lvp)
inlvpcount = 0
inlvpsum = 0
in_lvp_fin = []
for i in range(len(in_lvp)-1):
    if in_lvp[i+1]- in_lvp[i] < 20:
        inlvpsum += in_lvp[i]
        inlvpcount += 1
    else:
        inlvpsum += in_lvp[i]
        inlvpcount+= 1
        in_lvp_fin.append(int(inlvpsum / inlvpcount))
        inlvpsum = 0
        inlvpcount = 0
inlvpsum += in_lvp[i+1]
inlvpcount += 1
in_lvp_fin.append(int(inlvpsum / inlvpcount))
print("final inlvp len = ", len(in_lvp_fin))

### BP ###

in_bp = peakutils.indexes(bp, thres=0.6, min_dist=0.1)
in_bp = in_bp.tolist()
print(len(in_bp))
inbpcount = 0
inbpsum = 0
in_bp_fin = []
for i in range(len(in_bp)-1):
    if in_bp[i+1]- in_bp[i] < 40:
        inbpsum += in_bp[i]
        inbpcount += 1
    else:
        inbpsum += in_bp[i]
        inbpcount+= 1
        in_bp_fin.append(int(inbpsum / inbpcount))
        inbpsum = 0
        inbpcount = 0
inbpsum += in_bp[i+1]
inbpcount += 1
in_bp_fin.append(int(inbpsum / inbpcount))
print("final inbp len = ", len(in_bp_fin))


### ECG ###
in_ecg = peakutils.indexes(ecg, thres=0.5, min_dist=0.1)
in_ecg = in_ecg.tolist()
print(len(in_ecg))
inecgcount = 0
inecgsum = 0
in_ecg_fin = []
for i in range(len(in_ecg)-1):
    if in_ecg[i+1]- in_ecg[i] < 20:
        inecgsum += in_ecg[i]
        inecgcount += 1
    else:
        inecgsum += in_ecg[i]
        inecgcount+= 1
        in_ecg_fin.append(int(inecgsum / inecgcount))
        inecgsum = 0
        inecgcount = 0
inecgsum += in_ecg[i+1]
inecgcount += 1
in_ecg_fin.append(int(inecgsum / inecgcount))
print("final inecg = ", len(in_ecg_fin))

plt.figure('Left Ventricular Pressure')
axes1 = plt.gca()
axes1.set_ylim([0,150])
marklvp = in_lvp_fin
plt.plot(numbers, lvp, '-gD', markevery=marklvp)
#plt.show()


plt.figure('Blood Pressure')
axes2 = plt.gca()
axes2.set_ylim([50,150])
markbp = in_bp_fin
plt.plot(numbers, bp, '-gD', markevery=markbp)
#plt.show()

plt.figure('ECG')
axes3 = plt.gca()
axes3.set_ylim([-4,9])
markecg = in_ecg_fin
plt.plot(numbers, ecg, '-gD', markevery=markecg)
plt.show()
