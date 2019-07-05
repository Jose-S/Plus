# 15-112, Summer 2, TP
######################################
# Full name: Jose Saravia
# Section: A
# Andrew ID: jsaravia
######################################

from tkinter import *
from tkinter import ttk
import time

img ="""R0lGODlhfQB9APe5AD2F8j6F8j+G8kKI8kSJ8kWK8kaK8kmM8kmN8kyO80yP802P806Q80+Q81OS
81OT81eV81mX9FqX9FuY9FyY9F+a9GCb9GOd9GSd9GWe9Gae9Gaf9Wmg9Wqh9Wui9Wyj9XKm9XOn
9XSo9XWo9nap9niq9nmr9nqr9oCv9oOx94Wy94e094u294y295G6+JS7+JS7+ZO8+ZS8+Za9+Je+
+Jm/+JvA+J3C+J/C+aDD+anJ+bDO+rHO+rbR+rjS+73V+77W+8DX+8HX/MHY+8LZ+8PZ+8Pa+8TZ
+8Ta+8Xa+8Xb+8fc+8DY/MHY/MLY/MLZ/MPZ/MTa/MXa/MXb/Mba/Mbb/Mfb/Mjc/Mnc/Mjd/Mnd
/Mre/Mve/Mre/czf/M3f/M3f/czg+8zg/c3g/c7g/M/g/M7h/M/h/M7g/c/i/NDh/NDh/dHh/dHi
/NHi/dLj/NLi/dPj/dPk/dTk/NXk/NXl/NTk/dbk/dbl/dTk/tbl/tfm/tnn/Nnn/drn/djm/tnn
/trn/tro/dvp/dzp/d/r/dzo/tzp/t3p/t3q/t7q/t/q/t7r/t/r/uDq/uHs/eHt/eLt/ePu/ePt
/uPt/+Tv/eTu/uXu/uXv/uXv/+bv/ufv/+bw/ufw/ufw/+jw/ujx/unx/ujw/+nx/+ny/ury/+vy
/+zz/u70//D1/vD2/vL3//b5//X6//b6//f6//j7//n7//n8//r8//v9//z9//z+//3+//7/////
/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAALoALAAAAAB9AH0A
AAj+AHUJHEiwoMGDCBMeLBQkBwoPFyY8SEAgxiRGgOywAUMlSplHCkOKHEmypEmEj3agiACgpcuX
AGSYmkmzpqk4U65wOsmzp0+TKVE0gEn0JQybSGsGyrnzp9OnJmsNGSGgqFWXR5NqnSmqChlbUMOK
HdhpBoOraFtm3co2kBRQY+P2nGMiQNq7a9myHWWFj9y/IYlwuEsYQF69er+UAcxYoCweLAsTPoxY
rx4sshrHlQRCsmTKlfV2qaQZKq0cAzx/Ds165qQhtEr7bFNBtWfQrdnCISTbpK0bVW2vzt3ak5De
I0l1EK4aN3G2XVAhT1gEAfPmz4knkjO9YKwW123+O8++tVSU2N11rQgvnvxzKbemwxLBvr174lpg
9U6Fob79+7mtkUppmEDg338AtgaHKY3JosGBCCbI2hWZ/WVLCRBGKGFoVwCWQoYablgZFHLdAGKI
IiI2xFhKnIhiimyFYkZYoBzgInYw5oZIJ0/VcsGNOObYWhm1OOUCkEEKyVoRP7WI5G1KEpdGT6w4
8CSUUbYWyCw80XAlllmydsRJkaT2ZWHjhYnUJpGYFMKZw6kZ2hQlEQFnnHJWNuNIP945WZ6srTGS
nX7+CWhocYi0QaGGHooYFyGRwWijjupFh0IfTIpXpZVpkdAcmm7KKWK8HXRkqGilOaopTBxUiwL+
qKa6ql53HHRFrLLOytalBamA61WqrhpFQa8U8KtVwY46SSsEEXosUcmOuthApz4LU7ScMjmQBdZC
q6teagwUSrfeflveKgL1QO615rI1ra/rYtXuVk0IxG28as2rVbi6GIuvYfomNcktnPybb8BIdXKr
wdiOGocOBgOMsE1JsBBxw5xG8SbDE9ukRaYcd0wTF4uGLLIpaEhw8ckz5XGWySIfYua/GFfqSMQS
n5zJzPjW7GgmL9PMsimHqAxzx3ncKzTLaJS89MlVbPyvTCxHYfHREzcBMdYII7Hw0yKrUTDXAe9k
ANnzOmIv2u3yC2/PVafLtrliCNSJXXCfjO7+2nl3zK9A1a7rc57aCuSs4CdPK5ArZ8c7uJqWvNJr
3wgPW9DX5D4eJq8E1bKA4x0rglDg1moeZeEF9REv1QiDhBDI3Zou5BcKSZr5xJwj5PSzssNIhkiH
H9t7iomK1F/pAQs60hLdst5u8SNJ/evwEtJZ0iM8x0o9gJRIcpKXws8LBE9Vhm+uF1zy5CSuzs8a
xk+ka7o9eT44VUsGuM7/nBVFOtWJjajSX24MAReoGEF7ujrDWGyAqvY5igpy+ZD8VmUFC2FoUgKs
zA8Y4yAMcgoIFQKMKijAqBdUagiqKA1/CpXBrThhQLKZj59amJQg6Gc664ETDW3yhPQIpAbLcHKg
kjrkQ4FU50s7NMUkFFdEXSjnSjtkAymaWBBb4CA4N2phKa4AFioapA61uZEQJbSHQXgxIafJ3oH0
5wkroOeMCZGEB040vziQBo4j6YGBIGTCDR3CC3g8SREG45/e2QEOuAjkXE6At+uYDg2CUORTOkGD
oL0IMY3QwickKZZaEIEEWMRTaEoBhjd0kZNxIYVKhlKYMSbFEVvgwilQKZugROYqrpzJH7TABU3Q
sokMcQhEJEIRGVxiEX7AgxvGkAUrrAESuVBkQAAAOw=="""

