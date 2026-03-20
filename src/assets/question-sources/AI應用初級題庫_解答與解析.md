# AI 應用初級課程題庫解析

本檔提供題庫題目的完整解析與說明。

---

### Q1: 下列哪一項最能描述人工智慧（AI）的核心目標？

- (A) 完全取代人類在所有領域的工作。
- (B) 開發出能夠獨立思考和行動的通用智慧體。
- <span style='color: #0066cc; font-weight: bold;'>(C) 使機器能夠執行原本需要人類智慧才能完成的任務，如學習和推理。</span>
- (D) 僅用於分析大量數據以發現隱藏的模式。

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 使機器能夠執行原本需要人類智慧才能完成的任務，如學習和推理。</span>  
<span style='color: #646464;'>💡 為什麼？ AI的核心目標是讓機器具備人類的認知能力，如學習、推理和解決問題，而非完全取代人類。</span>

---

### Q2: 分析型AI的主要功能是什麼？

- (A) 預測未來的趨勢和行為。
- <span style='color: #0066cc; font-weight: bold;'>(B) 洞悉數據模式，分析和處理大量數據，以提供有價值的見解。</span>
- (C) 根據使用者輸入的提示詞生成各類素材。
- (D) 模擬人類的感知環境能力。

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 洞悉數據模式，分析和處理大量數據，以提供有價值的見解。</span>  
<span style='color: #646464;'>💡 為什麼？ 分析型AI透過尋找數據中的隱藏模式，來進行趨勢預測與提出洞察。</span>

---

### Q3: 在機器學習的基本原理中，下列哪一個敘述是正確的？

- (A) 機器學習模型只能處理結構化數據
- (B) 機器學習需要人工專家手動設計所有特徵
- <span style='color: #0066cc; font-weight: bold;'>(C) 機器學習透過分析大量的歷史數據，使系統能夠構建預測模型並在新數據到來時進行動態更新</span>
- (D) 機器學習模型一旦訓練完成，其效能不會隨著新數據而改變

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 機器學習透過分析大量的歷史數據，使系統能夠構建預測模型並在新數據到來時進行動態更新</span>  
<span style='color: #646464;'>💡 為什麼？ 核心是透過分析大量歷史資料進行模型訓練與預測，並在新數據到來時更新。</span>

---

### Q4: 下列哪一種機器學習方法透過讓代理（Agent）與環境互動並接收獎勵或懲罰來學習最佳行為策略？

- (A) 監督式學習
- (B) 非監督式學習
- <span style='color: #0066cc; font-weight: bold;'>(C) 強化學習</span>
- (D) 深度學習

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 強化學習</span>  
<span style='color: #646464;'>💡 為什麼？ 以此互動機制為核心，透過獎勵或懲罰學習最佳行為策略的即為強化學習。</span>

---

### Q5: 鑑別式AI與生成式AI在主要目標上的根本區別是什麼？

- (A) 鑑別式AI旨在生成新數據，而生成式AI專注於分類
- <span style='color: #0066cc; font-weight: bold;'>(B) 鑑別式AI的目標是透過學習數據的決策邊界來進行分類或預測，而生成式AI側重於學習數據的內在分佈，並基於該分佈生成新的數據</span>
- (C) 鑑別式AI主要應用於內容創建與數據增強，而生成式AI主要應用於分類、辨識與預測
- (D) 鑑別式AI的輸出是新的數據樣本，而生成式AI的輸出通常是分類標籤或數值預測

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 鑑別式AI的目標是透過學習數據的決策邊界來進行分類或預測，而生成式AI側重於學習數據的內在分佈，並基於該分佈生成新的數據</span>  
<span style='color: #646464;'>💡 為什麼？ 鑑別式AI旨在學習決策邊界來分類，而生成式AI側重學習內在分佈以生成新樣本。</span>

---

### Q6: 深度學習模型中的神經網路透過多層結構學習特徵。這種多層結構的主要優勢是什麼？

- (A) 它減少了模型訓練所需的計算資源
- (B) 它使得模型更容易避免過擬合的問題
- <span style='color: #0066cc; font-weight: bold;'>(C) 它能自動從大量數據中提取深層且抽象的特徵</span>
- (D) 它消除了對非線性激活函數的需求

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 它能自動從大量數據中提取深層且抽象的特徵</span>  
<span style='color: #646464;'>💡 為什麼？ 神經網路多層隱藏層的功能就是無需人工特徵工程，自動提取高階、抽象的特徵。</span>

---

### Q7: 為了減輕深度學習模型中的過擬合問題 ，下列哪一種方法通常被採用？

- (A) 減少訓練數據量
- (B) 增加模型複雜度
- (C) 提高學習率
- <span style='color: #0066cc; font-weight: bold;'>(D) 增加正則化項</span>

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(D) 增加正則化項</span>  
<span style='color: #646464;'>💡 為什麼？ 正則化（如L1/L2或Dropout）能限制模型複雜度，防止過擬合。</span>

---

### Q8: 資料偏見（Bias in Data）在AI系統中可能導致什麼不良後果？

- (A) 降低模型在訓練數據上的準確性
- (B) 增加模型訓練所需的時間
- <span style='color: #0066cc; font-weight: bold;'>(C) 模型可能會在分類時學習到數據的偏見，影響公平性與準確性</span>
- (D) 使得模型難以處理非結構化數據

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 模型可能會在分類時學習到數據的偏見，影響公平性與準確性</span>  
<span style='color: #646464;'>💡 為什麼？ 包含偏見的資料會導致偏見的模型決策，影響公平與準確。</span>

---

### Q9: 在AI治理中，為何需要國際合作？

- (A) 僅為了統一全球AI技術的發展標準
- (B) 主要目的是促進AI技術從發達國家向發展中國家的轉移
- (C) 僅為了避免AI技術被用於惡意目的
- <span style='color: #0066cc; font-weight: bold;'>(D) 以上皆是</span>

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(D) 以上皆是</span>  
<span style='color: #646464;'>💡 為什麼？ 國際合作旨在統一標準、促進轉移發展、防止AI遭惡意濫用。</span>

---

### Q10: 生成對抗網路（GAN）的核心組成部分是什麼？

- (A) 編碼器和解碼器
- (B) 分類器和回歸器
- <span style='color: #0066cc; font-weight: bold;'>(C) 生成器和鑑別器</span>
- (D) 特徵提取器和決策器

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 生成器和鑑別器</span>  
<span style='color: #646464;'>💡 為什麼？ GAN由生成器(Generator)與鑑別器(Discriminator)藉由對抗學習來訓練。</span>

---

### Q11: 下列何者屬於非結構化資料？

- (A) Excel 表格
- (B) SQL 資料庫
- <span style='color: #0066cc; font-weight: bold;'>(C) 商品評論</span>
- (D) 包含明確欄位的表格

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 商品評論</span>  
<span style='color: #646464;'>💡 為什麼？ 商品評論屬於文字資料，無法直接放進表格式資料庫，為非結構化資料。</span>

---

### Q12: 預測型AI的主要應用領域為何？

- (A) 生產流程自動化
- <span style='color: #0066cc; font-weight: bold;'>(B) 市場預測與風險評估</span>
- (C) 內容創作與藝術設計
- (D) 醫療影像的精準診斷

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 市場預測與風險評估</span>  
<span style='color: #646464;'>💡 為什麼？ 預測型AI主要用於根據歷史數據對未來趨勢和風險進行預測。</span>

---

### Q13: 在機器學習的流程中，準備訓練資料包含哪些主要步驟？

