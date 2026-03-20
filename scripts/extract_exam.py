import os
import re

out_dir = r'c:\雲端\ipas AI應用證照\題庫\答案與解析'
os.makedirs(out_dir, exist_ok=True)

files = [
    (r'c:\雲端\ipas AI應用證照\題庫\sub1_exam.txt', '114年第四梯次_科目1人工智慧基礎概論_考古題解析.md', '114年第四梯次初級AI應用規劃師 第一科人工智慧基礎概論 考古題解析'),
    (r'c:\雲端\ipas AI應用證照\題庫\sub2_exam.txt', '114年第四梯次_科目2生成式AI應用與規劃_考古題解析.md', '114年第四梯次初級AI應用規劃師 第二科生成式AI應用與規劃 考古題解析')
]

def normalize_ans(c):
    mapping = {'Ａ':'A', 'Ｂ':'B', 'Ｃ':'C', 'Ｄ':'D'}
    return mapping.get(c, c).upper()

for txt_file, out_name, title in files:
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    q_pattern = re.compile(r'^([A-DＡ-Ｄ])\s+(\d+)\.\s+(.*)')
    opt_pattern = re.compile(r'^[\(（]([A-D])[）\)](.*)')
    
    q_list = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        m_q = q_pattern.match(line)
        if m_q:
            ans_char = normalize_ans(m_q.group(1))
            q_num = int(m_q.group(2))
            q_text = m_q.group(3)
            opts = {}
            i += 1
            while i < len(lines):
                if i >= len(lines):
                    break
                l2 = lines[i].strip()
                # Stop if next question
                if q_pattern.match(l2):
                    i -= 1
                    break
                    
                m_opt = opt_pattern.match(l2)
                if m_opt:
                    opts[m_opt.group(1)] = m_opt.group(2).strip()
                elif l2 and not m_opt:
                    # Ignore page header
                    if '114 年第四次AI 應用規劃師' in l2 or '第一科：' in l2 or '第二科：' in l2 or '考試日期：' in l2 or ('第 ' in l2 and '頁，共 ' in l2) or '答案 題    目' in l2 or '《以下空白》' in l2 or '答案題 目' in l2.replace(' ', ''):
                        pass
                    else:
                        if not opts:
                            q_text += " " + l2
                        else:
                            last_k = list(opts.keys())[-1]
                            opts[last_k] += " " + l2
                i += 1
            
            if len(opts) >= 4:
                q_list.append({
                    'num': q_num,
                    'text': q_text.strip(),
                    'options': opts,
                    'ans': ans_char
                })
        i += 1
            
    if not q_list:
        print(f"Warning: No questions found in {txt_file}")
        continue
        
    md_lines = []
    md_lines.append(f"# {title}")
    md_lines.append("\n本檔提供 114 年考試考古題與正確解答。\n")
    md_lines.append("---\n")
    
    for idx, q in enumerate(q_list, 1):
        md_lines.append(f"### Q{idx}: {q['text']}\n")
        
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
        md_lines.append(f"<span style='color: #646464;'>💡 為什麼？ 本題為 114 年考古題，正確答案為 ({ans_char})。詳細觀念請參考「AI 應用規劃師」官方學習指引。</span>")
        md_lines.append("\n---\n")

    out_path = os.path.join(out_dir, out_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f"Generated {out_path} with {len(q_list)} questions")
