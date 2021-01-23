import json

from flask import Flask,render_template,request

import db

app = Flask(__name__)

def readr():
    data = []
    with open('./static/gene.txt','r') as fin:
        is_first_line = True
        for line in fin:
            if is_first_line:
                is_first_line = False
                continue
            line = line[:-1]
            infor = {}
            gene_symbol,ensembl_gene_id,GeneID = line.split('\t')[0:3]
            infor['symbol'] = gene_symbol
            infor['ensembl'] = ensembl_gene_id
            infor['GeneID'] = GeneID
            data.append(infor)
    return data

@app.route('/genes')
@app.route('/')
def genes():
    data = readr()
    return render_template('gene.html',data=data)

@app.route('/getjson')
def getjson():
    data = readr()
    return json.dumps(data)


@app.route('/show_add_user')
def show_add_user():
    return render_template('show_add_user.html')


@app.route('/do_add_user',methods=['POST'])
def do_add_user():
    print(request.form)
    name = request.form.get('name')
    sex = request.form.get('sex')
    age = request.form.get('age')
    email = request.form.get('email')
    sql = f"""
        insert into user (name, sex, age, email)
        values ('{name}', '{sex}', {age}, '{email}')
    """
    print(sql)
    db.inser_or_update(sql)
    return "Success"


@app.route('/show_users')
def show_users():
    sql = "select id, name from user"
    data = db.query_data(sql)
    return render_template('show_users.html',data=data)


@app.route('/show_user/<user_id>')
def show_user(user_id):
    sql = "select * from user where id=" + user_id
    data = db.query_data(sql)
    user = data[0]
    return render_template('show_user.html',user=user)

if __name__ == '__main__':
    app.run(debug=True)