img2 = """R0lGODlhyQEEAffXAD2F8kaL8keL8keM8kiL8kiM8kmM8lGR81KR81KS81OS81OT81ST81SU81yY
9FyZ9F2Z9F2a9F6a9F+a9F+b9GCb9Gef9Wif9Weg9Wig9Wmg9Wih9Wmh9Wqh9Wuh9Wui9Wyi9Wyj
9XOm9nKn9nOn9nSm9nSn9nWn9nWo9nao9nap9neq9n6t936u93+u93+v94Cu94Cv94Gv94Gw94Kw
94Kx94Ox94Sx94Sy94i0+Im0+Im1+Iq1+Iq2+Iu2+Iy3+I23+I64+I+4+JC4+JC5+JS8+JW8+JW9
+JS8+Za9+Ja++Je++Ji/+Jm/+JrA+JvB+JvA+ZzA+ZzB+Z3B+Z/D+aDD+aHE+aLE+aLF+aPF+aTG
+aXG+abH+afI+ajI+ajJ+anJ+arJ+qzK+q3L+q7L+q7M+q/M+rDN+rHN+rHO+rLO+rLP+rPP+rTP
+rTQ+rXQ+rXR+rXQ+7bR+rbR+7nS+7nT+7nU+7rU+7vV+7zV+73W+77X+7/X+7/X/MDY+8HY+8HZ
+8LY+8LZ+8PZ+8TZ/MTa/MXa/Mba/Mbb/Mfb/Mfc/Mjc/Mjd/Mnd/Mrd/Mre/Mve/Mvf/Mre/czf
/M3f/M3g/M7g/M/h/NHj/dLj/dPj/dPk/dTk/dXk/dTl/dXl/dbl/dbm/dfm/dXl/tbl/tjm/djn
/dnn/dno/dro/d3r/t7r/t/r/t/s/uDr/+Ds/uHs/uDt/uHt/uLt/uPt/+Lu/uPu/uXv/ubw/unx
/+vy/+zy/+3y/+zz/+3z/+70/+/0/+/1//D1//H1//H2//L2//L3//P3//T4//X4//X5//b5//f6
//j6//j7//n7//r8//v8//v9//z9//3+//7+//7//////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAANgALAAAAADJAQQB
AAj+ALEJHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuX
MGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSJMqXcq0qdOnUKNKnUq1qtWrWLNq3cq1q9evYMOK
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
"""