- (A) 僅資料的蒐集與儲存
- (B) 資料的蒐集、模型演算法的選擇與參數調整
- <span style='color: #0066cc; font-weight: bold;'>(C) 資料的蒐集、過濾雜訊及前處理</span>
- (D) 模型效能的測試與評估

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 資料的蒐集、過濾雜訊及前處理</span>  
<span style='color: #646464;'>💡 為什麼？ 訓練資料的品質決定模型成效，必須經過蒐集、清洗、轉換等前處理步驟。</span>

---

### Q14: 監督式學習與非監督式學習最主要的區別在於

- (A) 監督式學習使用較少的資料量
- <span style='color: #0066cc; font-weight: bold;'>(B) 監督式學習使用帶有標記的資料進行訓練，而非監督式學習則否</span>
- (C) 非監督式學習的模型準確度通常較高
- (D) 監督式學習僅適用於分類問題，非監督式學習僅適用於分群問題

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 監督式學習使用帶有標記的資料進行訓練，而非監督式學習則否</span>  
<span style='color: #646464;'>💡 為什麼？ 是否有標記(Label)是監督式與非監督式學習兩者根本的差異。</span>

---

### Q15: 下列何者不是鑑別式AI的主要應用？

- (A) 垃圾郵件檢測
- (B) 人臉辨識
- (C) 情感分析
- <span style='color: #0066cc; font-weight: bold;'>(D) 根據文字描述生成圖像</span>

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(D) 根據文字描述生成圖像</span>  
<span style='color: #646464;'>💡 為什麼？ 根據文字生成圖像屬於典型的「生成式AI」任務。</span>

---

### Q16: 深度學習相較於傳統機器學習方法的主要優勢為何？

- (A) 需要較少的訓練數據
- <span style='color: #0066cc; font-weight: bold;'>(B) 能夠自動從數據中提取深層且抽象的特徵</span>
- (C) 模型的可解釋性更高
- (D) 對硬體設備的要求較低

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 能夠自動從數據中提取深層且抽象的特徵</span>  
<span style='color: #646464;'>💡 為什麼？ 深度學習能夠自動從大量數據中提取深層且抽象的特徵，減少對人工標註的依賴。</span>

---

### Q17: 在處理數據時，填補遺缺值的常見方法有哪些？

- (A) 僅刪除包含遺缺值的記錄
- <span style='color: #0066cc; font-weight: bold;'>(B) 使用統計方法填補（如平均值、中位數、眾數等）或利用插補法</span>
- (C) 將遺缺值直接替換為零
- (D) 僅適用於數值型數據

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 使用統計方法填補（如平均值、中位數、眾數等）或利用插補法</span>  
<span style='color: #646464;'>💡 為什麼？ 使用平均值、中位數或插補法填補，能在不嚴重影響資料集大小情況下保留特徵。</span>

---

### Q18: 下列哪一種探索性資料分析方法適用於展示多個變數兩兩之間的相關性？

- <span style='color: #0066cc; font-weight: bold;'>(A) 熱圖（Heatmap）</span>
- (B) 散佈圖矩陣（Scatter Plot Matrix）
- (C) 箱型圖/盒鬚圖（Box Plot）
- (D) 折線圖（Line chart）

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 熱圖（Heatmap）</span>  
<span style='color: #646464;'>💡 為什麼？ 熱圖（Heatmap）能透過二維矩陣與顏色深淺的變化，直觀地展示多個變數兩兩之間的「相關係數」高低，是特徵工程與共線性分析中最常用的探索性圖表。</span>

---

### Q19: AI治理的重要性體現在哪些方面？

- (A) 提高系統運行速度與效能
- <span style='color: #0066cc; font-weight: bold;'>(B) 確保AI技術發展過程中的倫理與法規遵循</span>
- (C) 降低AI模型的硬體成本與電力消耗
- (D) 強化人工智慧的自主學習與創造力

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 確保AI技術發展過程中的倫理與法規遵循</span>  
<span style='color: #646464;'>💡 為什麼？ AI治理主要確保技術發展過程符合倫理規範、法規與公平透明原則。</span>

---

### Q20: 生成對抗網路（GAN）的訓練目標是什麼？

- (A) 僅訓練生成器生成盡可能真實的數據
- (B) 僅訓練鑑別器準確判斷數據的真偽
- <span style='color: #0066cc; font-weight: bold;'>(C) 透過生成器和鑑別器之間的對抗學習，使得生成器能生成更逼真的數據</span>
- (D) 使生成器和鑑別器達到完全相同的判斷能力

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 透過生成器和鑑別器之間的對抗學習，使得生成器能生成更逼真的數據</span>  
<span style='color: #646464;'>💡 為什麼？ 透過生成器和鑑別器之間的對抗博弈，使得生成器最終能生成難以分辨真偽的數據。</span>

---

### Q21: 提升AI系統透明性的適當措施包括揭露AI系統的相關資訊，請問這樣做的主要目的是為了回應AI治理中的哪個重要概念？

- (A) 技術可行性
- <span style='color: #0066cc; font-weight: bold;'>(B) 可解釋性與信任</span>
- (C) 商業價值
- (D) 運算效率

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 可解釋性與信任</span>  
<span style='color: #646464;'>💡 為什麼？ 透明度與揭露機制的建立旨在讓使用者理解AI的決策並產生信任。</span>

---

### Q22: 下列關於資料來源的敘述，何者最可能影響資料的品質與代表性？

- (A) 資料儲存的硬體設備
- (B) 資料分析師的個人經驗
- <span style='color: #0066cc; font-weight: bold;'>(C) 資料蒐集的方法與範圍</span>
- (D) 資料視覺化的呈現方式

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 資料蒐集的方法與範圍</span>  
<span style='color: #646464;'>💡 為什麼？ 資料的品質基於蒐集，取樣偏差或範圍不當會嚴重損害其代表性。</span>

---

### Q23: 資料處理流程中，處理重複值的主要目的是什麼？

- (A) 提升資料的運算速度
- <span style='color: #0066cc; font-weight: bold;'>(B) 確保分析結果的準確性與可靠性</span>
- (C) 降低資料儲存的成本
- (D) 使資料更符合特定的格式要求

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 確保分析結果的準確性與可靠性</span>  
<span style='color: #646464;'>💡 為什麼？ 資料重複會使特定特徵權重偏移，導致模型偏差，因此需處理以確保可靠性。</span>

---

### Q24: 在AI專案中，保障資料隱私最直接的做法可能包含以下哪項？

- (A) 使用更複雜的AI模型
- (B) 提升資料分析的效率
- <span style='color: #0066cc; font-weight: bold;'>(C) 實施資料加密與存取控制</span>
- (D) 增加資料視覺化的互動性

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 實施資料加密與存取控制</span>  
<span style='color: #646464;'>💡 為什麼？ 資料加密與權限控管是防止未經授權存取的最基本、最直接保障措施。</span>

---

### Q25: 機器學習的基本原理是透過何種方式使機器具備預測與分類能力？

- (A) 人工編寫固定的程式邏輯
- <span style='color: #0066cc; font-weight: bold;'>(B) 透過數據訓練模型</span>
- (C) 依賴專家系統的知識庫
- (D) 模擬人類的直覺判斷

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 透過數據訓練模型</span>  
<span style='color: #646464;'>💡 為什麼？ 機器學習依賴從歷史資料中找出規律與模式，從而具備未知數據的預測分類能力。</span>

---

### Q26: 請問SVM主要透過以下哪個概念來進行分類？

- (A) 計算樣本之間的距離
- <span style='color: #0066cc; font-weight: bold;'>(B) 尋找最佳決策邊界</span>
- (C) 建立多個並行的決策樹
- (D) 模擬生物神經網路的結構

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 尋找最佳決策邊界</span>  
<span style='color: #646464;'>💡 為什麼？ 支持向量機(SVM)旨在尋找一個最大化間距的超平面作為最佳決策邊界。</span>

---

