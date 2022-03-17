import numpy as np
from numpy import linalg as LA

l_hip_x = 123 # x座標を入力
l_hip_y = 273.001 # y座標を入力

l_knee_x = 134.778 # x座標を入力（軸芯）
l_knee_y = 337.153 # y座標を入力（軸芯）

l_ankle_x = 198.88 # x座標を入力
l_ankle_y = 387.174 # y座標を入力

u = np.array([l_hip_x - l_knee_x, l_hip_y - l_knee_y])
v = np.array([l_ankle_x - l_knee_x, l_ankle_y - l_knee_y])

i = np.inner(u, v)
n = LA.norm(u) * LA.norm(v)

c = i / n
a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

print(a)