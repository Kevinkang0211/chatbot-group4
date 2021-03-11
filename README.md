### 2021 Microsoft x TSMC careerhack 決賽
### 主題：聊天機器人 - 美食公道伯

## 開發語言、工具及服務
- Python 3.6
- Microsoft Azure Service, including LUIS, SQL database, Application Insights.
- QnA Maker
- google map API
- Line messaging API
- 爬蟲相關工具(Selenium、Beautifulsoup...)


## 主題緣由、介紹
![image](https://github.com/Kevinkang0211/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%871.jpeg)
![image](https://github.com/Kevinkang0211/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%873.jpeg)
![image](https://github.com/Kevinkang0211/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%874.jpeg)
![image](https://github.com/Kevinkang0211/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%875.jpeg)
![image](https://github.com/Kevinkang0211/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%876.jpeg)
![image](https://github.com/Kevinkang0211/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%877.jpeg)
![image](https://github.com/Kevinkang0211/chatbot-group4/blob/master/%E6%8A%95%E5%BD%B1%E7%89%878.jpeg)

## APP DEMO 畫面
加入好友

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/demo_%E5%8A%A0%E5%85%A5%E5%A5%BD%E5%8F%8B.png" width="500" height="900">

四大功能，包括使用說明、個人化推薦、瀏覽紀錄、我的最愛

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/demo_%E5%9B%9B%E5%80%8B%E5%8A%9F%E8%83%BD.png" width="500" height="900">

個人化推薦

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/demo_%E5%80%8B%E4%BA%BA%E5%8C%96%E6%8E%A8%E8%96%A6.png" width="500" height="900">

使用方式：可輸入我想吃XX or 我在哪 or 我在XX想吃YY，系統都會推薦給您餐點

e.g. 我在公館

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/demo_%E6%88%91%E5%9C%A8%E5%85%AC%E9%A4%A8.png" width="500" height="900">

e.g. 我想吃牛排

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/demo_%E6%88%91%E6%83%B3%E5%90%83%E7%89%9B%E6%8E%92.png" width="500" height="900">

e.g. 我想在文山區喝咖啡

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/demo_%E6%88%91%E6%83%B3%E5%9C%A8%E6%96%87%E5%B1%B1%E5%8D%80%E5%96%9D%E5%92%96%E5%95%A1.png" width="500" height="900">

點擊預算之後，系統就會發送美食字卡給使用者

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/demo_%E6%88%91%E5%9C%A8%E5%85%AC%E9%A4%A8%EF%BC%84%EF%BC%84%EF%BC%84.png" width="500" height="900">

點擊地圖會導到google map應用程式app

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/demo_%E5%9C%B0%E5%9C%96.png" width="500" height="900">

點擊評論會抓各大美食部落格的字卡給使用者

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/demo_%E8%A9%95%E8%AB%96.png" width="500" height="900">


## 作法
- 透過Azure的自然語言模型LUIS來對使用者的輸入進行分析判斷，知道其intent後以擷取句子中的entity來進行相對應的推薦
- 透過QnA Maker建立知識庫，以及聊天機器人相對應的問與答支援
- 使用google map API查看餐廳的地理位置以及相對應的評分
- 透過BOT Framework模擬器來模擬、測試ai chatbot功能
- 利用beautifulsoup、selenium等模組進行美食部落爬蟲
- 以Line作為channel跟使用者互動

## Chatbot Flow

<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/chatbot flow.jpg" width="450" height="300">
<img src="https://github.com/Kevinkang0211/chatbot-group4/blob/master/chatbot flow2.jpg" width="450" height="300">

### Install Python 3.6

## Running the sample
- Run `pip install -r requirements.txt` to install all dependencies
- Run `python app.py`


## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:3978/api/messages`


## Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)
