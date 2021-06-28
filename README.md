# Public-opinion-analysis-on-social-media

### 專案目標：
　　目標為了解網路社群中對於時事與政治類相關議題的討論程度，以及不同論壇的用戶對時事相關議題的情緒狀態。而本專案選定的研究資料來源為台灣兩大知名網路論壇 PTT 和 Dcard 中時事類討論人氣較高的看板，分別為 PTT的政黑板 (HatePolitic) 、八卦板 (Gossiping) 以及 Dcard 時事板 (Trending) 的討論內容作分析。
  
  
### 專案執行方法：
   本專案內容主要分為以下三個部分：
   1. 資料取得：以網路爬蟲方式分別取得 PTT 政黑板、八卦板、Dcard 時事板 2020 年的討論文章以及其推噓文 (留言)。
   2. 資料敘述分析：將取得的資料做初步的敘述分析，包含了解用戶使用形態以及推噓文、文章總讚數等資料做初步的了解。
   3. 看板輿情分析：以中研院所提供的開放套件 (CKIP、CsentiPackage) 對文章內容以及特定政治或時事議題作情緒分析，以正面或負面的情緒狀態表示之。
   
### 內容與產出：
   **1. 資料取得部分：**
   
   a. PTT：使用python之scrapy套件爬取ptt HatePolitics版及Gossiping板2020/1/1至2020/12/29之文章標題與文章內容。前者爬得78,508筆資料，後者爬得737,011筆資料。
      
   b. Dcard：以 Dcard所提供之 API 爬取時事板 2020 年的文章內容並記錄文章相關資訊如下表
   
   ![image](https://user-images.githubusercontent.com/51256347/123589770-47c97100-d81c-11eb-92f8-a4afc15f6fcf.png)
   
   **2. 資料敘述分析部分：**
   
   a.發文時間：
   
   ![image](https://user-images.githubusercontent.com/51256347/123589851-6fb8d480-d81c-11eb-8cdb-add0b29781ad.png)
   
   DCARD：在晚上發文的比例偏少，可能和使用者多為大學生有關，故無上班上課時間限制，不一定只能在晚上發文，且較為晚睡，凌晨時間的發文比例較高。
   
   PTT：兩個版的發文時間趨勢差異不大；且因為社會人士較多，故發文時間在凌晨時偏少，中午休息與下班時間後最高；休息時間越晚的人越少（半夜12點至凌晨5點的發文數量呈線性下降）、越接近中午發文越多（凌晨5點至中午12點的發文數量呈線性上升)，這可能也反映人在工作中不專心的程度也是線性成長的。
   
   b. 情緒狀態：
   
   ![image](https://user-images.githubusercontent.com/51256347/123589952-95de7480-d81c-11eb-982e-1496f90edb0c.png)
   
   DCARD（計算每一種表情符號在一篇文章中的比例，最後對每個表情取所有文章的平均），最常被使用的前三個表情符號為愛心、森77及哈哈，其中第一名(愛心)的比例又高出第二名(森77) 達8倍之多，可見DCARD時事版的使用者多願意給與正向的回饋。
   
   PTT（中間的圖為推文比例，右邊的圖為噓文比例；由於兩個版的走勢差不多，因此僅列出八卦版的圖)，原以為諸如政黑板這類的黑特文章論壇中，負面情緒會明顯較高，結果噓文比例比想像中的低許多，可見政黑板的文章內容應真的是民眾有感而發而寫出，並能得到大部分用戶的共鳴，並非單純為了黑特而黑特使得言論趨於偏激。
   
   c. 文字雲分析：
   
   ![image](https://user-images.githubusercontent.com/51256347/123591271-56b12300-d81e-11eb-9d08-f429ebe9eb1f.png)
   
   DCARD：
    男性常用的字和整體用戶常用的字差不多（因為男性佔整體用戶比例達5/6），裡頭的字多為政治人物的名字，看不出明顯的政治傾向，可能是因為政治傾向的比例差不多故效果被平衡掉；反觀女性的用字似乎與政治較為無關，貼文目的多為尋求問題解答或分享資訊。 
    
   PTT_HatePolitics：
    在推文比例高的標題文字雲中，較無特定用字特別顯眼的情形；反觀噓文比例高的標題文字雲中，較顯眼的多為政治人物的名字，包含蔡英文、柯文哲、侯友宜、陳時中等人，推測政黑板的政治傾向應較為偏藍。
    
   PTT_Gossiping：
    八卦版的文章主題較雜，但由文字雲可看出主要還是談論政治或武漢肺炎等時事為主。在噓文比例高的標題文字雲中，亦出現如網紅愛莉莎莎等非政治性人物。


  **3. 看板輿情分析部分：**
  
   a. 輔助套件：
   
   使用了中研院資訊所CKIP Lab研發的CKIP Tagger —開源的斷詞、詞性標注、實體辨識系統和台灣大學自然語言處理實驗室的NTUSD正、負面詞辭典，還有百度停用詞辭典來進行斷詞和情緒分析的工作。斷詞時候，必需篩走一些無關重要的詞性的字詞以及標點符號。
   
   b. 分析結果：
   
   我們分析情緒的指標是以文章內容正面字詞數量減掉文章內容負面字詞數量，若為正數代表使用正面字詞頻率多於負面字詞頻率，被視為正面文章；若相減後為零，則為中立傾向的文章，下面會展示正、負面傾向文章的圖表。
   
   ![image](https://user-images.githubusercontent.com/51256347/123592476-d55a9000-d81f-11eb-8f57-f548ccc9fa99.png)

  c. 各版情緒狀態與文字雲：
  
  政黑板：
  
  ![image](https://user-images.githubusercontent.com/51256347/123592584-fc18c680-d81f-11eb-99d0-a568c6c08ca7.png)
  
  ![image](https://user-images.githubusercontent.com/51256347/123592601-02a73e00-d820-11eb-8a5c-24c46efb93d4.png)

  八卦版：
  
  ![image](https://user-images.githubusercontent.com/51256347/123592636-12268700-d820-11eb-8710-dff8e622fe67.png)
  
  ![image](https://user-images.githubusercontent.com/51256347/123592656-18b4fe80-d820-11eb-99e7-5c50339390c8.png)
  
  Dcard時事版：
  
  ![image](https://user-images.githubusercontent.com/51256347/123592715-2e2a2880-d820-11eb-968f-84227dca7430.png)
  
  ![image](https://user-images.githubusercontent.com/51256347/123592736-35513680-d820-11eb-941b-f429371fee53.png)
  
  d. 對2020 總統參選人以及熱門人選之情緒分析：
  
  由下方圖表可以發現，各自的傾向都頗為接近的，其中負面文章的比例，以柯文哲為最多，佔57.9%，其次是蔡英文的56.7%，最後是韓國瑜的55.7%。正面文章的比例的排名也是相同，柯文哲的正面文章比例有32.0%，蔡英文的有31.2%，韓國瑜的有30.7%。
  
在圖表可以發現，各自的傾向都頗為接近的，其中負面文章的比例，以柯文哲為最多，佔57.9%，其次是蔡英文的56.7%，最後是韓國瑜的55.7%。正面文章的比例的排名也是相同，柯文哲的正面文章比例有32.0%，蔡英文的有31.2%，韓國瑜的有30.7%。

![image](https://user-images.githubusercontent.com/51256347/123592836-57e34f80-d820-11eb-949b-2fcd48142cfb.png)

以月份單獨分析他們的情緒走向的話，可以發現：

![image](https://user-images.githubusercontent.com/51256347/123592875-692c5c00-d820-11eb-90a6-07a9146f9a6e.png)

![image](https://user-images.githubusercontent.com/51256347/123592883-6cbfe300-d820-11eb-9b55-23913123c488.png)

![image](https://user-images.githubusercontent.com/51256347/123592909-75b0b480-d820-11eb-8e2c-a79a54e588d2.png)


  e. 三者的負面詞文字雲：
  
  ![image](https://user-images.githubusercontent.com/51256347/123592969-895c1b00-d820-11eb-9dcc-122e2540d0af.png)
  
  ![image](https://user-images.githubusercontent.com/51256347/123593007-924cec80-d820-11eb-8f56-61dbee5d3ff9.png)
  
  f. 三者正面詞文字雲：
  
  ![image](https://user-images.githubusercontent.com/51256347/123593048-a1339f00-d820-11eb-897b-ff70e3234c9f.png)
  
  ![image](https://user-images.githubusercontent.com/51256347/123593059-a55fbc80-d820-11eb-9857-3853a92448b3.png)
  
  
### 結論：
  
　　本專案透過研究分析兩大論壇時事類討論文章不僅發現了各自的用戶使用狀況，也發現雖然在推噓文數統計上噓文比例並不會特別高，但是在情緒分析部分用戶的負面情緒比例普遍偏高，推測可能在這些論壇上發表意見的網友大都是想抒發對於政治狀況的不滿，因此可能在用詞遣句上充滿較多負面情緒字眼。
  
　　然而本專案在進行文字處理中也發現課堂上所教的套件在處理中文文本時沒辦法較準確的切詞，而在多方嘗試之下選用了台灣中研院所開發的套件能較符合繁體中文文本的斷詞，但礙於時間與硬體資源不足沒辦法對完整的文本作分析 （情緒分析為隨機選取各看板1000篇文章）是這次專案比較美中不足的地方。


### 參考資料：

1.	Dcard API：
https://www.dcard.tw/service/api/v2
2.	Dcard 爬蟲說明：https://blog.jiatool.com/posts/dcard_api_v2/
3.	中研院中文詞庫小組：https://ckip.iis.sinica.edu.tw/
4.	Chen W.-F. and Ku L.-W., “中文情感語意分析套件 CSentiPackage 發展與應用,” 圖書館學與資訊科學, 2018.：https://reurl.cc/mqLyWW





  
















