import numpy as np
from scipy.sparse import csr_matrix as sparse_matrix  # 疎行列クラス

# 微分を表す行列を生成する関数
# input:
#   nx : 座標点の数
#   dx : 座標の間隔
# return:
#   D1, D2, D3 : 1階微分、2階微分、3階微分
def make_differential_ops(nx, dx):
    # 単位行列Iを右にn個シフトした行列（ベクトルfのi成分をf_{i+n}にする）
    f0 = np.identity(nx, dtype=int)  # f_{i}
    f1 = np.roll(f0, 1, axis=1)  # f_{i+1}  (*1)
    f2 = np.roll(f0, 2, axis=1)  # f_{i+2}
    f_1 = f1.transpose()  # f_{i-1}
    f_2 = f2.transpose()  # f_{i-2}

    # D1 : (f_{i+1} - f_{i-1}) / (2 dx)
    deriv1 = sparse_matrix(f1 - f_1) / (2*dx)

    # D2 : (f_{i+1} - 2f_{i} + f_{i-1}) / (dx^2)
    deriv2 = sparse_matrix(f1 - 2*f0 + f_1) / dx**2

    # D3 : (f_{i+2} - 2f_{i+1} + 2f_{i-1} - f_{i-2}) / (2 dx^3)
    deriv3 = sparse_matrix(f2 - 2*f1 + 2*f_1 - f_2) / (2*dx**3)

    return deriv1, deriv2, deriv3
