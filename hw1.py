from typing import List # 從 typing 模組中導入 List，以便能夠使用類型提示

def countLetters(sentence: str) -> List[int]: # 定義一個函數 countLetters，接受一個字串參數並返回一個整數列表
    letterCount: List[int] = [0] * 26  # 初始化一個長度為 26 的列表，用於計數每個字母的出現次數，初始值為 0

    for char in sentence: # 遍歷輸入的字串中的每一個字符
        if char.isalpha(): # 檢查該字符是否為字母
            index = ord(char) - ord('a')  # 將字母轉為小寫，計算其在字母表中的索引 (0-25)
            letterCount[index] += 1    # 將對應索引的計數器加一

    return letterCount  # 返回字母計數的列表
pass

def printLetterCount(letterCount: List[int]) -> None: # 定義一個函數 printLetterCount，接受一個整數列表作為參數，無返回值

    for i in range(26):  # 循環遍歷從 0 到 25，代表字母 'a' 到 'z'
        if letterCount[i] > 0: # 檢查對應字母的計數是否大於 0
            print(f"{chr(i + ord('a'))}: {letterCount[i]}") # 打印字母及其計數，使用 chr() 將索引轉換為對應字母
pass

inputSentence: str = "this is an apple"  # 定義一個輸入句子
letterCount: List[int] = countLetters(inputSentence)  # 調用 countLetters 函數計算字母出現次數，並儲存結果
printLetterCount(letterCount) # 調用 printLetterCount 函數輸出字母計數