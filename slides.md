## 我不想寫 code 了
## AI Agent in n8n

2025-05-25

Ben

---



<!-- .slide: data-background-iframe="media/Ben.html" -->

---

## Outline

- 老闆的問題
- AI Agent in n8n
- MCP in n8n
- 打造我的 AI 團隊



---



<!-- .slide: data-auto-animate -->

# 老闆的問題
- <font color='#646464'>AI Agent in n8n</font>
- <font color='#646464'>MCP in n8n</font>
- <font color='#646464'>打造我的 AI 團隊</font>


----

有一天，老闆問：『如何提速3倍』

----

提速三倍？那不就代表我可能會有三倍工作量？

----

壓力超大....不想寫 Code....

----

已經有三個人跟我說，都已經老大不小了，寫啥 Code.....

----

![n8n_ai_agent](media/n8n_ai_agent.png)


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



---

<!-- .slide: data-auto-animate -->

- <font color='#646464'> 老闆的問題</font>
# AI Agent in n8n
- <font color='#646464'>MCP in n8n</font>
- <font color='#646464'>打造我的 AI 團隊</font>


----

## Agentic Workflow
### 讓 Agent 自己找工具
![ai_agent_flow](media/ai_agent_flow.png)


----

## `playwright`

* Microsoft 出品的跨瀏覽器自動化測試框架，支援 Chromium、Firefox 與 WebKit。
* 多語言 API 與 MCP。
* 內建並行測試、網路攔截、截圖與錄影等功能，適用於端到端測試與爬蟲。


----

### 範例：我需要取得球賽賽況資訊

[Italy Serie A- NAP vs CAG](https://www.espn.com/soccer/commentary/_/gameId/712488
)

----

### AI Agent 直連 Playwright MCP

![n8n_crawler_playwright](media/n8n_crawler_playwright.png)


----

### AI Agent 直連 Playwright MCP


```json
[
  {
    "Time": "42'",
    "Commentary": "Goal - Volley Goal! Napoli 1, Cagliari 0. Scott McTominay (Napoli) right footed shot from the centre of the box to the centre of the goal. Assisted by Matteo Politano with a cross."
  },
  {
    "Time": "51'",
    "Commentary": "Goal! Napoli 2, Cagliari 0. Romelu Lukaku (Napoli) left footed shot from the centre of the box to the bottom right corner. Assisted by Amir Rrahmani."
  },
  {
    "Time": "52'",
    "Commentary": "Yellow Card - Romelu Lukaku (Napoli) is shown the yellow card for excessive celebration."
  },
  {
    "Time": "FT",
    "Commentary": "Match ends, Napoli 2, Cagliari 0."
  }
]

```


----


## Agentic Workflow- 幫他找工具

![ai_agen_tool_flow](media/ai_agen_tool_flow.png)

把不需要 LLM 的步驟先做完

----

### API Server + n8n


![n8n_playwright_api_server](media/n8n_playwright_api_server.png)



----

## AI Agentic 影分身之術

![n8n_crawler_playwright_multi](media/n8n_crawler_playwright_multi.png)

----

## Agentic RAG


<font size=1>from: https://weaviate.io/blog/what-are-agentic-workflows</font>
![agentic-search-workflow](media/agentic-search-workflow.jpg)



----

## Agentic RAG

![agentic-rag](media/agentic-rag.png)


----

### Agentic RAG in `n8n`

![n8n_ai_agent_rag](media/n8n_ai_agent_rag.png)

----

### RAG

![RAG](media/RAG.png)


----

### Agentic RAG

![Agentic_RAG](media/Agentic_RAG.png)


---



<!-- .slide: data-auto-animate -->

- <font color='#646464'> 老闆的問題</font>
- <font color='#646464'> AI Agent in n8n</font>
# MCP in n8n
- <font color='#646464'>打造我的 AI 團隊</font>


----

## MCP in n8n


- MCP Client
    - SSE
    - STDIO (community)
- MCP Server
    - SSE


----

### Model Context Protocol 

<font size=1>from: https://ikala.ai/zh-tw/blog/ikala-ai-insight/what-is-model-context-protocol-mcp/</font>
![](media/mcp_usb.png)


----

### MCP host & client in n8n

![n8n_crawler_playwright](media/n8n_crawler_playwright.png)

----

### MCP Client- SSE
Server-Sent Events
![mcp_client_sse](media/mcp_client_sse.png)



----

### MCP Client- STDIO
Standard I/O
![community_node](media/community_node.png)




----


![mcp_server_sse](media/mcp_server_sse.png)


----

![playwright_workflow](media/playwright_workflow.png)


----

### `claude_desktop_config.json`

```json
{
  "mcpServers": {

    "n8n-playwright":{
          "command": "npx",
          "args": [
            "-y",
            "supergateway",
            "--sse",
            "http://xxx.xxx.xx/mcp/playwright_n8n/sse"
      ]
    }
  }
}
```

----

### MCP from `n8n` in Claude

![claude_mcp](media/claude_mcp.png)


----

### 目前`n8n`使用心得

- 少寫不少 code
- 找不到適合的 Node
    - 稍微寫一點 code
    - 直接使用 HTTP Request Node


---

<!-- .slide: data-auto-animate -->

- <font color='#646464'> 老闆的問題</font>
- <font color='#646464'> AI Agent in n8n </font>
- <font color='#646464'>MCP in n8n</font>
# 打造我的 AI 團隊


----

## AI 新成員

- 已經報到
    - 秘書：回信
    - 寫手：寫報告
    - 行銷助理：整理新聞素材
    - 造型師：設計符合主題的造型
- 即將報到
    - 資料工程師：提供資料給營運團隊
    - MIS 櫃檯：回答日常電腦相關的蠢問題

----

### 秘書

![email](media/email.png)

----

### 寫手


![](media/writer.png)

----

### 行銷助理
![marketing_assistant](media/marketing_assistant.png)



----

### 造型師

<!-- .slide: data-background="media/stylist.png" -->

----

![](media/QR_slides.png)

----

## `Facebook`


<img src=media/QR_R_Ladies_Taipei.png width=50%></img><img src=media/QR_Ben_facebook.png width=50%></img>


----

<!-- .slide: data-background-iframe="https://www.accupass.com/go/ai_image_rladies" -->


----


<!-- .slide: data-background-iframe="https://www.accupass.com/go/openfun_rladies" -->

----

# Thank you