List1 = [i for i in range(20,10,-1)]
List2 = [j**2 for j in range(10)]
List3 = [k for k in range(100) if k % 2 == 0]
List4 = [l.lower() for l in 'ABCDEFG']
List5 = ['_' for m in 'Hello World!']
List6 = [n for n in 'The Quick Brown Fox' if n.upper() == n and n != ' ']
List7 = [word[0] for word in 'my race should continue on to the island shore to help ease boring eye strain tonight'.split()]
List8 = [[row[i] for row in [[1,2,3],[4,5,6],[7,8,9]]]for i in range(3)]