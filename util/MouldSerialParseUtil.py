def parse(mould_serial):
    import re
    # 使用正则表达式提取数字
    numbers = re.findall(r'\d+', mould_serial)
    if len(numbers) >= 2:
        print(numbers[0])
        print(numbers[1])
        return int(numbers[0]), int(numbers[1])
    else:
        print("解析失败")
        return None

def gen_mould_serial(year,id):
    return f"WDF{year}-{id}"

def parse_file_path(file_path):
    # 使用 split 方法将字符串按 '/' 分割
    parts = file_path.split('/')
    # 获取最后一个元素
    last_element = parts[-1]
    (year, id) = parse(last_element)
    return gen_mould_serial(year, id)

def main():
    parse_file_path("F:/外发文件记录/2024-11-28/WDF24-4184-11.28-型腔镶块.prt")


if __name__ == "__main__":
    main()