### Q27: 請問鑑別式AI的主要目標是？

- (A) 學習數據的內在分佈並生成新的數據
- <span style='color: #0066cc; font-weight: bold;'>(B) 學習數據的決策邊界以進行分類或預測</span>
- (C) 同時生成新的數據並進行準確的分類
- (D) 透過提示詞生成各類素材

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 學習數據的決策邊界以進行分類或預測</span>  
<span style='color: #646464;'>💡 為什麼？ 鑑別式AI的核心即是區分與判斷，藉由決策邊界對未知數據分類。</span>

---

### Q28: 在整合應用中，生成式AI產生的模擬數據如何幫助鑑別式AI？

- (A) 降低鑑別式AI模型的訓練難度
- (B) 加快鑑別式AI模型的部署速度
- <span style='color: #0066cc; font-weight: bold;'>(C) 擴展鑑別式AI的學習邊界，提升其泛化能力</span>
- (D) 減少鑑別式AI模型所需的硬體資源

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 擴展鑑別式AI的學習邊界，提升其泛化能力</span>  
<span style='color: #646464;'>💡 為什麼？ 模擬數據即為資料增強(Data Augmentation)，能有效提升模型的泛化能力。</span>

---

### Q29: 下列哪個選項不屬於大數據 5V？

- (A) Volume (大量)
- (B) Velocity (速度)
- (C) Variety (多樣)
- <span style='color: #0066cc; font-weight: bold;'>(D) Virtuality (虛擬性)</span>

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(D) Virtuality (虛擬性)</span>  
<span style='color: #646464;'>💡 為什麼？ 大數據5V為Volume, Velocity, Variety, Veracity, Value，不含Virtuality虛擬性。</span>

---

### Q30: 模型的主要功能是什麼？

- (A) 儲存大量的原始資料
- <span style='color: #0066cc; font-weight: bold;'>(B) 用來簡化和模擬真實世界，並進行預測或分類</span>
- (C) 自動生成新的訓練數據
- (D) 確保資料的安全性與隱私

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 用來簡化和模擬真實世界，並進行預測或分類</span>  
<span style='color: #646464;'>💡 為什麼？ 模型是將複雜的現實世界問題進行數學抽象化，方便進行預測或分類。</span>

---

### Q31: 在資料處理流程中，處理「遺缺值」的常見方法包括填補與刪除。請問在決定是否刪除包含大量遺缺值的記錄時，最重要的考量因素是什麼？

- (A) 遺缺值的具體數值大小
- (B) 處理遺缺值所需的時間成本
- <span style='color: #0066cc; font-weight: bold;'>(C) 刪除這些記錄是否會嚴重影響資料的代表性</span>
- (D) 目前可用的資料分析工具的功能限制

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 刪除這些記錄是否會嚴重影響資料的代表性</span>  
<span style='color: #646464;'>💡 為什麼？ 決定是否刪除帶有大量遺缺值的記錄時，最關鍵的考量是「刪除後是否會使資料集喪失代表性或平衡性」。若刪除後特定族群或情境的樣本嚴重減少，會導致模型的偏誤；相對地，遺缺值的具體大小並非決策的核心。</span>

---

### Q32: 敘述性分析中常用的統計指標，例如平均值與中位數。請問在分析一組包含極端值的數據時，哪個指標更能反映數據的集中趨勢？

- <span style='color: #0066cc; font-weight: bold;'>(A) 中位數</span>
- (B) 平均值
- (C) 標準差
- (D) 百分位數

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 中位數</span>  
<span style='color: #646464;'>💡 為什麼？ 中位數不受極端值（離群值）拉扯的影響，因此在偏態分佈中最能反映集中趨勢。</span>

---

### Q33: 相關性分析旨在測量兩個變量之間的關係。請問皮爾森相關係數主要衡量哪種關係？

- (A) 非線性關係
- (B) 時間序列上的依賴關係
- <span style='color: #0066cc; font-weight: bold;'>(C) 線性關係</span>
- (D) 因果關係

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 線性關係</span>  
<span style='color: #646464;'>💡 為什麼？ 皮爾森相關係數（Pearson Correlation Coefficient）專門用於衡量兩個連續變數之間「線性」相關的強度與方向，值域介於 -1（完全負相關）到 +1（完全正相關）之間。若需衡量非線性或排名關係，應改用史比曼（Spearman）等級相關係數。</span>

---

### Q34: 生成式AI模型的訓練過程，通常包含預訓練和微調兩個階段。請問微調階段的主要目的是什麼？

- (A) 學習數據的基本模式
- <span style='color: #0066cc; font-weight: bold;'>(B) 提升模型在特定任務或領域的表現</span>
- (C) 減少模型的參數數量
- (D) 加速模型的推論速度

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 提升模型在特定任務或領域的表現</span>  
<span style='color: #646464;'>💡 為什麼？ 預訓練學習通用知識，微調(Fine-tuning)則是為了適應下游特定任務或領域。</span>

---

### Q35: 下列何者不適合做為資料分布估計？

- (A) 直方圖（Histogram）
- (B) 散布圖（Scatter plot）
- <span style='color: #0066cc; font-weight: bold;'>(C) 雷達圖（Radar chart）</span>
- (D) 四分位數（Quartile）

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 雷達圖（Radar chart）</span>  
<span style='color: #646464;'>💡 為什麼？ 雷達圖多用於展示多維效能或能力評估；直方圖或散佈圖更適合用來展示資料分布。</span>

---

### Q36: K-Means 聚類算法中，K 代表什麼？

- (A) 數據集中特徵的數量
- (B) 數據集中樣本的數量
- <span style='color: #0066cc; font-weight: bold;'>(C) 所需劃分的群組數量</span>
- (D) 迭代次數

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 所需劃分的群組數量</span>  
<span style='color: #646464;'>💡 為什麼？ K-Means中的「K」代表使用者預先指定的群聚(Cluster)數量。</span>

---

### Q37: 深度學習模型中，下列哪一項通常用來降低過擬合問題？

- <span style='color: #0066cc; font-weight: bold;'>(A) 增加訓練數據量</span>
- (B) 增加模型的複雜度
- (C) 增加學習率
- (D) 增加正則化項

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 增加訓練數據量</span>  
<span style='color: #646464;'>💡 為什麼？ 增加訓練數據量讓模型見過更多樣化的範例，是緩解過擬合最根本的方式之一。更豐富的資料能使模型學到更通用的規律，而非只記住少數訓練案例的特定雜訊，自然提升泛化能力。</span>

---

### Q38: 鑑別式AI與生成式AI在模型目標上有所不同。請問以下哪個任務更可能由鑑別式AI完成？

- (A) 根據文字描述生成圖像
- <span style='color: #0066cc; font-weight: bold;'>(B) 判斷一封郵件是否為垃圾郵件</span>
- (C) 自動生成符合特定風格的音樂
- (D) 擴充現有的醫療影像數據集

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 判斷一封郵件是否為垃圾郵件</span>  
<span style='color: #646464;'>💡 為什麼？ 是否為垃圾郵件的判斷屬於「分類」任務，為典型的鑑別式AI應用。</span>

---

### Q39: 下列哪項技術是生成式 AI 發展的重要基礎？

- (A) 決策樹
- <span style='color: #0066cc; font-weight: bold;'>(B) 神經網路</span>
- (C) 線性迴歸
- (D) 貝氏分類

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 神經網路</span>  
<span style='color: #646464;'>💡 為什麼？ 深度學習與人工神經網路是現今生成模型（如Transformer、GAN）的基石。</span>

---

### Q40: 隨機森林（Random Forest）改進了單一決策樹的缺陷，主要透過什麼方法實 現？

