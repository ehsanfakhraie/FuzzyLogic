# a function to calculate x value in a line with two points
def point_value(x, point_1, point_2):
    return (point_2[0] - point_1[0]) * (x - point_1[1]) / (point_2[1] - point_1[1]) + point_1[0]


# Chest Pain
def chest_pain_fuzzification(x):
    return {
        'typical_anginal': 1 if x == 1 else 0,
        'atypical_anginal': 1 if x == 2 else 0,
        'non_aginal_pain': 1 if x == 3 else 0,
        'asymptomatic': 1 if x == 4 else 0
    }


# Blood Pressure
def blood_pressure_fuzzification(x):
    def blood_pressure_low(x):
        if x <= 111:
            return 1
        elif 111 < x < 134:
            return point_value(x, (111, 1), (134, 0))
        else:
            return 0

    def blood_pressure_medium(x):
        if x <= 127 or x >= 153:
            return 0
        elif 127 < x <= 139:
            return point_value(x, (127, 0), (139, 1))
        else:
            return point_value(x, (153, 0), (139, 1))

    def blood_pressure_high(x):
        if x <= 142 or x >= 172:
            return 0
        elif 142 < x <= 157:
            return point_value(x, (142, 0), (157, 1))
        else:
            return point_value(x, (172, 0), (157, 1))

    def blood_pressure_veryhigh(x):
        if x <= 154:
            return 0
        elif 154 < x <= 171:
            return point_value(x, (154, 0), (171, 1))
        else:
            return 1

    return {
        'low': blood_pressure_low(x),
        'medium': blood_pressure_medium(x),
        'high': blood_pressure_high(x),
        'very_high': blood_pressure_veryhigh(x)
    }


# Cholesterol


def cholesterol_fuzzification(x):
    def cholesterol_low(x):
        if x <= 151:
            return 1
        elif 151 < x < 197:
            return point_value(x, (151, 1), (197, 0))
        else:
            return 0

    def cholesterol_medium(x):
        if x <= 188 or x >= 250:
            return 0
        elif 188 < x <= 215:
            return point_value(x, (188, 0), (215, 1))
        else:
            return point_value(x, (250, 0), (215, 1))

    def cholesterol_high(x):
        if 217 >= x >= 307:
            return 0
        elif 217 < x <= 263:
            return point_value(x, (217, 0), (263, 1))
        else:
            return point_value(x, (307, 0), (263, 1))

    def cholesterol_very_high(x):
        if x <= 281:
            return 0
        elif 281 < x <= 347:
            return point_value(x, (281, 0), (347, 1))
        else:
            return 1

    return {
        'low': cholesterol_low(x),
        'medium': cholesterol_medium(x),
        'high': cholesterol_high(x),
        'very_high': cholesterol_very_high(x)
    }


# Blood Sugar
def blood_sugar_fuzzification(x):
    def blood_sugar_very_high(x):
        if x <= 105:
            return 0
        elif 105 < x <= 120:
            return point_value(x, (105, 0), (120, 1))
        else:
            return 1

    return {
        'very_high': blood_sugar_very_high(x)
    }


# ECG
def ecg_fuzzification(x):
    def ecg_normal(x):
        if x <= 0:
            return 1
        elif 0 < x < 0.4:
            return point_value(x, (0, 1), (0.4, 0))
        else:
            return 0

    def ecg_abnormal(x):
        if x <= 0.2 or x >= 1.8:
            return 0
        elif 0.2 < x <= 1:
            return point_value(x, (0.2, 0), (1, 1))
        else:
            return point_value(x, (1.8, 0), (1, 1))

    def ecg_hypertrophy(x):
        if x <= 1.4:
            return 0
        elif 1.4 < x <= 1.9:
            return point_value(x, (1.4, 0), (1.9, 1))
        else:
            return 1

    return {
        'normal': ecg_normal(x),
        'abnormal': ecg_abnormal(x),
        'hypertrophy': ecg_hypertrophy(x)
    }


