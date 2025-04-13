import math 
import random

def print_state(sum1, sum2, arr):
    print(f'{arr} \n  AI:{sum1}    Player:{sum2}')

def main():
    arr = []    
    arr = [random.randint(1, 13) for i in range(14)]
    sum1, sum2 = 0,0
    while len(arr) >0:
        print_state(sum1, sum2, arr)
        best_score, move = minmax(arr, 0 , 0 , True)
        print(f'best diff between computer and human is: {best_score}, computer is using {move}')
        if move == arr[0]:
            arr= arr[1:]
        else:
            arr=arr[0:-1]
        sum1+=move
           
        print_state(sum1, sum2, arr)
        if len(arr) ==0:
            break
        print("")
        str = input("L or R: ")
        if str == "L":
            sum2+=arr[0]
            arr = arr[1:]
        else:
            sum2+=arr[-1]
            arr= arr[0:-1]

    print(f'Gmae over')
    print_state(sum1, sum2, arr)



def calc_score(sum1, sum2):
    if sum1 != sum2:
        return sum1-sum2
    else:
        return 0

def get_sub_arrays(subs_arr):
    return [(subs_arr[0],subs_arr[1:]), (subs_arr[-1], subs_arr[:-1])]

def get_hash(arr):
    return hash(tuple(arr))

def minmax(subs_arr, sum1, sum2, is_max):
    if len(subs_arr) ==0:
        calculated_score =  calc_score(sum1, sum2)
        return calculated_score, None

    score = 0
    lr_move = None
    moves = get_sub_arrays(subs_arr)
    if is_max:
        max_score = -math.inf 
        for move in moves:
                score, _ = minmax(move[1], sum1+move[0], sum2, not is_max)
                if max_score < score:
                    max_score = score
                    lr_move = move[0] 

        return max_score, lr_move
    else:
        min_score = math.inf
        for move in moves:
            score, _ = minmax(move[1], sum1, sum2+move[0], not is_max)
            if min_score > score:
                min_score = score
                lr_move = move[0]
        return min_score, lr_move


if __name__ == '__main__':
    main()