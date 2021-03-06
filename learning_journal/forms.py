from wtforms import (
    Form,
    HiddenField,
    PasswordField,
    TextField,
    TextAreaField,
    validators,
)

strip_filter = lambda x: x.strip() if x else None


class EntryCreateForm(Form):
    title = TextField(
        'Entry title',
        [validators.Length(min=1, max=255)],
        filters=[strip_filter]
    )
    body = TextAreaField(
        'Entry body',
        [validators.Length(min=1)],
        filters=[strip_filter]
    )

class EntryEditForm(EntryCreateForm):
    id = HiddenField()

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=1, max=255)])
    password = PasswordField('Password', [validators.Length(min=1, max=255)])
