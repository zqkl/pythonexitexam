from flask import render_template,request,redirect,session,flash
from flask_app import app
from flask_app.models.tv_show_model import Shows

@app.route('/add_show')
def add_show():
    return render_template('new_show.html')


@app.route('/adding_show',methods=['POST'])
def adding_show():
    if not Shows.validate_create(request.form):
        return redirect('/add_show')
    data = {
        **request.form,
        'users_id':session['id']
    }
    print(data)
    Shows.create_show(data)
    return redirect('/shows')

@app.route('/single_show/<int:id>')
def single_show(id):
    data={
        'id':id
    }
    one_show = Shows.one_show(data)
    print(one_show.title)
    return render_template('single_show.html',one_show=one_show)

@app.route('/delete_show/<int:id>')
def delete_show(id):
    data={
        'id':id
    }
    Shows.delete_show(data)
    return redirect('/shows')

@app.route('/edit_show/<int:id>')
def edit_user(id):
    one_show = Shows.one_show({'id':id})
    return render_template('edit_show.html',id=id,one_show=one_show)

@app.route('/editing/<int:id>',methods=['POST'])
def editing(id):
    data={
        **request.form,
        'id':id

    }
    Shows.edit_user(data)
    return redirect('/shows')