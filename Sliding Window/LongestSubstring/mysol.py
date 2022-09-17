
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_sub_len = 0
    word_builder = {}
    word_list = []
    for c in s:
        if c in word_builder:
            if len(word_list) > max_sub_len: max_sub_len = len(word_list)
            index = word_builder[c]+1
            for i in word_list[:index]: del word_builder[i]
            word_list = word_list[index:]
            word_builder = {k: v-index for k,v in word_builder.items()}
    
        word_builder[c] = len(word_list)
        word_list.append(c)
    
    if len(word_list) > max_sub_len: max_sub_len = len(word_list)
    return max_sub_len

lengthOfLongestSubstring("abcabcbb")