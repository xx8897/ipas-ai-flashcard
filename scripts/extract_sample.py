import os
import re

out_dir = r'c:\雲端\ipas AI應用證照\題庫\答案與解析'
os.makedirs(out_dir, exist_ok=True)

files = [
    (r'c:\雲端\ipas AI應用證照\題庫\scripts\sample_114_04.txt', '114年4月版考試樣題_題庫解析.md', 'iPAS AI應用規劃師初級能力鑑定 - 考試樣題 (114年4月版)'),
    (r'c:\雲端\ipas AI應用證照\題庫\scripts\sample_114_09.txt', '114年9月版考試樣題_題庫解析.md', 'iPAS AI應用規劃師初級能力鑑定 - 考試樣題 (114年9月版)')
]

def normalize_ans(c):
    mapping = {'Ａ':'A', 'Ｂ':'B', 'Ｃ':'C', 'Ｄ':'D'}
    return mapping.get(c, c).upper()

for txt_file, out_name, title in files:
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    q_header_pattern = re.compile(r'^(\d+)\.?\s+([A-DＡ-Ｄ])$')
    opt_pattern = re.compile(r'^[\(（]([A-D])[）\)](.*)')
    
    q_list = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Check if current line is a question header
        m_q = q_header_pattern.match(line)
        if m_q and 0 < int(m_q.group(1)) <= 100:
            q_num = int(m_q.group(1))
            ans_char = normalize_ans(m_q.group(2))
            
            q_text = ""
            opts = {}
            
            i += 1 # Move to the line after header
            while i < len(lines):
                l2 = lines[i].strip()
                if not l2:
                    i += 1
                    continue
                
                # If we hit the NEXT question header, stop parsing current one
                m_next_q = q_header_pattern.match(l2)
                if m_next_q and 0 < int(m_next_q.group(1)) <= 100:
                    i -= 1 # Step back so outer loop can catch this as a new question
                    break
                
                # Check for options
                m_opt = opt_pattern.match(l2)
                if m_opt:
                    opts[m_opt.group(1)] = m_opt.group(2).strip()
                else:
                    # Ignore headers/footers/page numbers
                    ignore_lines = [
                        'iPAS AI 應用規劃師', '樣題範例非正式考題', '114.04 版', '114.09 版',
                        '◆ 科目', '題號 答', '案', '題目', '第一科', '第二科'
                    ]
                    if any(ig in l2 for ig in ignore_lines) or re.match(r'^\d+$', l2):
                        pass # Ignore it
                    else:
                        # Append to question text or last option
                        if not opts:
                            q_text = (q_text + " " + l2).strip()
                        else:
                            last_k = list(opts.keys())[-1]
                            opts[last_k] = (opts[last_k] + " " + l2).strip()
                i += 1
            
            # Save question even if options aren't 4 (will log for debugging)
            if q_text or opts:
                q_list.append({
                    'num': q_num,
                    'text': q_text or f"(無題目說明 - #{q_num})",
                    'options': opts,
                    'ans': ans_char
                })
        i += 1
            
    if not q_list:
        print(f"Warning: No questions found in {txt_file}")
        continue
        
    md_lines = []
    md_lines.append(f"# {title}")
    md_lines.append("\n本檔提供官方釋出的考試樣題與正確解答。\n")
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
        md_lines.append(f"<span style='color: #646464;'>💡 為什麼？ 本題為官方樣題，正確答案為 ({ans_char})。詳細觀念請參考「AI 應用規劃師」官方學習指引。</span>")
        md_lines.append("\n---\n")

    out_path = os.path.join(out_dir, out_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f"Generated {out_path} with {len(q_list)} questions")
