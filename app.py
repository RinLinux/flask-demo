import json

from flask import Flask,render_template,request

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
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)
