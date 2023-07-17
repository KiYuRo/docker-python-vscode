# DockerHubにあるpythonのイメージ指定する
FROM python:3.11-slim

# 作業ディレクトリをworkspaceに変更
WORKDIR /workspace/.devcontainer/web

# ローカルPCのrequirements.txtをコンテナのカレントディレクトリ（上で指定した場所）にコピー
COPY requirements.txt ${pwd}

# pipのアップデート
RUN pip install --upgrade pip

# pythonパッケージをインストール
RUN pip install -r requirements.txt
