score_table = {
    1:[0, 50, 10, 10],
    2:[51, 100, 5, 20],
    3:[101, 150, 2, 30],
    4:[151, 200, 1, 40],
    5:[201, 99999, 0, 50]
}

def update_scores(ws:int, ls:int) -> (int, int):
    diff=abs(ws-ls)
    key=0
    for item in score_table.items():
        k,v=item
        print(diff, k, v)
        if diff >= v[0] and diff <= v[1] :
            if ws < ls:
                ws+=v[3]
                ls-=v[3]
            else:
                ws+=v[2]
                ls-=v[2]
            return ws, ls

    return ws, ls

if __name__ == "__main__":
    print(score_table)
    ws, ls = input().split()
    ws=int(ws)
    ls=int(ls)

    a,b=update_scores(ws,ls)
    print(a,b)