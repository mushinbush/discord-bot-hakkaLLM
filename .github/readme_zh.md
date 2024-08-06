[English](https://github.com/mushinbush/discord-bot-hakka/blob/main/.github/readme.md) | 中文

## 介紹：

J 是個 Discord 聊天機器人，利用一些 API 運行對話模型的 Discord 聊天機器人，有下列功能：

- 簡單的一鍵安裝，只需下載並直接部署（需要安裝 Python）。
- 在 Discord 中用 LLM 模型進行對話交流，這些 API 目前是免費的！
- 可以自定義個性，讓你設定 bot 的行為跟功能。
- 目前支持：Google [Gemini](https://ai.google.dev/gemini-api)，Cohere [Command-R+](https://docs.cohere.com/docs/rate-limits)。

## 使用方法：
### Windows
1. 從 [Google Gemini](https://ai.google.dev/gemini-api) 或 [Cohere](https://dashboard.cohere.com) 取得你自己的 API 金鑰。
2. 創建你的 Discord 機器人，並從 [Discord 開發者門戶](https://discord.com/developers/applications) 取得你的 Discord bot token。
3. 安裝 [Python](https://www.python.org/)。安裝過程中務必勾選「Add Python X.X to PATH」！
4. git clone 這個repo，或者直接下載下來使用也可以 (Code -> Download ZIP)。
5. 運行 `start.bat` ；這會創建一個虛擬環境（venv）並安裝必要的依賴項。
6. 將你的 API 金鑰和 Discord 機器人令牌輸入到 `config.json` 文件中，然後重新運行 `start.bat`。你可以更換為你指定的模型。
7. 完成！
### Linux
1. 步驟與 Windows 幾乎相同，只是改成運行 `start.sh` 就好。

## 設定：

- 你可以在 `config.json` 中修改 bot 的設定：
  - `sysprompt`：定義命令、個性等的系統指示。
  - `sysfstmsg`：機器人的範例訊息，可以更好地指示你希望的 bot 的說話方式。
  - `trigger`: bot 的觸發詞，當訊息以設定的`trigger`開頭，就會觸發 bot 的回應。預設是`AI,`。
  - `cleantrig`: bot 的清除記憶體觸發詞，當訊息以設定的`cleantrig`開頭，就會清除目前 bot 的記憶體。預設是`cleanAI`。