- (A) 使用核函數映射高維空間
- <span style='color: #0066cc; font-weight: bold;'>(B) 集成多棵隨機生成的決策樹並投票</span>
- (C) 增加模型參數以減少偏差
- (D) 採用生成模型替代分類器

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 集成多棵隨機生成的決策樹並投票</span>  
<span style='color: #646464;'>💡 為什麼？ 隨機森林利用Bagging法，集成多棵決策樹的預測結果，以投票減少模型變異數。</span>

---

### Q41: 請問在醫療影像分析中，生成式AI生成的模擬病理影像的主要作用是什麼？

- (A) 加速鑑別式AI模型的部署
- (B) 降低鑑別式AI模型的訓練成本
- <span style='color: #0066cc; font-weight: bold;'>(C) 擴大鑑別式AI模型的訓練數據，提升其疾病識別能力</span>
- (D) 提高醫療影像的可解釋性

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 擴大鑑別式AI模型的訓練數據，提升其疾病識別能力</span>  
<span style='color: #646464;'>💡 為什麼？ 利用AI生成模擬影像能補足少見疾病的影像數量，進行資料增強。</span>

---

### Q42: 請問在交通領域，AI技術主要應用於哪些方面？

- (A) 疾病診斷與藥物研發
- <span style='color: #0066cc; font-weight: bold;'>(B) 自動駕駛與交通流量預測</span>
- (C) 風險評估與欺詐檢測
- (D) 自動化生產與品質控制

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 自動駕駛與交通流量預測</span>  
<span style='color: #646464;'>💡 為什麼？ 自動駕駛、交通流量監測預測是AI在交通領域最有代表性應用。</span>

---

### Q43: 關於鑑別式 AI，下列敘述何者較為正確？

- (A) 學習數據的聯合概率 P（x,y）
- <span style='color: #0066cc; font-weight: bold;'>(B) 專注於數據的分類或迴歸任務</span>
- (C) 主要用於生成新數據
- (D) 適合處理無標記數據

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 專注於數據的分類或迴歸任務</span>  
<span style='color: #646464;'>💡 為什麼？ 鑑別式AI不會生成新數據，而是對現有數據進行分類判別或數值預測(迴歸)。</span>

---

### Q44: 《AI Act》採取風險分級管理的方法規範AI應用。請問下列哪個AI應用可能被歸類為「不可接受風險」？

- (A) 提供顧客產品推薦的AI系統
- (B) 自動回覆常見問題的ChatBot
- <span style='color: #0066cc; font-weight: bold;'>(C) 用於社會信用評分的人臉辨識監控系統</span>
- (D) 用於拼字校正的AI工具

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 用於社會信用評分的人臉辨識監控系統</span>  
<span style='color: #646464;'>💡 為什麼？ 歐盟AI法案明確將具高度侵犯性（如大規模社會信用評分、人臉監控）列為禁止。</span>

---

### Q45: 下列何者屬於生成式 AI 使用之模型？

- (A) 支援向量機（SVM）
- (B) 邏輯迴歸（Logistic Regression）
- <span style='color: #0066cc; font-weight: bold;'>(C) 生成對抗網路（GAN）</span>
- (D) 隨機森林（Random Forest）

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 生成對抗網路（GAN）</span>  
<span style='color: #646464;'>💡 為什麼？ GAN就是生成對抗網路，為典型的生成式AI模型。</span>

---

### Q46: 下列哪一項屬於監督式學習的特點？

- <span style='color: #0066cc; font-weight: bold;'>(A) 數據集中包含標記訊息</span>
- (B) 僅需探索數據內部的結構
- (C) 使用代理與環境互動進行學習
- (D) 不需要驗證集來調整參數

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 數據集中包含標記訊息</span>  
<span style='color: #646464;'>💡 為什麼？ 監督式學習的資料集必須帶有已知答案(Label，標記)作為訓練依據。</span>

---

### Q47: 交叉驗證的主要目的是什麼？

- (A) 提高模型的訓練速度
- (B) 驗證數據是否線性可分
- <span style='color: #0066cc; font-weight: bold;'>(C) 減少模型的過擬合風險</span>
- (D) 測試模型的容錯能力

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 減少模型的過擬合風險</span>  
<span style='color: #646464;'>💡 為什麼？ 透過將資料集切割輪替驗證，能獲得更穩定、公正的模型效能評估並減少過擬合。</span>

---

### Q48: 機器學習的三個核心要素是什麼？

- <span style='color: #0066cc; font-weight: bold;'>(A) 數據、模型、損失函數</span>
- (B) 訓練集、測試集、驗證集
- (C) 特徵工程、優化演算法、正則化
- (D) 超參數調整、模型選擇、數據處理

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 數據、模型、損失函數</span>  
<span style='color: #646464;'>💡 為什麼？ 機器學習由輸入(Data)、處理(Model)及評估(損失函數Loss)三者驅動優化。</span>

---

### Q49: 關於「零樣本學習」（Zero-shot Learning），下列哪一個敘述最為正確？

- (A) 模型需先見過所有類別的訓練樣本才能進行分類
- <span style='color: #0066cc; font-weight: bold;'>(B) 模型能夠辨識從未在訓練中出現過的類別，依賴語意資訊或特徵關聯</span>
- (C) 這種學習方式僅適用於影像辨識任務，無法應用於語言模型
- (D) 零樣本學習的精確度通常遠高於有監督學習

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 模型能夠辨識從未在訓練中出現過的類別，依賴語意資訊或特徵關聯</span>  
<span style='color: #646464;'>💡 為什麼？ 模型能將學到的知識透過語意或特徵關聯，泛化並辨識未曾經歷過的類別。</span>

---

### Q50: 根據《金融業運用人工智慧指引》，為落實透明性與可解釋性原則，金融機構在使用AI與消費者互動時，應採取哪些做法？

- (A) 僅需內部了解AI的運作方式，無需向消費者說明
- (B) 可以選擇不揭露AI的使用以保護商業機密
- <span style='color: #0066cc; font-weight: bold;'>(C) 應適當揭露其正考慮之金融商品或服務係由AI提供的，並說明AI系統的功能與預期表現</span>
- (D) 只需要在消費者提出疑問時才進行簡要說明

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 應適當揭露其正考慮之金融商品或服務係由AI提供的，並說明AI系統的功能與預期表現</span>  
<span style='color: #646464;'>💡 為什麼？ 根據《金融業運用人工智慧指引》，透明性原則要求金融機構應向消費者主動揭露使用AI提供服務的事實，並說明其功能與預期表現，以確保消費者的知情權，建立信任基礎。「僅需內部了解」違反了可解釋性的要求。</span>

---

### Q51: No Code / Low Code平台的主要優勢之一是什麼？

- (A) 它們需要專業的程式設計師才能進行操作
- <span style='color: #0066cc; font-weight: bold;'>(B) 它們透過簡化開發流程，使更多非技術背景的人員能夠參與AI的創建與部署</span>
- (C) 它們提供的客製化程度非常有限
- (D) 它們通常適用於開發非常複雜且底層的系統

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 它們透過簡化開發流程，使更多非技術背景的人員能夠參與AI的創建與部署</span>  
<span style='color: #646464;'>💡 為什麼？ 無程式碼/低程式碼旨在透過視覺化介面簡化開發，讓一般業務人員也能建立AI應用。</span>

---

### Q52: 生成式AI在醫療保健領域的潛在應用包括：*

- (A) 優化醫院的行政管理流程
- (B) 分析病人滿意度調查結果
- <span style='color: #0066cc; font-weight: bold;'>(C) 分析大量生物醫學數據，預測分子結構，協助新藥開發</span>
- (D) 管理醫院的硬體設備維護排程

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 分析大量生物醫學數據，預測分子結構，協助新藥開發</span>  
<span style='color: #646464;'>💡 為什麼？ 利用生成式AI模擬分子結構(如AlphaFold)，能大幅加速新藥研發。</span>

