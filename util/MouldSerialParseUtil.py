def parse(mould_serial):
    import re
    # 使用正则表达式提取数字
    numbers = re.findall(r'\d+', mould_serial)
    if len(numbers) >= 2:
        print(numbers)
        return int(numbers[0]), int(numbers[1])
    else:
        print("解析失败")
        return None

def main():
    parse("WDF24-4187")

if __name__ == "__main__":
    main()