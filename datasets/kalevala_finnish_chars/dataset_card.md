# kalevala_finnish_chars

Character-level language modeling dataset derived from Project Gutenberg eBook: Kalevala.

Description: Finnish epic poetry compiled by Elias Lonnrot.

Language: Finnish

Author/editor: Elias Lonnrot

Source eBook page: https://www.gutenberg.org/ebooks/7000

Source text download: https://www.gutenberg.org/cache/epub/7000/pg7000.txt

Rights note: Project Gutenberg lists this eBook as public domain in the United States. Check local copyright rules before reuse outside this course context.

Split sizes by characters:

- train: 474505
- val: 59313
- test: 59314

Processing: normalized newlines to Unix `\n`, removed Project Gutenberg header/footer markers, trimmed trailing spaces, then split by character count using 80/10/10.
