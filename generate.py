"""Generate printable vocabulary worksheets. Python 3.9+, standard library only."""
import argparse
import html
import random
from pathlib import Path

BANK = {
    'animals': [('cat', 'con mèo'), ('dog', 'con chó'), ('bird', 'con chim'), ('fish', 'con cá'), ('duck', 'con vịt'), ('rabbit', 'con thỏ'), ('cow', 'con bò'), ('frog', 'con ếch')],
    'family': [('mother', 'mẹ'), ('father', 'bố'), ('sister', 'chị hoặc em gái'), ('brother', 'anh hoặc em trai'), ('grandmother', 'bà'), ('grandfather', 'ông')],
    'food': [('rice', 'cơm'), ('bread', 'bánh mì'), ('milk', 'sữa'), ('egg', 'trứng'), ('apple', 'quả táo'), ('banana', 'quả chuối'), ('carrot', 'củ cà rốt'), ('cake', 'bánh ngọt')],
}

def generate(topic='animals', count=6, seed=1, title='English practice'):
    if topic not in BANK:
        raise ValueError('Unknown topic')
    if not 1 <= count <= len(BANK[topic]):
        raise ValueError(f'Count must be 1–{len(BANK[topic])}')
    rng = random.Random(seed)
    words = rng.sample(BANK[topic], count)
    questions, answers = [], []
    for number, (word, meaning) in enumerate(words, 1):
        index = rng.randrange(len(word))
        missing = word[:index] + '_' + word[index+1:]
        options = rng.sample([pair[0] for pair in BANK[topic] if pair[0] != word], 2) + [word]
        rng.shuffle(options)
        choices = ' &nbsp; '.join(f'{chr(65+i)}. {html.escape(option)}' for i, option in enumerate(options))
        questions.append(f'<li><b>{html.escape(meaning)}</b><p>Complete / Điền chữ: {missing}</p><p>Choose / Chọn từ: {choices}</p></li>')
        answers.append(f'<li>{word} — {word[index]} — {chr(65+options.index(word))}</li>')
    return '''<!doctype html><html lang="en"><meta charset="utf-8">
<title>English Worksheet Kit</title><style>
body{font:18px Arial,sans-serif;max-width:760px;margin:35px auto;color:#15354a;padding:20px}
h1{color:#086b70}li{padding:8px 0;break-inside:avoid}p{margin:10px 0}
.answers{break-before:page}button{padding:12px;background:#086b70;color:white;border:0;border-radius:8px}
@media print{button{display:none}body{margin:0;color:#000}@page{size:A4;margin:18mm}}
</style><button onclick="window.print()">Print / In phiếu</button>''' + f'<h1>{html.escape(title)}</h1><p>Name / Tên: ____________________ Date / Ngày: __________</p><p>Topic / Chủ đề: {topic}</p><ol>' + ''.join(questions) + '</ol><section class="answers"><h1>Teacher answer key / Đáp án</h1><p>Word — missing letter — correct choice</p><ol>' + ''.join(answers) + '</ol></section></html>'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic', choices=BANK, default='animals')
    parser.add_argument('--count', type=int, default=6)
    parser.add_argument('--seed', type=int, default=1)
    parser.add_argument('--title', default='English practice')
    parser.add_argument('--output', type=Path, default=Path('worksheet.html'))
    args = parser.parse_args()
    try:
        result = generate(args.topic, args.count, args.seed, args.title)
    except ValueError as error:
        parser.error(str(error))
    args.output.write_text(result, encoding='utf-8')
    print(f'Created {args.output}')

if __name__ == '__main__':
    main()
