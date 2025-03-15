# py_calculator
Pythonで作成した電卓です。
コマンドラインで式を入力すると計算結果を返します。

可能演算子：
+, 
-, 
*, 
/, 
**(累乗)

## 技術
言語: Python 3.8+
ライブラリ: ast, math


## セキュリティ対策
eval()を直接使わず、ast（抽象構文木）を解析して危険なコードの実行を防ぎます。

## 実行
clone
```bash
git clone https://github.com/yusa-bot/py_calculator.git
cd py_calculator
```

実行
```bash
python calculator.py
```

ex.)
```bash
計算式を入力 : 3*3+1
結果: 10
計算式を入力 : 10*2*3
結果: 60
計算式を入力 : 1234*123425*1234
結果: 187946159300
```

終了
```bash
計算式を入力 : exit
電卓を終了
```

## ファイル構成
```bash
calculator/
  │── calculator.py #実装ファイル
  └── memo.py #学習用メモ
```
