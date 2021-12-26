from flask import flash


class Survey:

    @staticmethod
    def validate_form(survey):
        is_valid = True
        if len(survey['name']) < 0:
            flash('Enter Name')
            is_valid = False
        if len(survey['location']) < 2:
            flash('Must be at least 2 characters')
            is_valid = False
        if len(survey['language']) < 2:
            flash('Must give a language')
            is_valid = False
        return is_valid
