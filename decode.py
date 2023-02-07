import map


def decode(inp: str):
    result = ""
    bits = []
    i = 0
    while i < len(inp):
        tmp = ""
        j = 0
        while i < len(inp):
            if j > 16:
                return "失败了"
            tmp += inp[i]
            i += 1
            j += 1
            ttt = tmp in map.terminologies
            if tmp in map.terminologies:
                bits.append(map.terminologies.index(tmp))
                break
    bytesGroup = []
    for i in range(0, len(bits), 3):
        bytesGroup.append(64*bits[i]+8*bits[i+1]+bits[i+2])
    result = str(bytes(bytesGroup), "utf-8")
    return result


if __name__ == "__main__":
    while True:
        inp = input("请输入鸡语：")
        print("原文：" + decode(inp))
        print()