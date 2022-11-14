s1='horrible'
s2='adorable'

def distance(s1,s2):
    l1,l2=len(s1),len(s2)
    dp=[[0 for i in range(l1+1)] for j in range(l2+1)]
    for i in range(l2+1):
        dp[i][0]=i
    for j in range(l1+1):
        dp[0][j]=j
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            d=1 if s1[j-1]!=s2[i-1] else 0
            dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+d)
    print('动态规划矩阵：')
    for line in dp:
        for s in line:
            print(s,'\t',end='')
        print('')
    return dp[-1][-1]

print('\nLevenshtein Distance:',distance(s1,s2))