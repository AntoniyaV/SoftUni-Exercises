n = int(input())
l = int(input())

for s1 in range(1, n + 1):
    for s2 in range(1, n + 1):
        for s3 in range(ord('a'), ord('a') + l):
            for s4 in range(ord('a'), ord('a') + l):
                for s5 in range(1, n + 1):
                    if s1 < s5 > s2:
                        print(f'{s1}{s2}{chr(s3)}{chr(s4)}{s5}', end=' ')