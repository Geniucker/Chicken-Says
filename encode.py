import map


def encode(inp: str):
    result = ""
    inp = inp.encode("utf-8")
    for i in inp:
        byte = i
        tmp = ""
        for j in range(2):
            tmp = map.terminologies[byte % 16] + tmp
            byte //= 16
        result += tmp
    return result


if __name__ == "__main__":
    while True:
        inp = input("请输入原文：")
        print("鸡语：" + encode(inp))
        print()