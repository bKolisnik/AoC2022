import os


def crt(ops,important_cycles = set([20,60,100,140,180,220])):
    x = 1
    cycles = 0
    
    results = dict()

    for i in range(len(ops)):
        if ops[i][0] == 'noop':
            cycles+=1
            if cycles in important_cycles:
                results[cycles] = cycles * x
        else:
            for _ in range(2):
                cycles+=1
                if cycles in important_cycles:
                    results[cycles] = cycles * x

            x+=int(ops[i][1])

    cum_sum = 0
    for key in results:
        cum_sum+=results[key]
    return cum_sum

def print_display(display):
    for i in range(len(display)):
        for j in range(len(display[0])):
            print(display[i][j],end="")
            if j == len(display[0])-1:
                print("\n",end="")

def crt2(ops,width=40,height=6):
    #draws a single pixel during each cycle

    # lit: #, dark: .
    #function to map cycles to which row of crt.
    #1 - 40 -> 1
    #41 - 80 -> 2
    #81 - 120 -> 3

    display = [['.' for x in range(width)] for y in range(height)]

    x = 1
    cycles = 0

    for i in range(len(ops)):
        if ops[i][0] == 'noop':
            cycles+=1
            pixel = cycles -1
            row, pixel = divmod(pixel,40)
            if x-1 <= pixel and pixel <= x+1:
                display[row][pixel] = "#"

        else:
            for _ in range(2):
                cycles+=1
                pixel = cycles -1
                row, pixel = divmod(pixel,40)
                if x-1 <= pixel and pixel <= x+1:
                    display[row][pixel] = "#"
            x+=int(ops[i][1])

    print_display(display)

if __name__ == "__main__":
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(TESTDATA_FILENAME) as file:
        ops = [line.rstrip().split(' ',1) for line in file]
        print(crt(ops))
        print(crt2(ops))