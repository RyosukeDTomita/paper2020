# paper2020
## プログラムの概要
>------------------------------------------------------------------------------------------------------------------------------
### 数値モデル関連

1. __init.py__
1. auto.bash Fortran 77で書かれた数値モデルのコードをコンパイルし、計算開始から、計算終了までの時間を測定するまでのシェルスクリプト。
1. boundarycondition.py 数値モデルに与えた条件を図示する。対馬暖流の流量、対馬海峡の水温、海面の熱フラックスのグラフを描く。
1. mkcsv.py 数値モデルの出力された結果をcsvに変換する関数。 
1. frito.py 数値モデルの結果を図に起こす。出力される図は圧力のコンター図とベクトル図を重ねたもの、水温の分布図、1層目の層厚の分布図。また、標準入力によって選択するディレクトリを変更できる。
1. frddiff.py 海面冷却の強い条件を与えたモデルと海面冷却が平均的なモデルの1層目の層厚の差の分布図を描く。＊frito.pyによってcsvファイルが作成されていることを前提とするため、先にfrito.pyを実行する必要がある。
1. pomtest.py 数値モデルに正しく条件が与えられているか確認するため、出力データを図示する。
1. notify.py Line notifyの機能を使い、Lineに通知を送ることができる。これをジョブ実行の後に &&でつけることで、ジョブの終了をLineで通知する。
    https://qiita.com/aoyahashizume/items/13848b013daa18f6461b より
1. wtspatially.py　数値モデルに与える海面冷却の空間分布を図示する。
1. japanmap.bash GMTで日本地図を描く。
>------------------------------------------------------------------------------------------------------------------------------
### JRA55(日本海周辺の風のデータセット)関連

1. avesample.f JRA55の風のデータを月平均データに直す。
1. loop.bash JRA55の風の月平均データをベクトル図にし、地形データをのせる
1. windfitting.f90 JRA55の月平均データに加重平均をかけて加工する。これにより月平均データを数値モデルのグリッド間隔にあわせる。
1. fittingtest.bash GMTにより、windfitting.f90により作成したデータのベクトル図を描く。
>------------------------------------------------------------------------------------------------------------------------------

### 旧バージョン(現在使用していない)
1. calang.f90 数値モデルの出力結果を加工する。
1. fr.bash 加工された出力結果をGMTを使ってベクトル図にする。
>------------------------------------------------------------------------------------------------------------------------------
- 作成した図のサンプルはartディレクトリに格納した。
