class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        sMap, tMap = {}, {}
        need, have = 0, 0

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        need = len(tMap)

        l, r = 0, 0
        res = (float("inf"), -1, -1)

        while r < len(s):
            rc = s[r]

            sMap[rc] = sMap.get(rc, 0) + 1

            if rc in tMap and sMap[rc] == tMap[rc]:
                have += 1

            while l <= r and have == need:
                lc = s[l]

                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)

                sMap[lc] -= 1

                if lc in tMap and sMap[lc] < tMap[lc]:
                    have -= 1

                l += 1

            r += 1

        return s[res[1]:res[2] + 1] if res[0] < float("inf") else ""