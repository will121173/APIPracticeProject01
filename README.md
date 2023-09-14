# APIPracticeProject01
202309勉強会用パブリックリポジトリ

## 簡易構成図
![](res/readme_kousei.jpg)


## 1. 初回起動リンク
GitHub上から、下記リンクでIDEに遷移する  
→ [open in gitpod](https://gitpod.io/#github.com/will121173/APIPracticeProject01)


## 2. サンプル作成・デプロイ
（ここからはGitPod上で操作する）

TERMINALタブで以下を実行する
- APIのホスト用コマンド
- Webページのホスト用コマンド
- 外部からのアクセス許可
- src/web/index.htmlの1行をコメントを元に修正
- src/web/sampleJS.jsの1行をコメントを元に修正


### APIのホスト用コマンド
`uvicorn main:app --reload --port 3000`  

※main.pyのあるディレクトリで実行
```
例:
cd src/api/
uvicorn main:app --reload --port 3000
```

### Webページのホスト用コマンド
`python -m http.server 8000`  

※index.htmlのあるディレクトリで実行  
※APIのホスト用コマンドとは別のTerminalで実行  
　（ターミナル追加ボタン・画像参照）

```
例:
cd src/web/
python -m http.server 8000
```

![](res/readme_terminal.png)



### 外部からのアクセス許可
下部ウィンドウのPORTSタブ > port3000の行をpublic(鍵が空いている状態)にする  
下部ウィンドウのPORTSタブ > port8000の行をpublic(鍵が空いている状態)にする  

![](res/readme_ports.png)


## 3. 接続テスト①
PORTSタブのport番号8000の行にあるURLへアクセス、サンプルページがうまく表示できればOK 

## 4. 接続テスト②
1. PORTSタブのport番号8000の行にあるURLへ「スマホ等別ネットワークの機器」からアクセス、サンプルページがうまく表示できる  
2. PORTSタブのport番号8000の行にあるURLへ「スマホ等別ネットワークの機器」からアクセス、サンプルページがうまく表示できる  

接続テスト②までOKなら当日ワークの準備もOK！後は自由に制作してください


## 5. その他
GitPodのワークスペースは2週間以上操作しないと消えてしまいます。
念のため下記Zip化コマンドを使用してバックアップしてください。

### Zip化コマンド:  
`zip -r project.zip /workspace/APIPracticeProject01`  
カレントディレクトリにZipで全体が保存される。プロジェクト名を変えている場合はパスが変わるので注意  
→ ファイル右クリックからダウンロード
