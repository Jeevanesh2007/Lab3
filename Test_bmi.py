import Lab_2.bmi as bmi

def test_bmi_normal_weight():
    if bmi <= 25.0 and bmi >= 18.5:
        print("Normal weight")
        return 0


def test_bmi_over_weight():
    if bmi > 25.0:
        print("Over weight")
        return 1


def test_bmi_under_weight():
    if bmi < 18.5:
        print("Under weight")
        return -1
