class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        chars_positions: Dict[str, List[Tuple[int, str]]] = defaultdict(list)
        for i, c in enumerate(s):
            chars_positions[c].append((i, c))
        
        # a = array of pairs of 
        print('chars_pos = ', chars_positions)
        
        
        
        for x, y in permutations(set(s), 2):
            print('x,y = ', str(x), ', ', str(y))
            tot, mid = 0, False
            for _, c in sorted(chars_positions[x] + chars_positions[y]):
                if c == x and (mid := tot > 0):
                    tot -= 1
                elif c == y:
                    res = max(res, tot + mid)
                    tot += 1
        return res