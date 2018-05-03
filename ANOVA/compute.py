import numpy as np
import scipy.stats as stats

def main():
    with open('assets/generate_datetime_for_ttest.txt', 'r', encoding='utf8') as source:
        date_time = [float(content.strip()) for content in source.readlines()]
        date_time = np.array(date_time)

    with open('assets/generate_text_for_ttest.txt', 'r', encoding='utf8') as source:
        text = [float(content.strip()) for content in source.readlines()]
        text = np.array(text)

    with open('assets/generate_number_for_ttest.txt', 'r', encoding='utf8') as source:
        number = [float(content.strip()) for content in source.readlines()]
        number = np.array(number)

    total_date_time = sum(date_time)
    total_text = sum(text)
    total_number = sum(number)

    grand_total = total_date_time + total_text + total_number
    n = 30

    print('sum of date time :: ' + str(total_date_time))
    print('sum of text :: ' + str(total_text))
    print('sum of number :: ' + str(total_number))
    print('grand total :: ' + str(grand_total))

    power_two_date_time = [content**2 for content in date_time]
    power_two_text = [content**2 for content in text]
    power_two_number = [content**2 for content in number]

    sum_power_two_date_time = sum(power_two_date_time)
    sum_power_two_text = sum(power_two_text)
    sum_power_two_number = sum(power_two_number)
    grand_total_power_two = sum_power_two_date_time + sum_power_two_text + sum_power_two_number

    print('sum of date time squre :: ' + str(sum_power_two_date_time))
    print('sum of text squre :: ' + str(sum_power_two_text))
    print('sum of number squre :: ' + str(sum_power_two_number))
    print('grand total square :: ' + str(grand_total_power_two))

    SST = grand_total_power_two - ((grand_total**2)/n)
    SSB = (((total_date_time**2)/10) + ((total_text**2)/10) + ((total_number**2)/10)) - ((grand_total**2)/n)
    SSE = SST - SSB
    print("sum squre of total :: " + str(SST))
    print("sum squre of between :: " + str(SSB))
    print("sum squre of error :: " + str(SSE))

    MSB = SSB / (3 - 1)
    print("mean squre of between :: " + str(MSB))

    MSE = SSE / (n - 3)
    print("mean squre of error :: " + str(MSE))

    # F = 0.0106/0.0002
    F = MSB/MSE
    print("f-value :: " + str(F))
    print("DF1 :: " + str(3 - 1))
    print("DF2 :: " + str(n - 3))
    print("f-criticle :: " + str(3.35413083))

    # result = stats.f_oneway(date_time, text, number)
    # print(result)


if __name__ == '__main__':
    main()
