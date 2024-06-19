[English](https://github.com/mushinbush/discord-bot-gemini/blob/main/.github/readme.md) | 中文
## 介紹：

J 是個 Discord 聊天機器人，利用 Google 的 [Gemini](https://ai.google.dev/gemini-api) API 運行對話模型。提供以下功能：

- 簡單的一鍵安裝，只需下載並直接部署。
- 在 Discord 中用 Gemini API 提供的LLM模型進行對話交流，目前是免費的(gemini-1.5-flash)！
- 可以自定義個性，讓你設定 bot 的行為跟功能。
- 如果你有錢，你可以花錢用更強大的模型。

## 使用方法：
### Windows
1. 從 [Google Gemini](https://ai.google.dev/gemini-api) 取得你自己的 Gemini API。
2. 創建你的 Discord 機器人，並從 [Discord 開發者門戶](https://discord.com/developers/applications) 取得你的 Discord bot token。
3. 安裝 [Python](https://www.python.org/)。安裝過程中務必勾選「Add Python X.X to PATH」！
4. git clone 這個repo，或者直接下載下來使用也可以 (Code -> Download ZIP)。
5. 運行 `start.bat` ；這會創建一個虛擬環境（venv）並安裝必要的依賴項。
6. 將你的Gemini API金鑰和Discord機器人令牌輸入到 `config.json` 文件中，然後重新運行 `start.bat`。
7. 完成！

## 設定：

- 你可以在 `config.json` 中修改 bot 的設定：
  - `sysprompt`：定義命令、個性等的系統指示。
  - `sysfstmsg`：機器人的範例訊息，可以更好地指示你希望的 bot 的說話方式。
  - `trigger`: bot 的觸發詞，當訊息以設定的`trigger`開頭，就會觸發 bot 的回應。預設是`AI,`。
  - `cleantrig`: bot 的清除記憶體觸發詞，當訊息以設定的`cleantrig`開頭，就會清除目前 bot 的記憶體。預設是`cleanAI`。