def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)
    
    l=len(ranked)
    j=0
    
    ans=[]
    for i in range(len(player)):
        while j<l and player[i]<ranked[j]:
            j+=1
        
        ans.append(j+1)
        
    return ans[::-1]