# 第1次作業-作業-HW1
>
>學號：1234567
><br />
>姓名：王小明
><br />
>作業撰寫時間：180 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2023/09/22
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容
- [x] 個人認為完成作業須具備觀念

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)

請在撰寫"說明程式與內容"該塊內容，請把原該塊內上述敘述刪除，該塊上述內容只是用來指引該怎麼撰寫內容。

1. 請解釋何謂git中下列指令代表什麼？並舉個例子，同時必須說明該例子的結果。其指令有add、commit、push、fetch、pull、branch、checkout與merge。

Ans:
1. git add
解釋：將變更的檔案加入暫存區，為下一次提交做好準備。
例子：
git add filename.txt
結果：filename.txt 會被加入到暫存區，但尚未提交到版本庫。這意味著對這個檔案的更改會在下次執行 git commit 時被記錄。

2. git commit
解釋：將暫存區的變更記錄到本地版本庫，並附上一個提交信息。
例子：
git commit -m "Add new feature"
結果：變更將被永久保存到本地版本庫中，並且你會看到提交信息 "Add new feature" 代表這次提交的目的。

3. git push
解釋：將本地版本庫的變更上傳到遠端版本庫。
例子：
git push origin main
結果：本地的 main 分支上的提交會被上傳到遠端的 main 分支，使得其他人也能看到這些變更。

4. git fetch
解釋：從遠端版本庫獲取最新的變更，但不會自動合併到當前分支。
例子：
git fetch origin
結果：遠端版本庫的變更會被下載到本地，但不會影響當前的工作分支。這使得你可以查看最新的變更後再決定是否合併。

5. git pull
解釋：從遠端版本庫獲取最新的變更並自動合併到當前分支。
例子：
git pull origin main
結果：當前分支會更新為遠端 main 分支的最新版本，可能會自動合併。如果有衝突，則需要手動解決。

6. git branch
解釋：列出、建立或刪除分支。
例子：
git branch new-feature
結果：在本地版本庫中創建一個名為 new-feature 的新分支，讓你可以在此分支上進行獨立的開發。

7. git checkout
解釋：切換到指定的分支或恢復檔案。
例子：
git checkout new-feature
結果：當前工作目錄會切換到 new-feature 分支，並顯示該分支的內容。

8. git merge
解釋：將兩個分支的變更合併到一起。
例子：
git merge new-feature
結果：當前分支會合併 new-feature 分支的變更。如果沒有衝突，這些變更會被整合到當前分支中；如果有衝突，則需要手動解決。



2. 於專案下的檔案—**hw1.py**，撰寫註解，以說明該程式每列中之背後意義。

    該hw1.py題目如下：

    ```
    統計字母數。假設今天輸入一句子，句子中有許多單字，單字皆為英文字母小寫，
    請統計句子中字母出現的字數，輸出實需要照字母排序輸出，且若該字母為0則不輸出

    如輸入
    this is an apple
    輸出
    a: 2
    e: 1
    h: 1
    i: 2
    l: 1
    n: 1
    p: 2
    s: 2
    t: 1
    ```

Ans:```from typing import List 

def countLetters(sentence: str) -> List[int]: 
    letterCount: List[int] = [0] * 26  

    for char in sentence: 
        if char.isalpha(): 
            index = ord(char) - ord('a')  
            letterCount[index] += 1    

    return letterCount  
pass

這段程式碼的目的是對輸入的字串中的每個字母進行計數，並返回一個列表，其中每個元素對應於字母表中一個字母的出現次數。這個過程忽略了非字母字符和大小寫的區別。若要使其完全支持大小寫，則在進行計算索引之前應先將字母轉為小寫

def printLetterCount(letterCount: List[int]) -> None: 

    for i in range(26):  
        if letterCount[i] > 0: 
            print(f"{chr(i + ord('a'))}: {letterCount[i]}") 
pass

這段程式碼的作用是遍歷字母計數的列表，找出所有出現過的字母，並將其與出現的次數一起打印出來。這使得最終的輸出顯示了哪些字母在輸入的句子中出現過以及每個字母的具體出現次數。

inputSentence: str = "this is an apple"  
letterCount: List[int] = countLetters(inputSentence)  
printLetterCount(letterCount) 
```

3. 請新增檔案**hw1_2.py，**輸入一個正整數(N)，其中$1\le N \le 100000$，請將該正整數輸出進行反轉

    ```
    如輸入
    1081

    輸出
    1801

    如輸入
    1000

    輸出
    1
    ```

Ans: N = input()   # 輸入一個正整數 N
     print(int(N[::-1])) # 反轉 N 並去掉前導零，然後輸出結果



4. **[課外題]**：請找尋資料，說明何謂**單元測試**，請新增檔案**hw1_3.py**，並利用溫度計攝氏轉華氏撰寫單元測試。

Ans:單元測試是指對程式中的最小單位——通常是函數或方法——進行測試，以確保它們按預期工作。
它是一種軟體測試技術，旨在檢查某個特定功能或程式邏輯在單一的測試環境中是否能正確運行，並產生預期的結果。



## 個人認為完成作業須具備觀念
###進行此項練習需理解 Git 的基本操作，包括版本控制的流程和指令的用途，這對於團隊協作和專案管理至關重要。此外，了解如何撰寫簡單的 Python 程式碼及其註解，並進行單元測試，確保程式邏輯的正確性，也是軟體開發中不可或缺的技能。這些知識將有助於提高程式碼的質量和維護性，並確保開發過程的順利進行。

開始寫說明，需要說明本次練習需學會那些觀念 (需寫成文章，需最少50字，並且文內不得有你、我、他三種文字)且必須提供完整與練習相關過程的notion筆記連結

