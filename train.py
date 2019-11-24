from random import randint
import os

def main():
    while True:
        nums = []
        for x in range(101):
            rn = randint(0, 99)
            nums.append(rn)
            print(rn, end=' ')
        input('ready... ')
        os.system('cls')
        print('numbers:')
        i = input('')
        given = i.split(' ')
        for x in range(len(given)):
            if int(given[x]) == nums[x]:
                print(f'CORRECT {given[x]}:{nums[x]}')
            else:
                print(f'WRONG {given[x]}:{nums[x]}')

if __name__ == "__main__":
    main()