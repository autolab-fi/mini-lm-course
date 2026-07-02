# Mini Language Model Course

## Цель курса

В этом курсе вы шаг за шагом построите маленькую language model: от текстового датасета до генерации текста и простого demo.

Учебная траектория:

```text
dataset -> tokenizer -> baseline LM -> neural LM -> evaluation -> generation -> deployment/demo -> feedback
```

Главная идея курса: каждый lab добавляет один новый слой понимания. Сначала вы готовите данные, затем превращаете символы в token ids, строите простой baseline без neural networks, а после этого переходите к обучаемой модели.

## Что вы будете делать

1. Подготовите train/validation/test split для текстового корпуса.
2. Реализуете символьный tokenizer.
3. Построите bigram character language model.
4. Обучите маленькую neural character LM.
5. Реализуете generation CLI с temperature sampling.
6. Сравните baseline и neural model через validation loss и perplexity.
7. Подготовите простой inference demo.
8. Запустите edge demo и измерите ограничения по latency, memory и model size.

## Как устроены проверки

Каждая лабораторная сохраняет artifacts: JSON, markdown reports, model checkpoints или generated samples. Автоматический grader проверяет не только запуск кода, но и формат результатов.

Для первых labs основной язык - Python. Форматы файлов и требования к artifacts указаны внутри каждого задания.

## Текущая стадия курса

На данный момент подготовлен план курса и реализован первый рабочий вертикальный срез worker/grader для `Lab 03: Bigram Character Language Model`.

Это значит, что `Lab 03` уже можно проверять локально через sample job: student submission запускается, artifacts собираются, grader выставляет score и сохраняет `result.json`.