---

### Q53: 將生成式AI與No Code / Low Code平台結合使用時，需要謹慎評估的考量因素是：*

- (A) 這種結合可以完全避免資料安全和隱私風險
- <span style='color: #0066cc; font-weight: bold;'>(B) 生成式AI可能產生不準確或不符預期的內容，而No Code / Low Code平台可能缺乏嚴謹的審核與驗證流程</span>
- (C) 這種結合會顯著增加應用程式的開發成本
- (D) 這種結合可以完全替代專業的AI開發團隊

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 生成式AI可能產生不準確或不符預期的內容，而No Code / Low Code平台可能缺乏嚴謹的審核與驗證流程</span>  
<span style='color: #646464;'>💡 為什麼？ 結合生成式AI與No Code/Low Code時，最需要謹慎的風險在於：AI可能產生幻覺或不正確的輸出，而視覺化開發平台往往缺乏嚴謹的單元測試與驗證機制，容易讓錯誤的AI輸出直接流入業務流程。絕非「完全避免安全風險」，安全隱患依然存在。</span>

---

### Q54: 在使用生成式AI模型時，提示詞工程（Prompt Engineering）的重要性體現在：*

- (A) 它主要用於分析模型的訓練數據
- (B) 它決定了模型部署的硬體需求
- <span style='color: #0066cc; font-weight: bold;'>(C) 它影響模型生成回應的品質、相關性和風格</span>
- (D) 它負責監控模型的運行效能

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 它影響模型生成回應的品質、相關性和風格</span>  
<span style='color: #646464;'>💡 為什麼？ 提示詞工程（Prompt Engineering）是設計高效指令以引導生成式AI產出符合預期回應的技術。精心設計的提示詞能直接決定模型回應的準確性、相關性與語言風格，與訓練數據分析、硬體需求或效能監控完全無關。</span>

---

### Q55: 企業在導入生成式AI的初期階段，應該優先考慮：*

- (A) 大規模採購最新的AI硬體設備
- <span style='color: #0066cc; font-weight: bold;'>(B) 明確自身需求與業務痛點，深入分析現有營運模式與挑戰</span>
- (C) 對所有員工進行全面的AI技術培訓
- (D) 直接將生成式AI應用於核心業務流程

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 明確自身需求與業務痛點，深入分析現有營運模式與挑戰</span>  
<span style='color: #646464;'>💡 為什麼？ 導入AI的首要步驟是「確認問題，再找解法」。企業應先釐清自身的業務痛點與需求，評估AI能否真正帶來價值，避免盲目採購昂貴設備。先買硬體後才找應用場景，是數位轉型失敗的常見原因。</span>

---

### Q56: 下列哪一項是使用生成式AI可能引發的倫理風險？*

- (A) 生成內容的成本過高
- <span style='color: #0066cc; font-weight: bold;'>(B) AI可能被濫用於製造錯誤資訊、假消息或惡意內容</span>
- (C) 模型訓練過程中消耗大量能源
- (D) AI生成的內容缺乏創意和原創性

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) AI可能被濫用於製造錯誤資訊、假消息或惡意內容</span>  
<span style='color: #646464;'>💡 為什麼？ 生成式AI被濫用於製造Deepfake或虛假資訊，是最大的倫理風險。</span>

---

### Q57: 在生成式AI的導入規劃中，概念驗證（POC）的主要目的是：*

- (A) 建立完整的AI應用系統
- <span style='color: #0066cc; font-weight: bold;'>(B) 透過小規模實驗測試，評估模型效能，檢視AI在真實業務環境中的預測準確度、效率及與現有作業模式的融合度</span>
- (C) 完成所有技術文件的編寫
- (D) 確保所有相關人員都已完成培訓

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 透過小規模實驗測試，評估模型效能，檢視AI在真實業務環境中的預測準確度、效率及與現有作業模式的融合度</span>  
<span style='color: #646464;'>💡 為什麼？ 同上，著重於模型效能與真實環境整合之評估。</span>

---

### Q58: 評估生成式AI專案的投資回報率（ROI）時，需要考慮的成本包括：*

- (A) 僅僅是購買AI軟體的費用
- (B) 主要是硬體設備的折舊費用
- <span style='color: #0066cc; font-weight: bold;'>(C) 技術開發成本、硬體與雲端服務成本、人員培訓成本以及後續的維護與升級成本</span>
- (D) 只有專案團隊的人力成本

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 技術開發成本、硬體與雲端服務成本、人員培訓成本以及後續的維護與升級成本</span>  
<span style='color: #646464;'>💡 為什麼？ 引入AI屬全面性IT專案，應納入軟硬體、人力培訓及後續維運等綜合成本。</span>

---

### Q59: 當企業將資料安全管理外包給第三方服務供應商時，這屬於哪一種風險應對策略？*

- (A) 風險緩解
- <span style='color: #0066cc; font-weight: bold;'>(B) 風險轉移</span>
- (C) 風險接受
- (D) 風險規避

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 風險轉移</span>  
<span style='color: #646464;'>💡 為什麼？ 將資料安全管理外包給第三方，是將潛在的損失責任與部分風險「轉移（Transfer）」給外部專業供應商的策略。風險緩解是整合內部措施降低威脅發生的可能性，而外包並不減少威脅本身，僅轉移了責任承擔方。</span>

---

### Q60: 為了確保生成式AI應用符合法規要求，企業應該：*

- (A) 僅關注技術的創新性
- (B) 避免使用任何個人資料進行模型訓練
- <span style='color: #0066cc; font-weight: bold;'>(C) 審查訓練數據來源，確保授權合規，並遵守資料隱私保護規範</span>
- (D) 將所有責任都歸咎於AI模型的開發者

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 審查訓練數據來源，確保授權合規，並遵守資料隱私保護規範</span>  
<span style='color: #646464;'>💡 為什麼？ 對模型來源、訓練資料確保取得授權與保護隱私，為合法應用要件。</span>

---

### Q61: No Code平台主要面向哪一類使用者？*

- (A) 具有資深程式設計經驗的開發者
- <span style='color: #0066cc; font-weight: bold;'>(B) 非技術背景的使用者</span>
- (C) 專職的AI演算法研究人員
- (D) 系統管理員

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 非技術背景的使用者</span>  
<span style='color: #646464;'>💡 為什麼？ 讓無程式開發背景的業務使用者也能輕鬆開發，推動AI民主化。</span>

---

### Q62: 生成式AI在客戶服務領域的應用包括：*

- (A) 設備的預測性維護
- <span style='color: #0066cc; font-weight: bold;'>(B) 虛擬智慧客服與自動化回應生成</span>
- (C) 生產流程的優化
- (D) 金融交易的風險評估

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 虛擬智慧客服與自動化回應生成</span>  
<span style='color: #646464;'>💡 為什麼？ 部署全天候AI智能客服可第一時間處理大量反覆且制式的查詢。</span>

---

### Q63: 在選擇 No Code / Low Code平台時，評估其系統整合能力的重要性為何？*

- <span style='color: #0066cc; font-weight: bold;'>(A) 決定平台的購買成本</span>
- (B) 確保平台與現有系統（如CRM、ERP等）的數據流通與業務流程的無縫連接
- (C) 評估使用者是否需要程式設計能力
- (D) 決定平台的市場評價

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 決定平台的購買成本</span>  
<span style='color: #646464;'>💡 為什麼？ 無程式碼/低程式碼旨在透過視覺化介面簡化開發，讓一般業務人員也能建立AI應用。</span>

---

### Q64: 提示詞（Prompt）生成式AI應用中扮演什麼角色？*

