from flask import Flask, render_template, redirect, url_for, request, flash, session
from forms import HiForm, RunnerForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any_key'


@app.route('/', methods=['get', 'post'])
def hi():
    form = HiForm()
    if form.validate_on_submit():
        name = form.name.data
        print(name)
        return redirect(url_for('runner'))
    return render_template('hi.html', form=form)


@app.route('/runner', methods=['get', 'post'])
def runner():
    form = RunnerForm()
    flash('Ты находишься в Подземелье!')
    if form.validate_on_submit():
        way = form.way.data
        step = form.num_steps.data
        if way == 0:
            if step == 1:
                return redirect(url_for('bedroom'))
            else:
                flash('Ты туда не попадёшь')
        elif way == 1:
            if step == 1:
                return redirect(url_for('hallway'))
            elif step == 2:
                return redirect(url_for('bathroom'))
            else:
                flash('Ты туда не попадёшь')
        elif way == 2:
            flash('Ты туда не попадёшь')
        else:
            flash('Ты туда не попадёшь')
    return render_template('go.html', form=form)


@app.route('/runner/bedroom', methods=['get', 'post'])
def bedroom():
    form = RunnerForm()
    flash('Ты находишься в Спальне!')
    if form.validate_on_submit():
        way = form.way.data
        step = form.num_steps.data
        if way == 0:
            flash('Ты туда не попадёшь')
        elif way == 1:
            if step == 1:
                return redirect(url_for('living_room'))
            elif step == 2:
                return redirect(url_for('kitchen'))
            else:
                flash('Ты туда не попадёшь')
        elif way == 2:
            if step == 1:
                return redirect(url_for('runner'))
            else:
                flash('Ты туда не попадёшь')
        else:
            flash('Ты туда не попадёшь')
    return render_template('go.html', form=form)


@app.route('/runner/living_room', methods=['get', 'post'])
def living_room():
    form = RunnerForm()
    flash('Ты находишься в Гостиной!')
    if form.validate_on_submit():
        way = form.way.data
        step = form.num_steps.data
        if way == 0:
            flash('Ты туда не попадёшь')
        elif way == 1:
            flash('Ты выбрался из подземелья!!!')
            return redirect(url_for('hi'))
        elif way == 2:
            if step == 1:
                return redirect(url_for('runner'))
            else:
                flash('Ты туда не попадёшь')
        else:
            flash('Ты туда не попадёшь')
    return render_template('go.html', form=form)


@app.route('/runner/kitchen', methods=['get', 'post'])
def living_room():
    form = RunnerForm()
    flash('Ты находишься в Гостиной!')
    if form.validate_on_submit():
        way = form.way.data
        step = form.num_steps.data
        if way == 0:
            flash('Ты туда не попадёшь')
        elif way == 1:
            flash('Ты выбрался из подземелья!!!')
            return redirect(url_for('hi'))
        elif way == 2:
            if step == 1:
                return redirect(url_for('runner'))
            else:
                flash('Ты туда не попадёшь')
        else:
            flash('Ты туда не попадёшь')
    return render_template('go.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
