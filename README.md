# Python Line OpenGPT API
此範例使用Line進行 `ChatGPT` AI聊天機器人。

## Getting Started
### Clone Project
你可以在本機直接使用 git 指令 clone 此專案並執行。

```
git clone https://github.com/uchpython12/line_chatgpt
cd https://github.com/uchpython12/line_chatgpt
```

### Docker Build Image
Docker自動打包image 本地端安裝請跳至Installation, docker run過後可直接訪問 [localhost:8888](http://localhost:8888/

```
docker build -t line_chatgpt .
docker run -p 8888:8888 line_chatgpt
```

### Installation
此專案下載至桌面後，使用以下指令安裝必要套件。

```
pip install -r requirements.txt
```

### line.xlsx
修改xlsx，寫上自己的key

```
auth_token=""
id=""
openai_key=""
```

### Running the Project
套件安裝成功後，即可開始執行本專案。

```
python run.py
```

running locally! Your app should now be running on [localhost:8888](http://localhost:8888/).