- (A) 僅用於選擇生成AI模型的類型
- (B) 主要用於評估生成內容的品質
- <span style='color: #0066cc; font-weight: bold;'>(C) 作為使用者輸入，引導模型生成特定類型的素材</span>
- (D) 決定模型訓練所需的數據量

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 作為使用者輸入，引導模型生成特定類型的素材</span>  
<span style='color: #646464;'>💡 為什麼？ Prompt工程能直接控制及引導模型輸出符合預期情境與準確度的結果。</span>

---

### Q65: 企業在導入生成式AI時，進行資源與基礎設施評估需要考量哪些方面？*

- (A) 僅考慮硬體設備的性能
- (B) 僅考慮數據的品質與數量
- <span style='color: #0066cc; font-weight: bold;'>(C) 技術人才、數據品質與基礎、硬體與系統架構</span>
- (D) 主要考慮市場的接受程度

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 技術人才、數據品質與基礎、硬體與系統架構</span>  
<span style='color: #646464;'>💡 為什麼？ 建立AI系統需要「人才、數據、基礎建置」三大關鍵面向支持。</span>

---

### Q66: AI幻覺（AI hallucinations）是生成式AI應用中常見的挑戰，指的是什麼？*

- (A) 模型生成內容的風格不一致
- (B) 模型訓練過程中出現的錯誤
- <span style='color: #0066cc; font-weight: bold;'>(C) 模型生成看似合理但實際上不正確或不存在的資訊</span>
- (D) 模型無法理解使用者的提示詞

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 模型生成看似合理但實際上不正確或不存在的資訊</span>  
<span style='color: #646464;'>💡 為什麼？ LLM常依循機率分布產出語義流暢卻沒有事實根據的內容，即AI幻覺。</span>

---

### Q67: 在生成式AI導入規劃的驗證POC（概念驗證）階段，主要目標是什麼？*

- (A) 完成所有AI模型的開發與部署
- (B) 對所有員工進行AI工具的操作培訓
- <span style='color: #0066cc; font-weight: bold;'>(C) 透過小規模測試，評估模型效能，檢視AI在真實業務環境中的預測準確度、效率及與現有作業模式的融合度</span>
- (D) 制定詳細的AI風險管理策略

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 透過小規模測試，評估模型效能，檢視AI在真實業務環境中的預測準確度、效率及與現有作業模式的融合度</span>  
<span style='color: #646464;'>💡 為什麼？ 概念驗證(POC)的核心是透過小規模實驗以確認技術與業務整合可行性。</span>

---

### Q68: 企業在實施風險緩解的生成式AI應用時，應從哪個方面著手？*

- <span style='color: #0066cc; font-weight: bold;'>(A) 將風險完全轉移給第三方</span>
- (B) 從數據管理開始，確保數據來源合法且具備高品質
- (C) 完全避免使用高風險的AI應用
- (D) 僅依賴法律規範來降低風險

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 將風險完全轉移給第三方</span>  
<span style='color: #646464;'>💡 為什麼？ 本題可從AI基本概念或上下文推斷最佳選項。</span>

---

### Q69: 下列哪一項不是生成式AI工具在使用體驗方面的優化方向？*

- (A) 提供更直觀的操作設計
- (B) 支援自然語言指令
- (C) 提供智慧化的參數調整建議
- <span style='color: #0066cc; font-weight: bold;'>(D) 強制限制使用者自訂生成內容</span>

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(D) 強制限制使用者自訂生成內容</span>  
<span style='color: #646464;'>💡 為什麼？ 限制不是優化手段，良好的界面應該幫助使用者更容易達成創意發想。</span>

---

### Q70: 企業導入生成式AI後，建立持續改進機制的重要性為何？*

- (A) 僅為了降低AI模型的運行成本
- (B) 僅為了收集用戶的回饋意見
- <span style='color: #0066cc; font-weight: bold;'>(C) 結合用戶意見與運行數據，對AI方案進行持續優化，確保系統始終適應動態環境並保持高效運作</span>
- (D) 主要目的是為了提高員工對AI技術的熟練度

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 結合用戶意見與運行數據，對AI方案進行持續優化，確保系統始終適應動態環境並保持高效運作</span>  
<span style='color: #646464;'>💡 為什麼？ AI上線後仍需因應數據漂移或使用反饋，隨時進行監控與動態升級。</span>

---

### Q71: No Code / Low Code平台的發展被視為推動AI民主化的重要力量，其主要原因是？*

- <span style='color: #0066cc; font-weight: bold;'>(A) 提升了AI模型的準確性</span>
- (B) 簡化了開發流程，使更多非技術背景人員能夠參與AI的創建與部署
- (C) 降低了AI技術的硬體需求
- (D) 加速了AI演算法的研究速度

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 提升了AI模型的準確性</span>  
<span style='color: #646464;'>💡 為什麼？ 無程式碼/低程式碼旨在透過視覺化介面簡化開發，讓一般業務人員也能建立AI應用。</span>

---

### Q72: 選擇No Code / Low Code平台時需要考量的關鍵因素。請問在評估平台的目標用戶與技術需求時，No Code平台主要面向哪類使用者？*

- <span style='color: #0066cc; font-weight: bold;'>(A) 具有資深程式設計經驗的開發者</span>
- (B) 非技術使用者
- (C) 專職的AI演算法研究人員
- (D) 系統管理員

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 具有資深程式設計經驗的開發者</span>  
<span style='color: #646464;'>💡 為什麼？ 無程式碼/低程式碼旨在透過視覺化介面簡化開發，讓一般業務人員也能建立AI應用。</span>

---

### Q73: 生成式AI在教育領域的應用潛力包括？*

- (A) 自動化金融交易
- <span style='color: #0066cc; font-weight: bold;'>(B) 自動化教材生成與個人化學習路徑設計</span>
- (C) 生產線的品質控制
- (D) 交通流量的預測

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 自動化教材生成與個人化學習路徑設計</span>  
<span style='color: #646464;'>💡 為什麼？ AI在教育中能進行適性化調整與客製化教材，實踐因材施教。</span>

---

### Q74: 生成式AI的核心特徵是？*

- (A) 分析和辨識現有數據
- <span style='color: #0066cc; font-weight: bold;'>(B) 透過模型的學習能力生成新內容</span>
- (C) 優化現有的演算法效率
- (D) 提升資料儲存的安全性

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 透過模型的學習能力生成新內容</span>  
<span style='color: #646464;'>💡 為什麼？ 「生成」，就是從無到有地利用既有知識庫推導和產出新的內容與樣式。</span>

---

### Q75: 提示詞（Prompt）在生成式AI中的作用。請問提示詞的主要功能是？*

- (A) 用於評估生成內容的品質
- <span style='color: #0066cc; font-weight: bold;'>(B) 作為使用者輸入，引導模型生成特定類型的素材</span>
- (C) 決定模型訓練所需的數據量
- (D) 調整模型的超參數

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 作為使用者輸入，引導模型生成特定類型的素材</span>  
<span style='color: #646464;'>💡 為什麼？ Prompt工程能直接控制及引導模型輸出符合預期情境與準確度的結果。</span>

---

### Q76: 企業在導入生成式AI時，首先需要進行？*

- <span style='color: #0066cc; font-weight: bold;'>(A) 確保硬體設備升級</span>
- (B) 明確自身需求與業務痛點
- (C) 安排員工進行AI相關培訓
- (D) 購買生成式AI相關軟體

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 確保硬體設備升級</span>  
<span style='color: #646464;'>💡 為什麼？ 本題可從AI基本概念或上下文推斷最佳選項。</span>

---

### Q77: 下列何者是使用生成式 AI 進行圖像生成時需要考慮的問題？  *

