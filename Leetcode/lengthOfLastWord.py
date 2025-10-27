def lengthOfLastWord(s: str) -> int:
    words = s.strip().split(' ')
    if not words:
        return 0
    return len(words[-1])

s = "Hello World"
print(lengthOfLastWord(s))