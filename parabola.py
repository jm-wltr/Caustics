import numpy as np
import matplotlib.pyplot as plt

#Crear figura
fig = plt.figure(dpi = 250)
ax = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

ax.set_box_aspect(1)
ax2.set_box_aspect(1)
ax3.set_box_aspect(1)

ax.set_ylim([0,1])
ax2.set_ylim([0,1])
ax3.set_ylim([0,1])

ax.set_xlim([0,1])
ax2.set_xlim([0,1])
ax3.set_xlim([0,1])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(['0.0','0.5','1.0'])
ax2.set_xticks([0, 0.5, 1])
ax2.set_xticklabels(['0.0','0.5','1.0'])
ax3.set_xticks([0, 0.5, 1])
ax3.set_xticklabels(['0.0','0.5','1.0'])
ax.set_yticks([0, 0.5, 1])
ax.set_yticklabels(['0.0','0.5','1.0'])
ax2.set_yticks([0, 0.5, 1])
ax2.set_yticklabels(['0.0','0.5','1.0'])
ax3.set_yticks([0, 0.5, 1])
ax3.set_yticklabels(['0.0','0.5','1.0'])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax3.set_xlabel('x')
ax3.set_ylabel('y')

ax.set_title('(a)')
ax2.set_title('(b)')
ax3.set_title('(c)')

plt.tight_layout()

#plt.subplots_adjust(wspace = 0.5, hspace = 0.5)

#Establecer variables
k = 1.0
x = np.linspace(-0.5, k, 50)

#Graficar
for t in np.linspace(0, k, 5):
    y = (-k)*x/t-t+x+k
    ax.plot(x,y, 'dimgray', linewidth = 1)

for t in np.linspace(0, k, 10):
    y = (-k)*x/t-t+x+k
    ax2.plot(x,y, 'dimgray', linewidth = 1)
    
for t in np.linspace(0, k, 20):
    y = (-k)*x/t-t+x+k
    ax3.plot(x,y, 'dimgray', linewidth = 1)
    
plt.show()
