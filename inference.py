import re

import fuzzification

RULE_NUMBER = 54


def inference(input_dict):
    chest_pain = fuzzification.chest_pain_fuzzification(int(input_dict['chest_pain']))

    cholesterol = fuzzification.cholesterol_fuzzification(int(input_dict['cholestrol']))

    blood_pressure = fuzzification.blood_pressure_fuzzification(int(input_dict['blood_pressure']))

    ecg = fuzzification.ecg_fuzzification(float(input_dict['ecg']))

    exercise = fuzzification.exercise_fuzzification(int(input_dict['exercise']))

    thallium = fuzzification.thallium_fuzzification(int(input_dict['thallium_scan']))

    age = fuzzification.age_fuzzification(int(input_dict['age']))

    blood_sugar = fuzzification.blood_sugar_fuzzification(int(input_dict['blood_sugar']))

    heart_rate = fuzzification.heart_rate_fuzzification(int(input_dict['heart_rate']))

    old_peak = fuzzification.old_peak_fuzzification(float(input_dict['old_peak']))

    sex = fuzzification.sex_fuzzification(int(input_dict['sex']))

    def get_item(item, member):
        if item == 'chest_pain':
            return chest_pain[member]
        if item == 'cholesterol':
            return cholesterol[member]
        if item == 'ECG':
            return ecg[member]
        if item == 'exercise':
            return exercise[member]
        if item == 'thallium':
            return thallium[member]
        if item == 'age':
            return age[member]
        if item == 'blood_pressure':
            return blood_pressure[member]
        if item == 'blood_sugar':
            return blood_sugar[member]
        if item == 'maximum_heart_rate':
            return heart_rate[member]
        if item == 'old_peak':
            return old_peak[member]
        if item == 'sex':
            return sex[member]

    results = {
        'healthy': [],
        'sick_1': [],
        'sick_2': [],
        'sick_3': [],
        'sick_4': []
    }

    # read rules file and iterate through it
    # example of rule:
    # RULE 5: IF (chest_pain IS non_aginal_pain) AND (blood_pressure IS high) THEN health IS sick_3;
    file = open('rules.fcl', 'r')
    for line in file:
        # remove newline character
        line = line.rstrip()
        # get phrases inside brackets using regex
        phrases = re.findall(r'\((.*?)\)', line)

        # get result phrase after "THEN health IS " using regex
        result = re.findall(r'health IS (.*?);', line)[-1]

        # separate each phrase into its own list wit " IS " as separator
        phrases = [phrase.split(' IS ') for phrase in phrases]
        temp_result = ''
        if len(phrases) == 1:
            # if there is only one phrase, it must be the result
            # get the result and the value of the phrase
            temp_result = get_item(phrases[0][0], phrases[0][1])
        elif len(phrases) == 2:
            operator = re.findall(r'(AND|OR)', line)[0]
            # if there are two phrases, there must be an operator
            # get the result and the value of the phrase
            first = get_item(phrases[0][0], phrases[0][1])
            print(phrases[0][0], phrases[0][1], first)
            # get the value of the second phrase
            second = get_item(phrases[1][0], phrases[1][1])
            print(phrases[1][0], phrases[1][1], second)
            # if the operator is AND, the result must be the same as the value
            if operator == 'AND':
                temp_result = min(first, second)
            # if the operator is OR, the result must be greater than the value
            elif operator == 'OR':
                temp_result = max(first, second)

        print(line, result, temp_result)
        results[result].append(temp_result)
    file.close()

    final_r = {
        'healthy': max(results['healthy']),
        'sick_1': max(results['sick_1']),
        'sick_2': max(results['sick_2']),
        'sick_3': max(results['sick_3']),
        'sick_4': max(results['sick_4'])
    }
    print(final_r)
    return final_r
