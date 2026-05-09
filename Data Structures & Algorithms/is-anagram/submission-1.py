class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        sFreq = {}
        tFreq = {}

        for i in range(len(s)):
            if s[i] in sFreq:
                sFreq[s[i]] += 1
            else:
                sFreq[s[i]] = 1
            
            if t[i] in tFreq:
                tFreq[t[i]] += 1
            else:
                tFreq[t[i]] = 1
        
        for key, val in sFreq.items():
            if key not in tFreq or tFreq[key] != val:
                return False
        
        return True