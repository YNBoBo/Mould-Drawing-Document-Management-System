import datetime

def get_today():
    now = datetime.datetime.now()
    today = now.strftime("%Y.%m.%d")
    return today

def main():
    print(get_today())


if __name__ == "__main__":
    main()