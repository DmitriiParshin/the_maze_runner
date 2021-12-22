from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange, Length, DataRequired


class HiForm(FlaskForm):
    name = StringField("Введи своё имя, путник:",
                           validators=[InputRequired(),
                                       Length(min=2, max=20)])
    submit = SubmitField("В путь!")


class RunnerForm(FlaskForm):
    submit = SubmitField("Поехали!")

    way = SelectField(
        'Выбери, куда будешь двигаться',
        coerce=int,
        choices=[
            (0, 'вперед'),
            (1, 'направо'),
            (2, 'назад'),
            (3, 'налево'),
        ],
        render_kw={
            'class': 'form-control'
        },
    )

    num_steps = IntegerField(
        'На сколько шагов?',
        validators=[NumberRange(min=1), DataRequired()],
        default=1,
        render_kw={
            'class': 'form-control'
        },
    )
