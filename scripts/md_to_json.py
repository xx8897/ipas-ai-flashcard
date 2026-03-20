import os
import re
import json
import sys

# 標準化路徑
BASE_DIR = r'c:\雲端\ipas AI應用證照\題庫\flashcard-app\src\assets\question-sources'
OUT_PATH = r'c:\雲端\ipas AI應用證照\題庫\flashcard-app\src\data\questions.json'

SOURCES = [
    {'file': '學習指引_科目1人工智慧基礎概論_題庫解析.md', 'source': '學習指引', 'subject': '科目1：人工智慧基礎概論'},
    {'file': '學習指引_科目2生成式AI應用與規劃_題庫解析.md', 'source': '學習指引', 'subject': '科目2：生成式AI應用與規劃'},
    {'file': '114年第四梯次_科目1人工智慧基礎概論_考古題解析.md', 'source': '114年第四梯次考古題', 'subject': '科目1：人工智慧基礎概論'},
    {'file': '114年第四梯次_科目2生成式AI應用與規劃_考古題解析.md', 'source': '114年第四梯次考古題', 'subject': '科目2：生成式AI應用與規劃'},
    {'file': '114年4月版考試樣題_題庫解析.md', 'source': '114年4月版樣題', 'subject': '混合（科目1＋科目2）'},
    {'file': '114年9月版考試樣題_題庫解析.md', 'source': '114年9月版樣題', 'subject': '混合（科目1＋科目2）'},
    {'file': 'AI應用初級題庫_解答與解析.md', 'source': 'AI應用初級題庫', 'subject': '綜合題庫'},
]

def clean_html(text):
    return re.sub(r'<[^>]*>', '', text).strip()

def parse_file(fpath, meta, uid, all_questions):
    if not os.path.exists(fpath):
        print(f"Skipping missing file: {fpath}")
        return

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 以 ### Q 分割題目
    blocks = re.split(r'\n### Q(\d+)[:：]*', content)
    # 第一個 block 通常是標題或前言，跳過
    for i in range(1, len(blocks), 2):
        q_num = blocks[i]
        q_body = blocks[i+1]
        
        # 分離題目文字與後續內容
        lines = [l.strip() for l in q_body.split('\n') if l.strip()]
        if not lines: continue
        
        q_text = ""
        options = {'A': '', 'B': '', 'C': '', 'D': ''}
        answer = "A"
        explanation = ""
        
        # 狀態機解析 body
        found_options = False
        for line in lines:
            # 抓取選項: 支援 (A), （A）, -(A), 以及帶標籤的
            m_opt = re.search(r'[（(]([A-D])[）)][ .](.+)', line)
            if m_opt:
                label = m_opt.group(1)
                val = clean_html(m_opt.group(2))
                options[label] = val
                found_options = True
                continue
            
            # 抓取正確答案
            if "正確解答" in line or "✅" in line:
                m_ans = re.search(r'[（(]([A-D])[）)]', line)
                if m_ans:
                    answer = m_ans.group(1)
                continue
            
            # 抓取解析
            if "💡" in line or "為什麼" in line or "WHY" in line:
                explanation = re.sub(r'.*?(?:💡|為什麼|WHY)[?？\s]*', '', line)
                explanation = clean_html(explanation)
                continue
            
            # 累積題目文字 (在看到選項之前)
            if not found_options and not line.startswith('---'):
                q_text += " " + line
            # 累積解析文字 (在看到解答標記之後)
            elif explanation and not line.startswith('---'):
                explanation += " " + line

        # 最終檢查與補全
        q_text = q_text.strip() or f"(題目內容載入失敗 - Q{q_num})"
        explanation = explanation.strip() or "（本題尚無詳細解析）"
        
        all_questions.append({
            'id': uid[0],
            'source': meta['source'],
            'subject': meta['subject'],
            'text': q_text,
            'options': options,
            'answer': answer,
            'explanation': explanation
        })
        uid[0] += 1

all_questions = []
uid = [1]
for meta in SOURCES:
    fpath = os.path.join(BASE_DIR, meta['file'])
    parse_file(fpath, meta, uid, all_questions)

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully processed {len(all_questions)} questions.")
