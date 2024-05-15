import re

in_data = '5 5 4 5 4 5 4 5 4'
#
join_data = re.sub(r' ', "", in_data)
bad_num = ['2','3']
count_max = -1


results = {}

for i in range(0, len(join_data)):
    tmp_index = 0
    tmp_index = i + 7
    tmp_string = join_data[i:i+7]
    if len(tmp_string) < 7:
        break
    tmp_sum = 0
    tmp_split = list(tmp_string)
    if "3" not in tmp_split:
        if "2" not in tmp_split:
            counter = tmp_string.count('5')
            results[i] = counter
            #print(tmp_string)

for m in results.values():
    if int(m) > count_max:
        count_max = m

print(count_max)