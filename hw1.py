from typing import List # 從 typing 模組中導入 List，以便能夠使用類型提示

def countLetters(sentence: str) -> List[int]:
    letterCount: List[int] = [0] * 26

    for char in sentence:
        if char.isalpha():
            index = ord(char) - ord('a')
            letterCount[index] += 1

    return letterCount
pass

def printLetterCount(letterCount: List[int]) -> None:

    for i in range(26):
        if letterCount[i] > 0:
            print(f"{chr(i + ord('a'))}: {letterCount[i]}")
pass

inputSentence: str = "this is an apple"
letterCount: List[int] = countLetters(inputSentence)
printLetterCount(letterCount)