img3 ="""R0lGODlhfQB9APe5AD2F8j6F8j+G8kKI8kSJ8kWK8kaK8kmM8kmN8kyO80yP802P806Q80+Q81OS
81OT81eV81mX9FqX9FuY9FyY9F+a9GCb9GOd9GSd9GWe9Gae9Gaf9Wmg9Wqh9Wui9Wyj9XKm9XOn
9XSo9XWo9nap9niq9nmr9nqr9oCv9oOx94Wy94e094u294y295G6+JS7+JS7+ZO8+ZS8+Za9+Je+
+Jm/+JvA+J3C+J/C+aDD+anJ+bDO+rHO+rbR+rjS+73V+77W+8DX+8HX/MHY+8LZ+8PZ+8Pa+8TZ
+8Ta+8Xa+8Xb+8fc+8DY/MHY/MLY/MLZ/MPZ/MTa/MXa/MXb/Mba/Mbb/Mfb/Mjc/Mnc/Mjd/Mnd
/Mre/Mve/Mre/czf/M3f/M3f/czg+8zg/c3g/c7g/M/g/M7h/M/h/M7g/c/i/NDh/NDh/dHh/dHi
/NHi/dLj/NLi/dPj/dPk/dTk/NXk/NXl/NTk/dbk/dbl/dTk/tbl/tfm/tnn/Nnn/drn/djm/tnn
/trn/tro/dvp/dzp/d/r/dzo/tzp/t3p/t3q/t7q/t/q/t7r/t/r/uDq/uHs/eHt/eLt/ePu/ePt
/uPt/+Tv/eTu/uXu/uXv/uXv/+bv/ufv/+bw/ufw/ufw/+jw/ujx/unx/ujw/+nx/+ny/ury/+vy
/+zz/u70//D1/vD2/vL3//b5//X6//b6//f6//j7//n7//n8//r8//v9//z9//z+//3+//7/////
/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAALoALAAAAAB9AH0A
AAj+AHUJHEiwoMGDCBMeLBQkBwoPFyY8SEAgxiRGgOywAUMlSplHCkOKHEmypEmEj3agiACgpcuX
AGSYmkmzpqk4U65wOsmzp0+TKVE0gEn0JQybSGsGyrnzp9OnJmsNGSGgqFWXR5NqnSmqChlbUMOK
HdhpBoOraFtm3co2kBRQY+P2nGMiQNq7a9myHWWFj9y/IYlwuEsYQF69er+UAcxYoCweLAsTPoxY
rx4sshrHlQRCsmTKlfV2qaQZKq0cAzx/Ds165qQhtEr7bFNBtWfQrdnCISTbpK0bVW2vzt3ak5De
I0l1EK4aN3G2XVAhT1gEAfPmz4knkjO9YKwW123+O8++tVSU2N11rQgvnvxzKbemwxLBvr174lpg
9U6Fob79+7mtkUppmEDg338AtgaHKY3JosGBCCbI2hWZ/WVLCRBGKGFoVwCWQoYablgZFHLdAGKI
IiI2xFhKnIhiimyFYkZYoBzgInYw5oZIJ0/VcsGNOObYWhm1OOUCkEEKyVoRP7WI5G1KEpdGT6w4
8CSUUbYWyCw80XAlllmydsRJkaT2ZWHjhYnUJpGYFMKZw6kZ2hQlEQFnnHJWNuNIP945WZ6srTGS
nX7+CWhocYi0QaGGHooYFyGRwWijjupFh0IfTIpXpZVpkdAcmm7KKWK8HXRkqGilOaopTBxUiwL+
qKa6ql53HHRFrLLOytalBamA61WqrhpFQa8U8KtVwY46SSsEEXosUcmOuthApz4LU7ScMjmQBdZC
q6teagwUSrfeflveKgL1QO615rI1ra/rYtXuVk0IxG28as2rVbi6GIuvYfomNcktnPybb8BIdXKr
wdiOGocOBgOMsE1JsBBxw5xG8SbDE9ukRaYcd0wTF4uGLLIpaEhw8ckz5XGWySIfYua/GFfqSMQS
n5zJzPjW7GgmL9PMsimHqAxzx3ncKzTLaJS89MlVbPyvTCxHYfHREzcBMdYII7Hw0yKrUTDXAe9k
ANnzOmIv2u3yC2/PVafLtrliCNSJXXCfjO7+2nl3zK9A1a7rc57aCuSs4CdPK5ArZ8c7uJqWvNJr
3wgPW9DX5D4eJq8E1bKA4x0rglDg1moeZeEF9REv1QiDhBDI3Zou5BcKSZr5xJwj5PSzssNIhkiH
H9t7iomK1F/pAQs60hLdst5u8SNJ/evwEtJZ0iM8x0o9gJRIcpKXws8LBE9Vhm+uF1zy5CSuzs8a
xk+ka7o9eT44VUsGuM7/nBVFOtWJjajSX24MAReoGEF7ujrDWGyAqvY5igpy+ZD8VmUFC2FoUgKs
zA8Y4yAMcgoIFQKMKijAqBdUagiqKA1/CpXBrThhQLKZj59amJQg6Gc664ETDW3yhPQIpAbLcHKg
kjrkQ4FU50s7NMUkFFdEXSjnSjtkAymaWBBb4CA4N2phKa4AFioapA61uZEQJbSHQXgxIafJ3oH0
5wkroOeMCZGEB040vziQBo4j6YGBIGTCDR3CC3g8SREG45/e2QEOuAjkXE6At+uYDg2CUORTOkGD
oL0IMY3QwickKZZaEIEEWMRTaEoBhjd0kZNxIYVKhlKYMSbFEVvgwilQKZugROYqrpzJH7TABU3Q
sokMcQhEJEIRGVxiEX7AgxvGkAUrrAESuVBkQAAAOw=="""

