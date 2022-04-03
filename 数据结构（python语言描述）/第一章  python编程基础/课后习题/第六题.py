from prettytable import PrettyTable


filename = input("请输入文件名：")
with open(filename) as f:
    content = f.readlines()
    for i, line in enumerate(content):
        if i == 0:
            table = PrettyTable(line.split())
        else:
            table.add_row(line.split())
table.reversesort = False
print(table)
