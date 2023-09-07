# APIPracticeProject01
202309勉強会用パブリックリポジトリ

## 1. 初回起動リンク
GitHub上から、下記リンクでIDEに遷移する  
→ [open in gitpod](https://gitpod.io/#github.com/will121173/APIPracticeProject01)


## 2. サンプル作成
（ここからはGitPod上で操作する）



## デプロイコマンド
`uvicorn main:app --reload`  
※main.pyのあるディレクトリで実行


## 外部からのアクセス許可
下部ウィンドウのPORTSタブ > いずれかの行をpublic(鍵が空いている状態)にする  

![](res/readme_ports.png)

## Zip化コマンド:  
`zip -r project.zip /workspace/APIPracticeProject01`  
カレントディレクトリにZipで全体が保存される。プロジェクト名を変えている場合はパスが変わるので注意  
→ ファイル右クリックからダウンロード
