class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_index = {s: i for i, s in enumerate(req_skills)}
        n = len(req_skills)
                
        dp = {0: []}
                        
        for i, person in enumerate(people):
            skill_mask = 0
            for skill in person:
                if skill in skill_index:
                    skill_mask |= (1 << skill_index[skill])
                                                                        
            for mask, team in list(dp.items()):
                new_mask = mask | skill_mask
                
                if new_mask == mask:
                    continue
                
                if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                    dp[new_mask] = team + [i]
        
        return dp[(1 << n) - 1]
