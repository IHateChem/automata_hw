import sys
input = sys.stdin.readline; N, alphabets = input().strip().split(); N = int(N); N_alpha = len(alphabets); TM = [[] for _ in range(N)]; answer = []
for i in range(N*N_alpha):
    next, c, direction = input().strip().split(); next = int(next)
    TM[i//N_alpha].append((next, c, direction))
M = int(input())
alphabetindex = {alphabets[i] : i for i in range(N_alpha)}; directionindex = {"R": 1, "L": -1, "S":0}
for _ in range(M): 
    s = input().strip()
    end = len(s)
    tape = ["#"]; tape.extend(s) #start tape with #
    tape.extend(["#" for _ in range(200000-len(s))]) #fill tape with #s
    q = 0 #current state
    pnt = 0 #head pointer
    while q < N:
        p = q
        s = tape[pnt]
        q, c, direction = TM[q][alphabetindex[s]]
        tape[pnt] = c
        pnt += directionindex[direction]
        if pnt > end:
            end = pnt
            if pnt >= len(tape):
                tape.extend(["#" for _ in range(200000)])
    for i in range(end, -1, -1):
        if tape[i] != "#":
            end = i+1; break
    for i in range(0, end):
        if tape[i] != "#":
            start = i; break
    answer.append( "".join(tape[start:end])+ " "+str(q))
print("\n".join(answer))