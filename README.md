# 日本海における対馬暖流第３分枝の経年変化
![対馬暖流](https://github.com/RyosukeDTomita/paper2020/blob/master/art/japansea.png "日本海")
## 研究内容
- 対馬暖流第三分枝(上図参照)の流路が経年変化する現象について、海洋大循環モデルの一つである[POM](http://www.ccpo.odu.edu/POMWEB/index.html)を改造した1.5層モデルを用いた物理的メカニズムを明らかにする。研究内容については本ページの[Wiki](https://github.com/RyosukeDTomita/paper2020/wiki/%E7%A0%94%E7%A9%B6%E6%A6%82%E8%A6%81 "研究概要")をご覧ください。
******
## 本リポジトリの概要
- 2020年2月末に提出した卒業論文を執筆するにあたり、行った数値モデルの解析を目的としたプログラムが主である。。
- 作成した図のサンプルは[/art](https://github.com/RyosukeDTomita/paper2020/tree/master/art)に格納した。
******
### 数値モデルの解析に用いたプログラム
******
#### [/model](https://github.com/RyosukeDTomita/paper2020/tree/master/model)

    1. auto.bash             Fortran77で書かれた数値モデルのコードをコンパイルし、計算開始から、計算終了までの時間を測定するまでのシェルスクリプト。
    2. boundarycondition.py  数値モデルに与えた条件を図示する。対馬暖流の流量、対馬海峡の水温、海面の熱フラックスのグラフを描く。
    3. mkcsv.py              数値モデルの出力された結果をcsvに変換する関数。 
    4. frito.py              数値モデルの結果を図に起こす。出力される図は圧力のコンター図とベクトル図を重ねたもの、水温の分布図、1層目の層厚の分布図。また、標準入力によって選択するディレクトリを変更できる。
    5. frddiff.py            海面冷却の強い条件を与えたモデルと海面冷却が平均的なモデルの1層目の層厚の差の分布図を描く。＊frito.pyによってcsvファイルが作成されていることを前提とするため、先にfrito.pyを実行する必要がある。
    6. pomtest.py            数値モデルに正しく条件が与えられているか確認するため、いくつかの出力データの時系列をグラフにする。計算するのは対馬海峡の流量、1層目の境界面の深さの平均、水温の平均、対馬海峡の水温の平均、流速の平均である。
    7. notify.py             Line notifyの機能を使い、Lineに通知を送ることができる。これをジョブ実行の後に &&でつけることで、ジョブの終了をLineで通知する。参考サイトは[こちら](https://qiita.com/aoyahashizume/items/13848b013daa18f6461b "notify.bash")
    8. wtspatially.py　      数値モデルに与える海面冷却の空間分布を図示する。
    9. japanmap.bash         GMTで日本地図を描く。
    10. frito.bash           frito.pyと同じ図をGMTによって書く。

### JRA55(日本海周辺の風のデータセット関連)
******
#### /JRA55

    1. avesample.f      JRA55の風のデータを月平均データに直す。
    2. loop.bash        JRA55の風の月平均データをベクトル図にし、地形データをのせる
    3. windfitting.f90  JRA55の月平均データに加重平均をかけて加工する。これにより月平均データを数値モデルのグリッド間隔にあわせる。
    4. fittingtest.bash GMTにより、windfitting.f90により作成したデータのベクトル図を描く。
### 旧バージョンや、その他
******
#### /old-version

    1. calang.f90  数値モデルの出力結果を加工する。
    2. fr.bash     加工された出力結果をGMTを使ってベクトル図にする。