# Maximum Heart Rate
def heart_rate_fuzzification(x):
    def heart_rate_low(x):
        if x <= 100:
            return 1
        elif 100 < x < 141:
            return point_value(x, (100, 1), (141, 0))
        else:
            return 0

    def heart_rate_medium(x):
        if x <= 111 or x >= 194:
            return 0
        elif 111 < x <= 152:
            return point_value(x, (111, 0), (152, 1))
        else:
            return point_value(x, (194, 0), (152, 1))

    def heart_rate_high(x):
        if x <= 152:
            return 0
        elif 152 < x <= 210:
            return point_value(x, (152, 0), (210, 1))
        else:
            return 1

    return {
        'low': heart_rate_low(x),
        'medium': heart_rate_medium(x),
        'high': heart_rate_high(x)
    }


# Exercise
def exercise_fuzzification(x):
    return {
        'false': 1 if x == 0 else 0,
        'true': 1 if x == 1 else 0
    }


# OLD PEAK
def old_peak_fuzzification(x):
    def old_peak_low(x):
        if x <= 1:
            return 1
        elif 1 < x < 2:
            return point_value(x, (1, 1), (2, 0))
        else:
            return 0

    def old_peak_risk(x):
        if x <= 1.5 or x >= 4.2:
            return 0
        elif 1.5 < x <= 2.8:
            return point_value(x, (1.5, 0), (2.8, 1))
        else:
            return point_value(x, (4.2, 0), (2.8, 1))

    def old_peak_terrible(x):
        if x <= 2.5:
            return 0
        elif 2.5 < x <= 4:
            return point_value(x, (2.5, 0), (4, 1))
        else:
            return 1

    return {
        'low': old_peak_low(x),
        'risk': old_peak_risk(x),
        'terrible': old_peak_terrible(x)
    }


# Thallium
def thallium_fuzzification(x):
    return {
        'normal': 1 if x == 3 else 0,
        'medium': 1 if x == 6 else 0,
        'high': 1 if x == 7 else 0
    }


# Sex
def sex_fuzzification(x):
    sex = {
        'male': 1 if x == 0 else 0,
        'female': 1 if x == 1 else 0
    }
    return sex


# AGE

def age_fuzzification(x):
    def age_young(x):
        if x <= 29:
            return 1
        elif 29 < x < 38:
            return point_value(x, (29, 1), (38, 0))
        else:
            return 0

    def age_mild(x):
        if x <= 33 or x >= 45:
            return 0
        elif 33 < x <= 38:
            return point_value(x, (33, 0), (38, 1))
        else:
            return point_value(x, (45, 0), (38, 1))

    def age_old(x):
        if x <= 40 or x >= 58:
            return 0
        elif 40 < x <= 48:
            return point_value(x, (40, 0), (48, 1))
        else:
            return point_value(x, (58, 0), (48, 1))

    def age_very_old(x):
        if x <= 52:
            return 0
        elif 40 < x <= 48:
            return point_value(x, (52, 0), (60, 1))
        else:
            return 1

    return {
        'young': age_young(x),
        'mild': age_mild(x),
        'old': age_old(x),
        'very_old': age_very_old(x)
    }


# output
def o_fuzzification(x):
    def o_healthy(x):
        if x <= 0.25:
            return 1
        elif 0.25 < x < 1:
            return point_value(x, (0.25, 1), (1, 0))
        else:
            return 0

    def o_sick1(x):
        if x <= 0 or x >= 2:
            return 0
        elif 0 < x <= 1:
            return point_value(x, (0, 0), (1, 1))
        else:
            return point_value(x, (2, 0), (1, 1))

    def o_sick2(x):
        if x <= 1 or x >= 3:
            return 0
        elif 1 < x <= 2:
            return point_value(x, (1, 0), (2, 1))
        else:
            return point_value(x, (3, 0), (2, 1))

    def o_sick3(x):
        if x <= 2 or x >= 4:
            return 0
        elif 2 < x <= 3:
            return point_value(x, (2, 0), (3, 1))
        else:
            return point_value(x, (4, 0), (3, 1))

    def o_sick4(x):
        if x <= 3:
            return 0
        elif 3 < x <= 3.75:
            return point_value(x, (3, 0), (3.75, 1))
        else:
            return 1

    output = {
        'healthy': o_healthy(x),
        'sick_1': o_sick1(x),
        'sick_2': o_sick2(x),
        'sick_3': o_sick3(x),
        'sick_4': o_sick4(x)
    }
    return output
