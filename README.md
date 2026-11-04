# English Worksheet Kit

An early-stage, MIT-licensed Python tool for teachers to generate printable English vocabulary worksheets with Vietnamese prompts. Designed for adult-led beginner practice, including young learners. It is independent and not affiliated with Cambridge or any examination provider.

## Sử dụng nhanh

1. Giải nén. Mở `sample_animals.html` bằng trình duyệt để xem phiếu mẫu.
2. Chọn **Print / In phiếu**; chọn Save as PDF nếu cần. Đáp án nằm ở trang riêng: chỉ in trang bài tập khi phát cho học sinh.
3. Muốn tạo phiếu mới, cài Python 3.9 trở lên rồi chạy trong thư mục dự án:

```sh
python generate.py --topic animals --count 6 --seed 5 --output worksheet.html
python generate.py --topic family --count 6 --title "My family" --output family.html
python generate.py --topic food --count 8 --output food.html
```

Không cần thư viện ngoài, tài khoản hay API. Không thu thập dữ liệu học sinh. Phiếu được tạo ngay trên máy.

## Current features

- Three editable vocabulary banks: animals, family, food.
- Missing-letter and three-option vocabulary questions.
- Reproducible random selection with `--seed`.
- Printable HTML with a separate teacher answer-key page.
- Escaped custom titles and validation of question counts.

## Project status

Version 0.1.0: a new prototype prepared with AI assistance. Published as an initial prototype; not yet evaluated in classrooms. No verified users, downloads, external contributors, or ecosystem adoption are claimed. The word banks are original small teaching lists, not an official Cambridge vocabulary list. Vietnamese prompts require teacher support for pre-readers.

## Contributing

Review spelling, suggest vocabulary with clear translations, improve accessibility, or add exercises. Once a repository is published, use issues and pull requests; do not include children's personal information. Before contributing, run:

```sh
python -m unittest discover -s tests
```

## Next steps

Teacher feedback, illustrated exercises with appropriately licensed images, additional word banks, and improved layout. These are planned, not completed.
