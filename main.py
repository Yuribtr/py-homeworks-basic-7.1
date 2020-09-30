import glob

files_list = []
for file in glob.glob("*.txt"):
    # exclude our output to prevent recursive writing to this file
    if file != 'result.txt':
        files_list.append(file)

strings = []
for filename in files_list:
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
        count = len(lines)
        strings.append([filename, count, ''.join(lines)])
# sort all strings by lines count
strings.sort(key=lambda x: x[1])
with open('result.txt', 'w', encoding='utf-8') as file:
    for item in strings:
        file.write(item[0]+'\n')
        file.write(str(item[1])+'\n')
        file.write(item[2]+'\n')