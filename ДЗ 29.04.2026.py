strs = ["flower", "flow", "flight"]


def z_func(s, n):
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

lengths_list = []

for element in strs:
    lengths_list.append(len(element))


string = ""
for i in strs:
    string += i


n = len(string)
z_string = z_func(string, n)


min_value = 10000
current_index = 0
for element in lengths_list:
    if current_index == 0:
        current_index += element
        continue

    min_value = min(min_value, z_string[current_index])
    current_index += element

print(string[:min_value])