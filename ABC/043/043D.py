# テストケースの答えと一致しない回答なのでunittestなし
s = input()
length = len(s)

if length == 2:
    print('1 2') if s[0] == s[1] else print('-1 -1')
else:
    end = 0
    for i in range(length-2):
        if s[i] == s[i+1] :
            end = 1
            print(str(i + 1) + ' ' + str(i + 2))
            break

        if s[i] == s[i+2] :
            end = 1
            print(str(i + 1) + ' ' + str(i + 3))
            break


    if end == 0 :
        print('-1 -1')