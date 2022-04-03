file_name = input("请输入文件名：")
add_lines = input("请输入文本：")
with open(file_name, "a+") as f:
    f.write(f"\n{add_lines}")
    f.seek(0)
    content = f.readlines()

while True:
    print(f"当前文件的行数：{len(content)}")
    line_num = int(input("请输入行号："))
    if line_num != 0:
        print(content[line_num-1])
    break