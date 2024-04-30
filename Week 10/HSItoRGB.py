import numpy as np

def HSItoRGB(H, S, IN):
    H = np.radians(H)

    C = (1 - abs(2 * IN - 1)) * S

    X = C * (1 - abs((H / np.pi) % 2 - 1))

    if 0 <= H < np.pi / 3:
        R1, G1, B1 = C, X, 0
    elif np.pi / 3 <= H < 2 * np.pi / 3:
        R1, G1, B1 = X, C, 0
    else:
        R1, G1, B1 = 0, X, C

    m = IN - (1 / 3) * (R1 + G1 + B1)

    R, G, B = R1 + m, G1 + m, B1 + m

    R, G, B = int(R * 255), int(G * 255), int(B * 255)

    return R, G, B


hsi_values = np.array([120.0, 0.5, 0.8])
rgb_values = HSItoRGB(*hsi_values)

print("HSI Values:", hsi_values)
print("RGB Values:", rgb_values)