- (A) 生成圖像的解析度
- (B) 版權和合法性
- (C) 模型的推論時間
- <span style='color: #0066cc; font-weight: bold;'>(D) 以上皆是</span>

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(D) 以上皆是</span>  
<span style='color: #646464;'>💡 為什麼？ 圖像生成必須考量計算資源(推論時間)、生成的解析度，更首重是否有侵權。</span>

---

### Q78: 資料隱私與安全是生成式AI應用中需要重視的風險。以下哪種措施有助於確保資料隱私？*

- <span style='color: #0066cc; font-weight: bold;'>(A) 使用更強大的硬體設備</span>
- (B) 透過數據加密、匿名化和權限管理保護敏感資訊
- (C) 增加生成內容的多樣性
- (D) 提升模型的生成速度

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 使用更強大的硬體設備</span>  
<span style='color: #646464;'>💡 為什麼？ 本題可從AI基本概念或上下文推斷最佳選項。</span>

---

### Q79: 大型語言模型（LLM）的發展趨勢，例如GPT系列。請問LLM能力提升的主要方向包括？*

- <span style='color: #0066cc; font-weight: bold;'>(A) 降低對大量數據的依賴</span>
- (B) 擴展參數規模和計算能力，提高語言生成的連貫性與語義深度
- (C) 減少模型的複雜度以提升運行速度
- (D) 完全取代傳統的自然語言處理方法

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 降低對大量數據的依賴</span>  
<span style='color: #646464;'>💡 為什麼？ 本題可從AI基本概念或上下文推斷最佳選項。</span>

---

### Q80: 風險緩解在生成式AI風險管理中扮演重要角色。請問以下哪個行動屬於風險緩解的範疇？*

- (A) 暫緩開發高風險應用
- (B) 購買保險將風險責任轉移給第三方
- <span style='color: #0066cc; font-weight: bold;'>(C) 從數據管理開始，確保數據來源合法且具備高品質，並對生成內容進行審查與發布</span>
- (D) 評估風險容忍度並接受

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 從數據管理開始，確保數據來源合法且具備高品質，並對生成內容進行審查與發布</span>  
<span style='color: #646464;'>💡 為什麼？ 從源頭確保數據的高品質與合法性，是主動遏止AI犯錯的重要管理措施。</span>

---

### Q81: No Code平台主要面向哪類使用者？*

- (A) 具有資深程式設計經驗的開發者
- <span style='color: #0066cc; font-weight: bold;'>(B) 非技術使用者</span>
- (C) 專職的AI演算法研究人員
- (D) 系統管理員

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 非技術使用者</span>  
<span style='color: #646464;'>💡 為什麼？ 讓無程式開發背景的業務使用者也能輕鬆開發，推動AI民主化。</span>

---

### Q82: No Code / Low Code平台在企業數位轉型中的優勢，包括降低成本、縮短上市時間和加速數位轉型。請問以下哪個選項最能體現「加速數位轉型」的優勢？*

- <span style='color: #0066cc; font-weight: bold;'>(A) 減少開發過程中的人力投入</span>
- (B) 促進IT與業務部門的協作，快速開發業務應用
- (C) 使企業能夠更快地將產品推向市場
- (D) 降低企業在軟體開發上的總體支出

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 減少開發過程中的人力投入</span>  
<span style='color: #646464;'>💡 為什麼？ 無程式碼/低程式碼旨在透過視覺化介面簡化開發，讓一般業務人員也能建立AI應用。</span>

---

### Q83: 學校教師如何引導學生正確使用生成式 AI 工具？  *

- (A) 不應使用 AI 工具於教學場域
- (B) 無限制地使用 AI 工具
- <span style='color: #0066cc; font-weight: bold;'>(C) 訂立清晰的使用規範並進行說明</span>
- (D) 僅鼓勵學生利用 AI 完成課堂作業

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 訂立清晰的使用規範並進行說明</span>  
<span style='color: #646464;'>💡 為什麼？ 直接明訂規則能幫助學生合規並善用AI輔助思考，而非單純禁用。</span>

---

### Q84: 下列哪一種方式可以有效幫助現職員工提升 AI 應用能力？  *

- (A) 提高薪資來吸引 AI 人才
- <span style='color: #0066cc; font-weight: bold;'>(B) 安排跨部門交流和測試專案</span>
- (C) 減少員工的工作負擔
- (D) 員工視需求選擇性自學 AI 技術

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 安排跨部門交流和測試專案</span>  
<span style='color: #646464;'>💡 為什麼？ 透過專案實作和跨部門碰撞交流，能最有效的擴大員工應用的想像空間與實戰經驗。</span>

---

### Q85: 下列何者為企業導入 AI 技術後最直接的影響？  *

- (A) 增加人力需求
- <span style='color: #0066cc; font-weight: bold;'>(B) 提升生產力和效率</span>
- (C) 減少數據處理能力
- (D) 降低市場競爭力

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 提升生產力和效率</span>  
<span style='color: #646464;'>💡 為什麼？ 處理大量常規任務能直接減少繁瑣人力，釋放效能。</span>

---

### Q86: 下列何者是人工智慧未來發展中最迫切需要解決的挑戰？  *

- (A) 計算資源的過剩
- <span style='color: #0066cc; font-weight: bold;'>(B) 資料隱私與道德規範問題</span>
- (C) 人才培育與跨領域合作的不足
- (D) 無法應用於小型企業場景

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 資料隱私與道德規範問題</span>  
<span style='color: #646464;'>💡 為什麼？ AI工具的發展速度遠超過法規建立速度，導致隱私、偏見及道德問題層出不窮。</span>

---

### Q87: 在生成式 AI 導入過程中，資料安全與隱私保護的哪一方面是最重要的考量？  *

- <span style='color: #0066cc; font-weight: bold;'>(A) 權限控管與合規要求</span>
- (B) 增強客服回饋（反饋）能力
- (C) 資料視覺化能力
- (D) 設定目標優先級

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 權限控管與合規要求</span>  
<span style='color: #646464;'>💡 為什麼？ 制定嚴格的權限查核與合規架構，是資料防護的一把鎖。</span>

---

### Q88: 成功導入生成式 AI 的關鍵在於哪三個因素？  *

- (A) 提供更多數據、加強合作、減少成本
- <span style='color: #0066cc; font-weight: bold;'>(B) 清晰定義痛點、技術匹配、培養人才</span>
- (C) 投資高端設備、增加技術人員、縮短流程
- (D) 推行技術改革、調整市場策略、強化品牌

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 清晰定義痛點、技術匹配、培養人才</span>  
<span style='color: #646464;'>💡 為什麼？ 尋找合適的問題、合適的技術人員、以及最配對的解決方案。</span>

---

### Q89: 在 AI 導入正式實施階段，企業應優先進行的活動是什麼？  *

- (A) 增加行銷預算
- (B) 調整產品價格
- <span style='color: #0066cc; font-weight: bold;'>(C) 確保相關人員熟悉新流程與工具</span>
- (D) 減少生產規模以減少風險

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 確保相關人員熟悉新流程與工具</span>  
<span style='color: #646464;'>💡 為什麼？ AI軟體的最終使用者是員工，完善的培訓使用能真正落實投資帶來的便利。</span>

---

### Q90: 下列何者為風險分析階段的主要目的？  *

- (A) 找到更多的數據來源
- (B) 增強模型的效能
- <span style='color: #0066cc; font-weight: bold;'>(C) 評估風險的影響與發生可能性</span>
- (D) 降低模型運行成本

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 評估風險的影響與發生可能性</span>  
<span style='color: #646464;'>💡 為什麼？ 衡量風險最重要的維度在於該事件「發生的機率」和「實際引發的損傷大小」。</span>

---

### Q91: 關於對抗式測試（Adversarial Testing），下列何者為正確？*

