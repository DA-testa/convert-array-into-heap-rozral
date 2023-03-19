#221RDB405 Ralfs Rozenbergs
import math

def build_heap(data):
    data_len=len(data)
    swaps=[]
    for i in range(math.floor(data_len/2),-1,-1):
        while True:
            value = 2*i+1
            if value >= len(data) or data[i] < data[value]:
                break
            if value+1 < len(data) and data[value] > data[value+1]:
                value += 1
            swaps.append([i,value])
            data[value],data[i] = data[i],data[value]
            i = value
    return swaps


def main():
    input_type = input()
    if "F" in input_type:
        try:
            file_input = input()
            file = open("test/" + file_input,"r")
            lines = file.readlines()
            length = int(lines[0])
            data = list(map(int,lines[1].split(" ")))
            file.close()
        except Exception:
            print("File not found")
    elif "I" in input_type:
        length = int(input())
        data = list(map(int, input().split(" ")))
        assert len(data) == length
    else:
        print("Incorrect format - choose I or F")

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()