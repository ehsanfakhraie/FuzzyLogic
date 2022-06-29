import re

import fuzzification

RULE_NUMBER = 54


def inference(input_dict):
    chest_pain = fuzzification.chest_pain_fuzzification(int(input_dict['chest_pain']))

    cholesterol = fuzzification.cholesterol_fuzzification(int(input_dict['cholestrol']))

    blood_pressure = fuzzification.blood_pressure_fuzzification(int(input_dict['blood_pressure']))

    ecg = fuzzification.ecg_fuzzification(int(input_dict['ecg']))

    exercise = fuzzification.exercise_fuzzification(int(input_dict['exercise']))

    thallium = fuzzification.thallium_fuzzification(int(input_dict['thallium_scan']))

    age = fuzzification.age_fuzzification(int(input_dict['age']))

    blood_sugar = fuzzification.blood_sugar_fuzzification(int(input_dict['blood_sugar']))

    heart_rate = fuzzification.heart_rate_fuzzification(int(input_dict['heart_rate']))

    old_peak = fuzzification.old_peak_fuzzification(int(input_dict['old_peak']))

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
        'healthy': 0,
        'sick_1': 0,
        'sick_2': 0,
        'sick_3': 0,
        'sick_4': 0
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

        if len(phrases) == 1:
            # if there is only one phrase, it must be the result
            # get the result and the value of the phrase
            result = get_item(phrases[0][0], phrases[0][1])
            # add the result to the results dictionary
            results[result] += 1
        elif len(phrases) == 2:
            operator = re.findall(r'(AND|OR)', line)[0]
            # if there are two phrases, there must be an operator
            # get the result and the value of the phrase
            first = get_item(phrases[0][0], phrases[0][1])
            # get the value of the second phrase
            second = get_item(phrases[1][0], phrases[1][1])
            # if the operator is AND, the result must be the same as the value
            temp_result = ''
            if operator == 'AND':
                temp_result = min(first, second)
            # if the operator is OR, the result must be greater than the value
            elif operator == 'OR':
                temp_result = max(first, second)

            results[result] = max(results[result], temp_result)
    file.close()

    # for rule in file:
    #     rule = (rule.replace('(', '')).replace(')', '')
    #     start = rule.index('IF') + 3
    #     end = rule.index('THEN')
    #     if_clause = rule[start: end - 1].split(' ')
    #     start = end + 5
    #     end = rule.index(';')
    #     then_clause = rule[start: end].split(' ')
    #     result = 0
    #     if len(if_clause) == 3:
    #         # print('1', if_clause[0], if_clause[2])
    #         result = get_item(if_clause[0], if_clause[2])
    #     else:  # len = 7
    #         # print('2', if_clause[3])
    #         # print('3', if_clause[0], if_clause[2])
    #         # print('4', if_clause[4], if_clause[6])
    #         operator = if_clause[3]
    #         x = get_item(if_clause[0], if_clause[2])
    #         y = get_item(if_clause[4], if_clause[6])
    #         if operator == 'AND':
    #             result = min(x, y)
    #         else:  # operator = 'OR'
    #             result = max(x, y)
    #     # print(i, then_clause)
    #     results[then_clause[2]] = max(results[then_clause[2]], result)
    #     i += 1
    #     if i == RULE_NUMBER:
    #         break

    # print(results)
    return results
