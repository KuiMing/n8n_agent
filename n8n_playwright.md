## 自動化工作流程下的 LLM 
## 驅動無程式碼網頁爬蟲與EDA


2025-06-19

陳奎銘 Ben @南區統計年會

---

無程式碼？

----

我只能說盡量不寫程式

----

<!-- .slide: data-background-iframe="media/Ben.html" -->



---

- # `playwright`
- # AI Agent
- # n8n





----


## `playwright`

* Microsoft 出品的跨瀏覽器自動化測試框架，支援 Chromium、Firefox 與 WebKit。
* 多語言 API 與 MCP。
* 內建並行測試、網路攔截、截圖與錄影等功能，適用於端到端測試與爬蟲。

----

## Install `playwright`

```
pip install playwright
playwright install --with-deps
```

----

## `playwright` Demo

```
playwright codegen --target python \
--output download_script.py \
https://data.moenv.gov.tw/dataset/detail/AQX_P_432

```

<iframe width="560" height="315" src="https://www.youtube.com/embed/P4ytwrt8HiM?si=yqyb5m4YwKxj0uaq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

## generate code by `playwright`

產出可以直接下載資料的程式碼
```python[7-10|5, 12]
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("https://data.moenv.gov.tw/dataset/detail/AQX_P_432")
    page.get_by_role("button", name="下載篩選後資料").click()
    with page.expect_download() as download_info:
        page.get_by_label("下載篩選後資料").get_by_text("CSV").click()
    download = download_info.value
    download.save_as("AQX_P_432.csv")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
```



----

## 關鍵是取得網頁內容

```python
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto(url, timeout=self.timeout, wait_until="networkidle")
content = page.content()
```

----

## 架設 API Service

- 用現成的，不用自己寫 code
    - docker.io/kuiming/playwright-api
    - https://github.com/KuiMing/n8n_agent

----

## AI Agent



能感知環境、規劃動作與利用記憶進行推理，並透過工具或 API 呼叫執行任務以達成預定目標的系統


----

## AI Agent

![ai_agent](media/ai_agent.png)

----

## `n8n`

### API 懶人包 + 樂高
#### 自動化工作流程工具

----


## WHY `n8n`
- **開源且免費**：可自架設於本地或雲端，無需擔心資料隱私。
- **高度彈性**：支援自訂節點與腳本，滿足各種自動化需求，可設置多種觸發器。
- **資源豐富**：擁有龐大開發者社群、豐富範例與插件，官方快速迭代回應新需求，對比封閉商業平台更易獲得資源與技術支援。

----

## `n8n` Nodes

![ai_agent](media/n8n_nodes.png)


----

## `n8n` Credential- 地端


![](media/credential_local.png)

----

## `n8n` Credential- 雲端

![](media/credential_cloud.png)




----

### 範例：我需要取得球賽資訊

[FIFA Club World Cup](https://www.fifa.com/)


----

<!-- .slide: data-background="media/n8n-playwright-1.png" -->

----

<!-- .slide: data-background="media/n8n-playwright-2.png" -->

----

<!-- .slide: data-background="media/n8n-playwright-3.png" -->

----

<!-- .slide: data-background="media/n8n-playwright-4.png" -->

----

<!-- .slide: data-background="media/n8n-playwright-5.png" -->

----

<!-- .slide: data-background="media/n8n-playwright-6.png" -->

----
<!-- .slide: data-background="media/n8n-playwright-7.png" -->

----
<!-- .slide: data-background="media/n8n-playwright-8.png" -->

----

<!-- .slide: data-background="media/n8n-playwright-9.png" -->

----

<!-- .slide: data-background="media/n8n-playwright-schedule.png" -->


----

## Take away

- 若有爬蟲需求，請嘗試使用 `playwright`
- 請用 AI Agent 減少自己需要動手的雜事
- 請用 n8n 讓雜事自動化



---

#### https://github.com/KuiMing/n8n_agent


----

## `Facebook`


<img src=media/QR_R_Ladies_Taipei.png width=50%></img><img src=media/QR_Ben_facebook.png width=50%></img>


----

<!-- .slide: data-background-iframe="https://www.accupass.com/go/openfun_rladies" -->

----

# Thank you