img4 = """R0lGODdhMgAyANUAAAAAAAB28A928QB68Qx68RR88R198SR+8Sp/8TN/8iWB8iyC8jOD8juE8kyE
8kKG8j2J80aK8l6M8kyN81WN802Q81eS81uV9GWa9Gud9HKf9W+i9HWi9X2n9X6p9YSr9oqu9o60
95S095i395e5+Jm595y9+L+//6TB+KrE+bDG+bPL+szM/7rO+rrQ+8TU+sbZ/Mrb/NHf/NXi/Nvm
/d7p/uXt/ujv/+Tx/+vy//H2//T7/////wAAAAAAAAAAACH5BAkKAD0ALAAAAAAyADIAAAb/wJ5w
SCwSc7uccqlMGp/Q6DB3y/GSzGyTR81Jv0blVUte8rheMLhZbi+x6qjYTTcr40Urtl7fcfFCVnyD
dniChIh/a2iIiWlyjI2OkJKVglBIlpJOYZF1OmQ6OzqkoqBkilOIoDU2WTY0sbE1NDOubap7bqAy
KRsoTDsxEhQXFBYUESE1ZXA9h3U0KRcHASHBLwIFCAfVHDNuPDeBnmUyHd0HC8BvLw0NEQ8MJbdt
iuVkMxkGDAwdLczaJWjwoIEBenV4CDnlpoaHAg0gpKgnkMGCBQ0WmOjzLAfDMikUMIiwwqOWHS8M
NEAhgsGBCDE+Zjmlq8wMauvaoEwAzIaH/wMGQPThk8JlBhoyl+iIUdLjiwgFLMTQxOTDAAUp6FC0
AYJATqo5amgIAOFF0jY6QgYQATZHjAsDLkwlpGMFgwAgKFZ6OwDD3EF17+YFSwPDgAkxau5SsWBt
WxsdBixocbYMDhEGBowYSsfEggMfbtl4QcPN25cu6CgmE2MCggYrQKGgMGO1khJAOQR002MUnRD8
MsBYscBBbS2gVkTo17SMqIV1YlQY8ODCBAK0a+qwkWJCgwKh6egQgk/LCwz9GiCg/dFGjJYNBmQA
R0fhs/JMbHwwECHC+hkM2UBCBAsgUIAG9IWTxg34KTHDBwy888B/p+hAgwUBvGRCaQmN032RbTnQ
4MFVFjFQwATHeURDBhSIEAMOfDjTURsxlGACCjiicONuObhnSyN5lCeaXsgRksoRILaVBSedKMnH
kUE6qeAX0EjJBJSYNEgVlpRYeQkgejjpxyNgVmkJGoCEkUklMqaZhxVaZnHGHW5iUsUY4nFRRZ1x
rHkSmXgEAQA7"""

