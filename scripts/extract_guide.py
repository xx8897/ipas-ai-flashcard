import os
import re

out_dir = r'c:\雲端\ipas AI應用證照\題庫\答案與解析'
os.makedirs(out_dir, exist_ok=True)

files = [
    (r'c:\雲端\ipas AI應用證照\題庫\sub1.txt', '學習指引_科目1人工智慧基礎概論_題庫解析.md', 'AI應用規劃師(初級)-科目1人工智慧基礎概論 題庫解析', 1),
    (r'c:\雲端\ipas AI應用證照\題庫\sub2.txt', '學習指引_科目2生成式AI應用與規劃_題庫解析.md', 'AI應用規劃師(初級)-科目2生成式AI應用與規劃 題庫解析', 2)
]

for txt_file, out_name, title, subject in files:
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    q_pattern = re.compile(r'^(\d+)\.\s+(.*)')
    opt_pattern = re.compile(r'^[（\(]([A-D])[）\)]\s*(.*)')
    ans_pattern = re.compile(r'^(\d+)\.\s*Ans[（\(]([A-D])[）\)]')
    
    q_list = []
    
    # PASS 1: Extract Questions
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        m_q = q_pattern.match(line)
        m_ans = ans_pattern.match(line)
        
        if m_q and int(m_q.group(1)) > 0 and int(m_q.group(1)) <= 100:
            if m_ans:
                pass
            else:
                q_num = int(m_q.group(1))
                q_text = m_q.group(2)
                opts = {}
                i += 1
                while i < len(lines):
                    l2 = lines[i].strip()
                    if ans_pattern.match(l2) or q_pattern.match(l2):
                        i -= 1
                        break
                    
                    m_opt = opt_pattern.match(l2)
                    if m_opt:
                        opts[m_opt.group(1)] = m_opt.group(2)
                    elif l2 and not m_opt:
                        # Ignore footer
                        if l2.startswith('') or re.match(r'^\d+-\d+$', l2):
                            pass
                        else:
                            if not opts:
                                q_text += " " + l2
                            else:
                                last_k = list(opts.keys())[-1]
                                opts[last_k] += " " + l2
                    i += 1
                
                if len(opts) >= 4:
                    # Keep track of absolute question index based on parsed order
                    q_list.append({
                        'q_idx': len(q_list) + 1,
                        'num': q_num,
                        'text': q_text.strip(),
                        'options': opts,
                        'ans': '',
                        'exp': ''
                    })
        i += 1
        
    # PASS 2: Extract Answers
    ans_list = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        m_ans = ans_pattern.match(line)
        if m_ans:
            q_num = int(m_ans.group(1))
            ans_char = m_ans.group(2)
            exp_text = ""
            empty_count = 0
            i += 1
            while i < len(lines):
                l2_raw = lines[i]
                l2 = l2_raw.strip()
                if ans_pattern.match(l2) or q_pattern.match(l2) or re.match(r'^\d+\.\d+\s+', l2):
                    i -= 1
                    break
                else:
                    if l2.startswith('解析：') or l2.startswith('解析:'):
                        exp_text += l2.replace('解析：', '').replace('解析:', '').strip()
                        empty_count = 0
                    elif l2:
                        if not l2.startswith('') and not re.match(r'^\d+-\d+$', l2):
                            exp_text += " " + l2
                            empty_count = 0
                    else:
                        empty_count += 1
                        if empty_count >= 2:
                            break
                i += 1
            ans_list.append({'ans': ans_char, 'exp': exp_text.strip()})
        i += 1

    # Merge Q and A securely
    for idx, q in enumerate(q_list):
        if idx < len(ans_list):
            q['ans'] = ans_list[idx]['ans']
            q['exp'] = ans_list[idx]['exp']

    # Apply Errata for Subject 1
    if subject == 1:
        for q in q_list:
            if q['q_idx'] == 13:
                q['ans'] = 'A'
                q['options']['A'] = '原理相對其他集群法較為複雜'
                q['exp'] = 'K-means 的原理相對簡單，主要透過反覆分配點到最近中心、並更新中心點來最小化平方誤差和，並非複雜方法。K-means 常與 PCA（降維）、Elbow method（選 k 值）等方法結合，具有一定彈性。對於球形且大小密度接近的群體，K-means 表現良好。'
            elif q['q_idx'] == 17:
                q['text'] = '當我們進行一次假設檢定，得到的 p 值為 0.03，而我們事先設定的顯著性水準為 0.05。以下哪一個敘述最合乎統計檢定的意義？'
                q['ans'] = 'B'
                q['options']['B'] = '我們在 95%的信心水準下拒絕虛無假設'
                q['options']['D'] = '我們犯型一錯誤的機率為 5%'
                q['exp'] = '顯著性水準設定為 0.05 表示，我們容許最多 5%的機率犯型一錯誤（即 Type-I Error），並非代表實際犯錯的機率是5%。'
            
    # Write to Markdown
    md_lines = []
    md_lines.append(f"# {title}")
    md_lines.append("\n本檔提供該科目學習指引的題庫解析。\n")
    md_lines.append("---\n")
    
    for q in q_list:
        md_lines.append(f"### Q{q['q_idx']}: {q['text']}\n")
        
        ans_char = q['ans']
        for opt_k in ['A', 'B', 'C', 'D']:
            opt_v = q['options'].get(opt_k, '')
            if opt_k == ans_char:
                md_lines.append(f"- <span style='color: #0066cc; font-weight: bold;'>({opt_k}) {opt_v}</span>")
            else:
                md_lines.append(f"- ({opt_k}) {opt_v}")
        
        md_lines.append("")
        ans_text_full = f"({ans_char}) {q['options'].get(ans_char, '')}"
        md_lines.append(f"<span style='color: #008000; font-weight: bold;'>✅ 正確解答：{ans_text_full}</span>  ")
        md_lines.append(f"<span style='color: #646464;'>💡 為什麼？ {q['exp']}</span>")
        md_lines.append("\n---\n")

    out_path = os.path.join(out_dir, out_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f"Generated {out_path} with {len(q_list)} questions")