- (A) 是指模型在監督式學習中，使用多輪交叉驗證以強化準確率的測試手法
- (B) 是在模型訓練階段加入大量標記資料以防止過擬合的技術
- <span style='color: #0066cc; font-weight: bold;'>(C) 是一種測試方法，透過設計刻意擾亂輸入資料來檢驗模型的穩定性</span>
- (D) 主要用於資料前處理階段，過濾掉不一致或錯誤的樣本

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 是一種測試方法，透過設計刻意擾亂輸入資料來檢驗模型的穩定性</span>  
<span style='color: #646464;'>💡 為什麼？ 透過插入對抗樣本等惡意輸入，測試模型在遭逢干擾時是不會發生誤判的測試技術。</span>

---

### Q92: 在部署AI系統或模型服務時，進行「延遲測試」（Latency Testing）的主要目的是什麼？  *

- (A) 檢查模型是否能正確處理對抗性輸入
- (B) 測量模型預測結果的正確率是否達到預期標準
- <span style='color: #0066cc; font-weight: bold;'>(C) 評估模型輸入到輸出所需的時間，以確保系統回應效能</span>
- (D) 驗證訓練資料是否已經被正確標準化與正規化

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 評估模型輸入到輸出所需的時間，以確保系統回應效能</span>  
<span style='color: #646464;'>💡 為什麼？ Latency測試旨在衡量系統收到指令到回覆產出所經過的時間，驗證用戶體驗。</span>

---

### Q93: 關於大型語言模型的「微調」（Fine-tuning）技術，下列哪一項敘述正確？  *

- (A) 微調是指將整個模型從零開始重新訓練，以提升其泛化能力
- (B) 微調主要用於壓縮模型體積，使其能部署在低記憶體裝置上
- <span style='color: #0066cc; font-weight: bold;'>(C) 微調是將已訓練模型針對特定任務或資料再訓練，以提升其在特定領域的表現</span>
- (D) 微調過程中禁止修改任何模型權重，以確保模型穩定性

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 微調是將已訓練模型針對特定任務或資料再訓練，以提升其在特定領域的表現</span>  
<span style='color: #646464;'>💡 為什麼？ 預訓練學習通用知識，微調(Fine-tuning)則是為了適應下游特定任務或領域。</span>

---

### Q94: 生成式AI的核心特徵是透過模型的學習能力生成新內容。請問生成式AI常用的技術架構不包括以下哪種？*

- <span style='color: #0066cc; font-weight: bold;'>(A) 生成對抗網路（GAN）</span>
- (B) 變分自編碼器（VAE）
- (C) 基於變換器（Transformer）架構的模型
- (D) 支援向量機（SVM）

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) 生成對抗網路（GAN）</span>  
<span style='color: #646464;'>💡 為什麼？ 「生成」，就是從無到有地利用既有知識庫推導和產出新的內容與樣式。</span>

---

### Q95: 在使用生成式AI工具時，調整「溫度（Temperature）」參數會影響生成內容的哪個方面？*

- (A) 生成速度
- <span style='color: #0066cc; font-weight: bold;'>(B) 創意性與隨機性</span>
- (C) 準確性與事實性
- (D) 計算資源消耗

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(B) 創意性與隨機性</span>  
<span style='color: #646464;'>💡 為什麼？ Temperature值越高，產出的內容越隨機、具創意；越低則越保守、確定性高。</span>

---

### Q96: 企業在導入生成式AI的初始階段，最重要的是進行？*

- (A) 技術團隊的擴充與培訓
- (B) 硬體設備與雲端服務的升級
- <span style='color: #0066cc; font-weight: bold;'>(C) 明確自身需求與業務痛點</span>
- (D) 大規模的資料收集與清洗

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 明確自身需求與業務痛點</span>  
<span style='color: #646464;'>💡 為什麼？ 企業導入 AI 前，必須先經歷「定錨」階段。如果不知道要解決什麼痛點（如降低客服成本、加速審查流程），盲目擴編團隊或採買硬體只會浪費資源，釐清需求永遠是第一步。</span>

---

### Q97: 下列關於 RAG（檢索增強生成） 的敘述何者正確？*

- <span style='color: #0066cc; font-weight: bold;'>(A) RAG 技術主要依賴對大型語言模型進行完全的重新訓練</span>
- (B) RAG 技術能完全避免 AI 產生錯誤或虛構的內容
- (C) RAG 技術結合搜尋引擎和生成式 AI，先檢索相關文件再生成回答，有助於提高回答的準確性並提供資料來源
- (D) RAG 技術的優點是不受資料庫品質和檢索精準度的影響

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(A) RAG 技術主要依賴對大型語言模型進行完全的重新訓練</span>  
<span style='color: #646464;'>💡 為什麼？ 檢索增強生成能讓LLM以外部搜尋來的知識庫做為回答基礎以減少回答的虛構造假。</span>

---

### Q98: AI 幻覺（AI Hallucination） 的主要原因是？*

- (A) AI 模型具備真正理解和查證資訊的能力，但偶爾會故意提供錯誤答案
- (B) AI 模型總是能記住所有過往的對話紀錄，並提供連貫的回覆
- <span style='color: #0066cc; font-weight: bold;'>(C) 多數文字生成模型僅預測下一個字（詞語），並未真正理解與查證，可能生成看似合理但實際上錯誤的內容</span>
- (D) AI 模型在進行數字運算時，總是能以全運算方式進行，因此不會產生錯誤

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 多數文字生成模型僅預測下一個字（詞語），並未真正理解與查證，可能生成看似合理但實際上錯誤的內容</span>  
<span style='color: #646464;'>💡 為什麼？ LLM常依循機率分布產出語義流暢卻沒有事實根據的內容，即AI幻覺。</span>

---

### Q99: 下列何者屬於 AI 倫理 的重要考量？*

- (A) AI 模型的訓練數據量越大越好，不需要考慮數據的多樣性
- (B) 在追求 AI 系統效能提升時，可以忽略對環境造成的碳排放
- <span style='color: #0066cc; font-weight: bold;'>(C) 確保 AI 系統的決策過程儘可能避免偏見，對不同群體保持公平</span>
- (D) AI 系統的輸出內容是否違反法規或涉及著作權與 AI 倫理無關

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 確保 AI 系統的決策過程儘可能避免偏見，對不同群體保持公平</span>  
<span style='color: #646464;'>💡 為什麼？ AI 倫理的核心價值在於確保科技發展不損害人類福祉，其中「公平與無偏見 (Fairness and Non-discrimination)」是最關鍵的考量之一，以確保系統設計不會歧視或邊緣化任何特定族群。</span>

---

### Q100: 金融機構在使用 生成式 AI 時應特別注意？*

- (A) 可以完全信任生成式 AI 產出的所有資訊，並直接應用於業務決策
- (B) 使用第三方業者開發的生成式 AI 時，由於技術由專業機構提供，無需再進行額外風險管控
- <span style='color: #0066cc; font-weight: bold;'>(C) 生成式 AI 產出的資訊仍需由金融機構人員就其風險進行客觀且專業的管控，以避免對客戶或金融消費者產生不公平之情況</span>
- (D) 金融機構在使用 AI 系統時，應優先考慮降低成本，公平性並非主要考量

<span style='color: #008000; font-weight: bold;'>✅ 正確解答：(C) 生成式 AI 產出的資訊仍需由金融機構人員就其風險進行客觀且專業的管控，以避免對客戶或金融消費者產生不公平之情況</span>  
<span style='color: #646464;'>💡 為什麼？ 受到高度監管的金融業使用 AI 應採「Human in the loop (人機協同)」，不能盲目信任或直接交由 AI 決策，必須有人為介入來審查其客觀性與公平性以落實風險管控。</span>

---
