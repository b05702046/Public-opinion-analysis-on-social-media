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
      a. 發文時間：
      ![image](https://user-images.githubusercontent.com/51256347/123589851-6fb8d480-d81c-11eb-8cdb-add0b29781ad.png) 
      DCARD：在晚上發文的比例偏少，可能和使用者多為大學生有關，故無上班上課時間限制，不一定只能在晚上發文，且較為晚睡，凌晨時間的發文比例較高。
      PTT：兩個版的發文時間趨勢差異不大；且因為社會人士較多，故發文時間在凌晨時偏少，中午休息與下班時間後最高；休息時間越晚的人越少（半夜12點至凌晨5點的發文數量呈線性下降）、越接近中午發文越多
      （凌晨5點至中午12點的發文數量呈線性上升)，這可能也反映人在工作中不專心的程度也是線性成長的。
      b. 情緒狀態：
      ![image](https://user-images.githubusercontent.com/51256347/123589952-95de7480-d81c-11eb-982e-1496f90edb0c.png)
      
      DCARD（計算每一種表情符號在一篇文章中的比例，最後對每個表情取所有文章的平均），最常被使用的前三個表情符號為愛心、森77及哈哈，其中第一名(愛心)的比例又高出第二名(森77) 達8倍之多，可見DCARD時事版的使用者多願意給與正向的回饋。
      PTT（中間的圖為推文比例，右邊的圖為噓文比例；由於兩個版的走勢差不多，因此僅列出八卦版的圖)，原以為諸如政黑板這類的黑特文章論壇中，負面情緒會明顯較高，結果噓文比例比想像中的低許多，可見政黑板的文章內容應真的是民眾有感而發而寫出，並能得到大部分用戶的共鳴，並非單純為了黑特而黑特使得言論趨於偏激。




