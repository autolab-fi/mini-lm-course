# suomalainen_lukemisto_chars

Character-level language modeling dataset derived from Project Gutenberg eBook: Suomalainen lukemisto.

Description: A Finnish reading anthology with prose and poetry.

Language: Finnish

Author/editor: Knut Cannelin

Source eBook page: https://www.gutenberg.org/ebooks/64973

Source text download: https://www.gutenberg.org/files/64973/64973-0.txt

Rights note: Project Gutenberg lists this eBook as public domain in the United States. Check local copyright rules before reuse outside this course context.

Split sizes by characters:

- train: 362831
- val: 45353
- test: 45355

Processing: normalized newlines to Unix `\n`, removed Project Gutenberg header/footer markers, trimmed trailing spaces, then split by character count using 80/10/10.
