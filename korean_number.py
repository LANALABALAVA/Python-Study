def korean_number(x):
    dic = {1:'일', 2:'이', 3:'삼', 4:'사', 5:'오', 6:'육', 7:'칠', 8:'팔', 9:'구', 10:'십'}
    return dic[x]

print(korean_number(7))