img5 ="""R0lGODdhaAGAAtUAAAAAAD2F8lmW8lyW7WCX7JWYml2Z8mSa7ZmcnmSd9Gye65ueoW2g756hpGui
9HSj66Gkp3Kl9Xqm6qKmqnao9H+q7aaqrnyr9IOr54St66mtsoGu84mu54yw5oax862xto6z7K+z
uIq09JS05LG1upO27Y+49rS4vp654pS69Zq667a7wZq88qO85Ki+47m+xaK/7Z3A9rvAx6PC863C
473CyqHD+KzE6rPG5bfG38HGzqjH+Orx/v///wAAAAAAACH5BAkAAD4ALAAAAABoAYACAAb/QJ5w
SCwaj8ikcslsOp/QqHRKrVqv2Kx2y+16v+CweEwum8/otHrNbrvf8Lh8Tq/b7/i8fs/v+/+AgYKD
hIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmqq6ytrq+wsbKztLW2t7i5uru8
vb6/wMHCw8TFxsfIycrLugUFfho1zNNNzn0v1tTaSNlUNQUnXxbPQxMr2+hF3VPf4V7j6fFH61Lt
4uTy+Tzr0jwnH/2IhDg3REOBCf1qSHtBYkhAIQ+HrPigY0iDAgAhGtFBgkTFIv1efHhh5ERDfbK6
rShw0dnBITpckovpUoizBc402JxApIDO/yHjZPL4IHQfzyEIZCJQhyCps6VDiqJ8pdLZBx4yul30
d1XIOIQ2CyCQQXJnz588Jrzk8U3IxYxGoxY4SWKds6M4CZ4oQPLoVFdV/Rr8CKFARHthjay1ibbA
giPwoh4laoGIwa778H37uRLzX8D4Vp70x1cIzQZEEGdW7Hffz7pli0Q2ywOnYqj7HkuWiyDi51RV
CZKOzaPwXIjg5LI+K8Sgbx6z465Wh2+x9ObOIPxmVTX2XuI8aCJ3N70nbmwnsaE2En3tOOE8sPm1
bl1I0u2rug/5DpFgNtX0lKdWQOv81N5RMekmBE4EtrZYV9HhZ4p+QvDHQ1ITFKYdW8klVv9ECM5Y
kBRu8d2lwX3Q4XNdUBYYVEBlu8U4zgJBSQhcaKVVmCMPLfkFoIpD1JXdETiJBaGK1mHjEnj0+RWU
gjZGKeWUVFZp5ZVYZqnlllx26eWXYIYp5phklmnmmWimqeaabLbp5ptwxinnnHTWaeedeOap5558
9unnn4AGKuighBZq6KFTvfDcGUoiuslKUqnRqKOYBBXpFAE6MSmllWTljAzNXZFpE5tyOolTSZAA
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
vdqPJwgAADs="""

img6 = """R0lGODdhIwAmAJEAAAAAAP///wAAAAAAACH5BAkKAAIALAAAAAAjACYAAAJTjI8ny5wPY5ux1tms
Ttjt3y0fGI5bKJgaqlpsK5Uw9M6cbCN1buy8nwPahDMizNhCqpQm5shJ6vB0uCn0VP1lg9tht/g9
hpPjZbl5fqajmKkiXQAAOw==
"""

img7 = """R0lGODdhIgAmAJEAAAAAAP///wAAAAAAACH5BAkKAAIALAAAAAAiACYAAAJdjIWpy50GnZwIWoqV
3Rlv3knfFzbjWGonmq5r6bpdLHt0Ld5xru9Mf/sBg4+hrmJMKpdLJJNUfEYW0ilVylNSmjbjbAjr
pQTiMXFMxqHTrHUU5H4f4tc5vX435R0FADs="""

