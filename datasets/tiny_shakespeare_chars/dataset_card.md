# tiny_shakespeare_chars

Character-level language modeling dataset derived from Tiny Shakespeare.

Source: https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

Original dataset is commonly used for character-level language modeling examples and contains text from Shakespeare plays.

Split sizes by characters:

- train: 892315
- val: 111539
- test: 111540

Processing: normalized newlines to Unix `\n`, then split by character count using 80/10/10.
