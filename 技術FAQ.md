
Q1. 我需要很會寫Python程式才能在AEDT上開發自動化程式嗎？

A1. 不需要，自動化程式不會用到複雜的語法，只要知道下面這些就夠了：
- 基本型別及運算: string, int, float, boolean
- 基本型別資料結構及運算： list, tuple, dictionary
- 控制：if, else
- 迴圈：for, continue, break
- 匯入：Import
- 檔案讀寫函數：Open(), Close()
- 函數定義 def foo():
- 類別定義 class foo():

---

Q2. 是不是學會Python就可以開發自動化程式了

A2. 並不是。除了基本語法之外，你還要熟悉以下這些函式庫，你才能透過Python控制函式庫來與AEDT互動
- 基本函式庫：math, os, sys,...
- 進階函式庫：re, tkinter, matplotlib,...
- AEDT函式庫：Project, Design, Edit, Module

熟悉的意思並不是要背下所有的函式以及參數，而是要知道函式庫提供了何種功能，可以解決何種問題。只要知道如何發問問題，便可以透過Google找到答案。

---
Q. AEDT使用的是Iron Python，這和一般的Python有何差別？

A. 一般的Python又稱為Cpython。兩者的語法是類似的，內建基本函式庫也相同。但是目前多數科學用函式庫如Matplotlib，Scipy及Numpy僅支援Cpython。Iron Python主要建構在微軟的.NET框架，好處是可以使用到WPF技術在AEDT當中建立使用者介面。兩者都可以讀寫EXCEL或PPT，但是各自使用不同的函式庫。此外，目前Cpython已來到3.8版，而Iron Python仍停留在2.7版。已經會CPython的很容易就可以習慣IronPython。

---
Q. 在AEDT執行自動化程式的方式有哪些？

A. 主要方法有下列幾種：
- 從Automation執行script
- 從Toolkit執行script
- 熱鍵執行script
- ACT啟動GUI以執行script
- UDO(User Defined Outout)，建立客製化方程式
- UDP(User Defined Primitive)，建立客製化3D模型
- 將資料輸出到外部用Cpython處理(Anaconda)
- 透過批次檔控制AEDT完成前處理及後處理

---