img8 = """R0lGODdhIwAmAJEAAAAAAP///wAAAAAAACH5BAkKAAIALAAAAAAjACYAAAJTjI8ny5wPY5ux1tms
Ttjt3y0fGI5bKJgaqlpsK5Uw9M6cbCN1buy8nwPahDMizNhCqpQm5shJ6vB0uCn0VP1lg9tht/g9
hpPjZbl5fqajmKkiXQAAOw==
"""

# ------ Code is still being tested ------
# Warning: code has not been cleaned

class UIData(object):

    buttonStyle = "plusButton.TButton"
    buttonStylePaused = "pause.plusButton.TButton"

    # Most used data
    obstacleRadius = 25
    colorA = "blue"
    colorB = "white"
    powerItemImages = []

    def __init__(self, screenWidth, screenHeight):

        # Color Data
        self.bgColor = UIData.rgbString(16, 35, 64)
        self.ballAColor = UIData.rgbString(61, 133, 242)
        self.ballBColor = UIData.rgbString(235, 242, 255)
        self.ballBgColor = UIData.rgbString(82, 98, 122)

        # TextColors

        self.darkPressedTextColor = UIData.rgbString(45, 98, 178)
        self.darkActiveTextColor = UIData.rgbString(31, 67, 122)
        self.ligthPressedTextColor = UIData.rgbString(148, 152, 161)
        self.ligthActiveTextColor = UIData.rgbString(176, 181, 191)

        # Dimensions Data
        self.playerAMaxRadius = 100
        self.playerBMaxRadius = 75
        self.playerBMinRadius = 15
        self.playerRadius = 25
        self.ballBgRadius = 60

        # Images
        self.multiBallImage = self.titleImage = None
        self.halfTitleImage = None
        self.reversePowerImage = self.helpImage = None

        UIData.obstacleRadius = self.playerRadius
        UIData.colorA = self.ballAColor
        UIData.colorB = self.ballBColor


    def initUiElements(self, frame, data):

        self.configUIElementStyles()
        self.createSplashButtons(frame, data)
        self.createPauseButtons(frame, data)
        self.createPauseButton(frame, data)
        self.createHelpButtons(frame, data)

        self.multiBallImage = PhotoImage(data=img)
        self.titleImage = PhotoImage(data=img2)
        self.halfTitleImage = self.titleImage.subsample(3,3)
        self.reversePowerImage = PhotoImage(data=img4)
        self.helpImage = PhotoImage(data=img5)

        print(self.reversePowerImage, "PRINT")
        UIData.powerItemImages.append(self.reversePowerImage)
        print(len(UIData.powerItemImages))


    def createSplashButtons(self, frame, data):

        # Create Frame To Hold
        buttonFrameSplash = Frame(frame)

        # High Scores
        # hsButton = ttk.Button(buttonFrameSplash,
        #                       text="High Scores",
        #                       command=lambda: self.onButton(data, 1),
        #                       style=UIData.buttonStyle)
        # hsButton.grid(row=0, column=0)

        # Help Button
        b2 = ttk.Button(buttonFrameSplash,
                        text="Need Help?",
                        command=lambda: self.onButton(data, 2),
                        style=UIData.buttonStyle)
        b2.grid(row=1, column=0)
        buttonFrameSplash.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.buttoSplashFrame = buttonFrameSplash
        # self.buttonHighScore = hsButton
        self.buttonHelp = b2

    def createPauseButton(self, frame, data):

        buttonImage = PhotoImage(data=img6)

        pauseButton = ttk.Button(frame,
                                 image = buttonImage,
                                 command=lambda: self.onButton(data, 5),
                                 style=UIData.buttonStyle)
        pauseButton.image = buttonImage

        pauseButton.place(relx=0.8, rely=0.05)

        self.buttonPause = pauseButton

    def createHelpButtons(self, frame, data):

            buttonFrameHelp = Frame(frame)

            backButton = ttk.Button(buttonFrameHelp,
                                 text="Go Back",
                                 command=lambda: self.onButton(data, 6),
                                 style=UIData.buttonStylePaused)
            backButton.grid(row=0, column=0)

            buttonFrameHelp.place(relx=0.5, rely=0.95, anchor=CENTER)

            self.buttoHelpFrame = buttonFrameHelp
            self.buttonBack = backButton


    def createPauseButtons(self, frame, data):

            buttonFramePause = Frame(frame)

            hButton = ttk.Button(buttonFramePause,
                                 text="Help",
                                 command=lambda: self.onButton(data, 3),
                                 style=UIData.buttonStylePaused)
            hButton.grid(row=0, column=0)

            qButton = ttk.Button(buttonFramePause,
                                 text="Quit",
                                 command=lambda: self.onButton(data, 4),
                                 style=UIData.buttonStylePaused)
            qButton.grid(row=1, column=0)

            buttonFramePause.place(relx=0.5, rely=0.5, anchor=CENTER)

            self.buttoPauseFrame = buttonFramePause
            self.buttonQuit = qButton
            self.buttonHelpPause = hButton

    def configUIElementStyles(self):

        ttk.Style().configure(UIData.buttonStyle, foreground='white',
                              font=("Futura", 24),
                              background=self.bgColor,
                              activebackground="black",
                              borderwidth=0,
                              relief=FLAT)

        ttk.Style().map(UIData.buttonStyle,
                        foreground=[('pressed', self.ligthPressedTextColor),
                                    ('active', self.ligthActiveTextColor)],
                        background=[('pressed', '!disabled', self.bgColor),
                                    ('active', self.bgColor)])

        ttk.Style().configure(UIData.buttonStylePaused,
                              background=self.ballBColor,
                              foreground=self.bgColor,
                              width=6)

        ttk.Style().map(UIData.buttonStylePaused,
                        foreground=[('pressed', self.darkPressedTextColor),
                                    ('active', self.darkActiveTextColor)],
                        background=[('pressed', self.ballBColor),
                                    ('active', self.ballBColor)])

    def removeSplashUi(self):

        self.buttoSplashFrame.place_forget()

    def showSplashUi(self):
        self.buttoSplashFrame.place(relx=0.5, rely=0.9, anchor=CENTER)

    def removePauseUi(self):
        self.buttoPauseFrame.place_forget()

    def showPauseUi(self):
        self.buttoPauseFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def removePauseButton(self):
        self.buttonPause.place_forget()

    def showPauseButton(self):
        self.buttonPause.place(relx=0.8, rely=0.05)

    def removeHelpButton(self):
        self.buttoHelpFrame.place_forget()

    def showHelpButton(self):
        self.buttoHelpFrame.place(relx=0.5, rely=0.95, anchor=CENTER)


    def onButton(self, data, buttonId):

        if (buttonId == 1):
            print("Button 1")
        elif (buttonId == 2):
            print("Button 2")
            data.isInHelpMenu = True
        elif (buttonId == 3):
            print("Button 3")
            data.isInHelpMenu = True
            data.isPaused = True
            self.removePauseButton()
            self.removePauseUi()
        elif (buttonId == 4):
            print("Button 4")
            self.button4(data)
        elif (buttonId == 5):
            print("Button 5")
            self.button5(data)
        elif(buttonId == 6):
            data.isInHelpMenu = False
            self.removeHelpButton()
            data.player2.minimizeAnimation(data.ui.playerBMaxRadius, .001)


    # Logic for quit button
    def button4(self, data):
        data.isPlaying = False
        data.isPaused = False
        data.oldScore = data.score
        data.score = 0
        data.level = 1

    # Logic for pause button
    def button5(self, data):

        data.isPaused = not data.isPaused
        if (data.isPaused):
            data.timeOnPause = time.time()
            img = PhotoImage(data=img7)
            self.buttonPause.configure(image=img)
            self.buttonPause.image = img
        else:
            img = PhotoImage(data=img8)
            self.buttonPause.configure(image=img)
            self.buttonPause.image = img
            data.hasExitedPause = True
            data.timeExit = time.time()

    @staticmethod
    def rgbString(red, green, blue):
        return "#%02x%02x%02x" % (red, green, blue)
