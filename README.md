# Mini Language Model Course

Course repository for the web platform [ondroid.org](https://ondroid.org).

This course teaches the full mini language model workflow:

```text
dataset -> tokenizer -> baseline LM -> neural LM -> evaluation -> generation -> deployment/demo -> feedback
```

## Current Stage

The course repository has been updated from the generic template to the current Mini LM lesson plan.

Implemented in the sibling worker repository:

- `Lab 03: Bigram Character Language Model` local worker/grader prototype
- sample job: `../mini-lm-worker/sample_jobs/lab_03_bigram.json`
- sample submission: `../mini-lm-worker/sample_submissions/lab_03_bigram/train_bigram.py`
- grader: `../mini-lm-worker/src/ai_grader/assignments/lab_03_bigram.py`

Prepared in this course repository:

- course metadata in `course-info.json`
- module and lesson structure in `lessons-list.json`
- overview lesson in `lessons/module-0/course_overview.md`
- lab placeholders for `Lab 01` through `Lab 08`
- step-by-step English lessons for `Lab 03.1` through `Lab 03.8`
- browser editor starter code in `lessons-list.json` under each lesson's `template` field
- course-side verification functions in `verifications/module_1.py`

## Description of Repository Structure

- **images** folder: Contains images for the course. Images can be organized in any structure within this folder. We suggest saving images in different folders for different modules.
- **lessons** folder: Contains lessons in Markdown (.md) format. Lessons can be organized in any structure within this folder. We suggest saving lessons in different folders for different modules.
- **course-info.json** file: Contains basic information about the course, such as the full course name, short name, description, workload, student requirements, and image links.
- **lessons-list.json** file: Contains a list modules with lessons:
- **verifications** folder: Contains Python verification code loaded by the worker. The browser editor templates live in the course, while datasets and execution happen in the worker.

### Structure of lessons-list.json
**lessons-list.json** contains list with modules.
Every module in the list has structure:

- *str_id*: unique string identifier for each module in the course.
- *name*: display name of the module on the course page.
- *description*: description of the module.
- *sn*: Serial number of the module in the course, **starting from 0**.
- *lessons*: list of the lessons in the module.

Every lessons has structure:
- *str_id*: Unique string identifier for each lesson in the course.
- *name*: Display name of the lesson on the course page.
- *url*: URL for the lesson's Markdown file.
- *sn*: Serial number of the lesson in the course, starting from 0.
- *description*: description of the lesson.
- *template*: starter Python code shown in the browser editor.

### Structure of course-info.json
Course info:

- *fullCourseName*: Full name of the course.
- *shortCourseName*: Short name of the course.
- *shortDescription*: A short description of the course, up to 160 characters.
- *fullDescription*: A full description of the course, around 500 characters.
- *imageSmall*: URL for the small image (approximately 640x360 px).
- *imageBig*: URL for the large image (approximately 1920x1080 px).
- *workload*: Estimated time required to complete the course.
- *programmingLanguage*: string identifyer of programming language used in course.
