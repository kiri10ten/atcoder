n, m = map(int, input().split())
s = []
tak_codes = []


for i in range(n):
    r_i = input().strip()
    s.append(list(r_i))


for i in range(n):
    for j in range(m):
        if i + 9 <= n and j + 9 <= m:
         
            tl_region = all(s[i + x][j + y] == '#' for x in range(3) for y in range(3))

            
            br_region = all(s[i + 6 + x][j + 6 + y] == '#' for x in range(3) for y in range(3))

            
            adjacent_cells = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            adj_white = all(s[i + 3 + x][j + 3 + y] != '#' for x, y in adjacent_cells) and s[i + 4][j + 4] == '.'

            if tl_region and br_region and adj_white:
                tak_codes.append((i + 1, j + 1)) 


if tak_codes:
    for r, c in tak_codes:
        print(f"({r} {c})")


