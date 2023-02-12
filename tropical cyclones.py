import re


def common_tc_dates(cyclone_dates_1, cyclone_dates_2) -> dict:
    answer = {'any_year': 0,
              'both_years': 0,
              'only_one_year': 0,
              'only_first_year': 0,
              'only_second_year': 0,
              'none_of_years': 0,
              }
    first_years, second_years = set(), set()

    date_31 = [str(i) for i in range(1, 32)]
    date_31.extend(['01', '02', '03', '04', '05', '06', '07', '08', '09'])

    month_31 = ['1', '01', '3', '03', '5', '05', '7', '07', '8', '08', '10', '12']

    date_30 = [str(i) for i in range(1, 31)]
    date_30.extend(['01', '02', '03', '04', '05', '06', '07', '08', '09'])

    month_30 = ['4', '04', '6', '06', '9', '09', '11']

    date_feb = [str(i) for i in range(1, 29)]
    date_feb.extend(['01', '02', '03', '04', '05', '06', '07', '08', '09'])

    if isinstance(cyclone_dates_1, list) and isinstance(cyclone_dates_2, list):
        reg = r"\s*\d{1,2}\s*/\s*\d{1,2}\s*/\s*\d{4}\s*"
        for i in range(len(cyclone_dates_1)):
            if isinstance(cyclone_dates_1[i], str) and re.match(reg, cyclone_dates_1[i]):
                add = re.sub(" ", "", cyclone_dates_1[i])
                if 1982 <= int(add.split('/')[2]) <= 2022:
                    if (add.split('/')[1] in month_31 and add.split('/')[0] in date_31) or (
                            add.split('/')[1] in month_30 and add.split('/')[0] in date_30) or (
                            add.split('/')[1] in ('2', '02') and add.split('/')[0] in date_feb):
                        if len(add.split('/')[0]) == 1:
                            add = '0' + add
                        if len(add.split('/')[1]) == 1:
                            add = add[:3] + '0' +add[3:]
                        add = add[:5]
                        first_years.add(add)

        for i in range(len(cyclone_dates_2)):
            if isinstance(cyclone_dates_2[i], str) and re.match(reg, cyclone_dates_2[i]):
                add = re.sub(" ", "", cyclone_dates_2[i])
                if 1982 <= int(add.split('/')[2]) <= 2022:
                    if (add.split('/')[1] in month_31 and add.split('/')[0] in date_31) or (
                            add.split('/')[1] in month_30 and add.split('/')[0] in date_30) or (
                            add.split('/')[1] in ('2', '02') and add.split('/')[0] in date_feb):
                        if len(add.split('/')[0]) == 1:
                            add = '0' + add
                        if len(add.split('/')[1]) == 1:
                            add = add[:3] + '0' +add[3:]
                        add = add[:5]
                        second_years.add(add)

    answer['only_first_year'] = len(first_years - second_years)
    answer['only_second_year'] = len(second_years - first_years)
    answer['both_years'] = len(first_years & second_years)
    answer['only_one_year'] = answer['only_first_year'] + answer['only_second_year']
    answer['any_year'] = len(set(first_years | second_years))
    answer['none_of_years'] = 365 - answer['any_year']
    return answer
