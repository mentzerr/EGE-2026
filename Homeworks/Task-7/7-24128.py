for card in range(1, 100000):
    V_F = 3840 * 2160 * 24 / 2**13
    V_F_ZH = V_F - V_F * .35 + 120
    C_1 = floor(20 * 2**20 / V_F_ZH)
    if C_1 * card > 4320:
        print(card)
        break