from numpy import array, dot, eye, exp, argmin, diag, trace, sqrt, e, log, linspace
from scipy.linalg import inv, sqrtm, eigh, expm, logm
from scipy.stats import norm
import matplotlib.pyplot as plt

sx = array([[0,1], [1,0]])
sz = array([[1,0], [0,-1]])
id = eye(2)

def Wp(D, Dp, eps):
    return (Dp - D)/2 + sqrt((Dp/(2*eps))**2 + (D/2)**2)

def Wm(D, Dp, eps):
    return (Dp - D)/2 - sqrt((Dp/(2*eps))**2 + (D/2)**2)

def Pp(D, Dp, eps):
    return id/2 + (0.5/sqrt((eps*D)**2 + Dp**2)) * (eps*D*sz - Dp*sx)

def Pm(D, Dp, eps):
    return id/2 - (0.5/sqrt((eps*D)**2 + Dp**2)) * (eps*D*sz - Dp*sx)

def qXi(D, Dp, eps, b):
    Z = 1 + exp(-b*D)
    Zp = 1 + exp(-b*Dp)
    taub = (1/Z)*array([[1,0], [0, exp(-b*D)]])
    J_TPM = Zp / Z

    pr_p = trace(dot(Pp(D, Dp, eps), taub))
    pr_m = trace(dot(Pm(D, Dp, eps), taub))
    J_x = pr_p*exp(-b*Wp(D, Dp, eps)) + pr_m*exp(-b*Wm(D, Dp, eps))

    Jarz = (1-eps)*J_TPM + eps*J_x

    return log(Jarz*Z/Zp)


#################
#################
### PLOTTING ####
#################
#################

bet = 0.2

[D_a, Dp_a] = [2, 3]
[D_b, Dp_b] = [6, 3]

ep_l = linspace(0.00043, 0.83, 10000, endpoint=True)
#
QX_a = []
WP_a = []
WM_a = []
for ep in ep_l:
    QX_a = QX_a + [qXi(D_a, Dp_a, ep, bet)]
    WP_a = WP_a + [Wp(D_a, Dp_a, ep)]
    WM_a = WM_a + [Wm(D_a, Dp_a, ep)]
###
QX_b = []
WP_b = []
WM_b = []
for ep in ep_l:
    QX_b = QX_b + [qXi(D_b, Dp_b, ep, bet)]
    WP_b = WP_b + [Wp(D_b, Dp_b, ep)]
    WM_b = WM_b + [Wm(D_b, Dp_b, ep)]

fig = plt.figure(figsize=(6,4), dpi=200)

lbs = 13
plt.tick_params(axis='x', labelsize = lbs, direction = 'in', bottom = True, top = False)
plt.tick_params(axis='y', labelsize = lbs, direction = 'in', right = True, left = True)
plt.tick_params(axis='x', labelsize = lbs, direction = 'in', bottom = True, top = False)
plt.tick_params(axis='y', labelsize = lbs, direction = 'in', right = True, left = True)
#
plt.xlim(-0.3, 8.3)
plt.xticks([0, 2, 4, 6, 8])
plt.ylim(-4.7, 8.7)
plt.yticks([-4, -2, 0, 2, 4, 6, 8])
#
fts_la = 14
plt.xlabel(r'$\ln(1/\epsilon)$', rotation = 'horizontal', fontsize = fts_la, labelpad = 10)
#
plt.plot(-log(ep_l), log(array(QX_a)), color="#8CB9BD", solid_capstyle='round',  linewidth=5, label = r'$\ln(\Xi)$')
plt.plot(-log(ep_l), log(array(WP_a)), color="#ECB159", solid_capstyle='round',  linewidth=5, label = r'$\ln(\lambda_+)$')
plt.plot(-log(ep_l), log(abs(array(WM_a))), color="#B67352", linestyle='dotted', solid_capstyle='round',  linewidth=5, label = r'$\ln(-\lambda_-)$')

fts_le = 13
lbp = 0.6
lls = 0.6
plt.legend(fontsize=fts_le, frameon=True, borderpad=lbp, labelspacing=lls)

flnm = 'FIG_Xi-Wpm' + '_D' + str(D_a) + '_Dp' + str(Dp_a) + '_beta' + str(bet) + '.pdf'
#plt.savefig(flnm, bbox_inches='tight')

plt.tight_layout()
plt.show()
fig.savefig("Xi_Wpm_D2_Dp3_beta02.pdf")