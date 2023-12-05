DOC_FORMAT_HTML = 'html'
DOC_FORMAT_JSON = 'json'
DOC_FORMAT_MD = 'md'
DOC_FORMAT_TEX = 'tex'
DOC_FORMATS = [DOC_FORMAT_HTML, DOC_FORMAT_JSON, DOC_FORMAT_MD, DOC_FORMAT_TEX]

QUIZ_TYPE_PRACTICE = 'practice_quiz'
QUIZ_TYPE_ASSIGNMENT = 'assignment'
QUIZ_TYPE_GRADED_SURVEY = 'graded_survey'
QUIZ_TYPE_SURVEY = 'survey'
QUIZ_TYPES = [QUIZ_TYPE_PRACTICE, QUIZ_TYPE_ASSIGNMENT, QUIZ_TYPE_GRADED_SURVEY, QUIZ_TYPE_SURVEY]

# All question types Canvas supports.
QUESTION_TYPE_CALCULATED = 'calculated_question'
QUESTION_TYPE_ESSAY = 'essay_question'
QUESTION_TYPE_FILE_UPLOAD = 'file_upload_question'
QUESTION_TYPE_FILL_IN_MULTIPLE_BLANKS = 'fill_in_multiple_blanks_question'
QUESTION_TYPE_MATCHING = 'matching_question'
QUESTION_TYPE_MULTIPLE_ANSWERS = 'multiple_answers_question'
QUESTION_TYPE_MULTIPLE_CHOICE = 'multiple_choice_question'
QUESTION_TYPE_MULTIPLE_DROPDOWNS = 'multiple_dropdowns_question'
QUESTION_TYPE_NUMERICAL = 'numerical_question'
QUESTION_TYPE_SHORT_ANSWER = 'short_answer_question'
QUESTION_TYPE_TEXT_ONLY = 'text_only_question'
QUESTION_TYPE_TF = 'true_false_question'

# Supported question types.
QUESTION_TYPES = [
    QUESTION_TYPE_MATCHING,
    QUESTION_TYPE_MULTIPLE_ANSWERS,
    QUESTION_TYPE_MULTIPLE_CHOICE,
    QUESTION_TYPE_MULTIPLE_DROPDOWNS,
    QUESTION_TYPE_NUMERICAL,
    QUESTION_TYPE_TF,
]

NUMERICAL_ANSWER_TYPE_EXACT = 'exact'
NUMERICAL_ANSWER_TYPE_RANGE = 'range'
NUMERICAL_ANSWER_TYPE_PRECISION = 'precision'
