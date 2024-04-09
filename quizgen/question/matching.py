import quizgen.common
import quizgen.constants
import quizgen.question.base

class Matching(quizgen.question.base.Question, question_type = quizgen.constants.QUESTION_TYPE_MATCHING):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_answers(self):
        self._check_type(self.answers, dict, "'answers' key")

        self._validate_matches()
        self._validate_distractors()

    def _validate_matches(self):
        if ('matches' not in self.answers):
            raise quizgen.common.QuizValidationError("Matching 'answers' value is missing the 'matches' field.")

        matches = self.answers['matches']
        new_matches = []

        for i in range(len(matches)):
            match = matches[i]

            if (isinstance(match, list)):
                if (len(match) != 2):
                    raise quizgen.common.QuizValidationError(f"Expected exactly two items for a match list, found {len(match)} items at element {i}.")

                match = {
                    'left': match[0],
                    'right': match[1],
                }

            keys = ['left', 'right']
            for key in keys:
                if (key not in match):
                    raise quizgen.common.QuizValidationError("Missing key '{key}' for for match item {i}.")

            new_matches.append({
                'left': self._validate_text_item(match['left'], "Left value for match item %d" % (i)),
                'right': self._validate_text_item(match['right'], "Right value for match item %d" % (i)),
            })

        self.answers['matches'] = new_matches

    def _validate_distractors(self):
        if ('distractors' not in self.answers):
            self.answers['distractors'] = []

        distractors = self.answers['distractors']
        new_distractors = []

        for i in range(len(distractors)):
            new_distractors.append(self._validate_text_item(distractors[i], "distractor at index %d" % (i),
                    clean_whitespace = True))

        self.answers['distractors'] = new_distractors

    def _shuffle(self, rng):
        # Shuffling matching is special because it requires additional shuffling support at the converter level.
        self.answers['shuffle'] = True
        self.answers['shuffle_seed'] = rng.randint(0, 2 ** 64)
