def lengthOfLastWord(s: str):
    return 0 if len(s) == 0 else len(s.strip().split(" ")[-1])
