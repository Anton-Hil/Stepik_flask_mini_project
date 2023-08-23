from flask_wtf import FlaskForm
from wtforms import RadioField, IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired, NumberRange


class ChooseDirectionForm(FlaskForm):
    direction = RadioField(label='Choose direction',
                           choices=['Up',
                                    'Down',
                                    'Lef',
                                    'Right'],
                           coerce=str,
                           validators=[InputRequired]
                           )
    submit = SubmitField('Submit')


class SettingsForm(FlaskForm):
    field_height = IntegerField(label='Field height',
                                default=20,
                                validators=[InputRequired, NumberRange(min=2)]
                                )
    field_width = IntegerField(label='Field width',
                               default=20,
                               validators=[InputRequired, NumberRange(min=2)]
                               )
    difficulty = SelectField(label='Choose difficulty',
                             choices=['Easy',
                                      'Normal',
                                      'Hard'
                                      ],
                             default='Normal',
                             validators=[InputRequired]
                             )
    submit = SubmitField('Submit')
