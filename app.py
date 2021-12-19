from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = "zullowa06"


class testForm(FlaskForm):
    nama = StringField('Nama Lengkap :')
    umur = StringField('Umur :')
    nohp = StringField('Nomor Hp :')
    email = StringField('Email Pribadi:')
    ktp = StringField('No KTP :')
    alamat = TextAreaField(
        'Alamat KTP : ')
    submit = SubmitField(label=('Submit'))


@app.route("/")
def home():
    return render_template('pages/home.html', judul='Covid-19')


@app.route("/regist", methods=['GET', 'POST'])
def regist():

    form = testForm()
    kelamin = request.form.getlist('kelamin')
    suhu = request.form.getlist('suhu')
    item_suhu = request.form.getlist('item_suhu')
    napas = request.form.getlist('napas')
    item_napas = request.form.getlist('item_napas')
    gejala = request.form.getlist('gejala')
    item_gejala = request.form.getlist('item_gejala')
    kondisi = request.form.getlist('kondisi')
    item_kondisi = request.form.getlist('item_kondisi')
    kontak1 = request.form.getlist('kontak1')
    item_kontak1 = request.form.getlist('item_kontak1')
    kontak2 = request.form.getlist('kontak2')
    item_kontak2 = request.form.getlist('item_kontak2')
    kontak3 = request.form.getlist('kontak3')
    item_kontak3 = request.form.getlist('item_kontak3')
    pergi = request.form.getlist('pergi')
    item_pergi = request.form.getlist('item_pergi')

    data_kelamin = ""
    for data in kelamin:
        data_kelamin = data

    data_suhu = 0
    index_suhu = ""
    for i, s in zip(item_suhu, suhu):
        data_suhu = data_suhu + int(s)
        index_suhu = index_suhu + i
        if index_suhu == "Tidak pernah melakukan pemeriksaan suhu":
            data_suhu = 1

    data_napas = 0
    index_napas = ""
    for n, i in zip(napas, item_napas):
        data_napas = data_napas + int(n)
        index_napas = index_napas + i
        if index_napas == "Tidak pernah mengalami sesak napas":
            data_napas = 1

    data_gejala = 0
    nama_gejala = ""
    for g, i in zip(gejala, item_gejala):
        data_gejala = data_gejala + int(g)
        nama_gejala = nama_gejala + i
        if nama_gejala == "Tidak memiliki gejala":
            data_gejala = 2

    data_kondisi = 0
    nama_kondisi = ""
    for k, i in zip(kondisi, item_kondisi):
        data_kondisi = data_kondisi + int(k)
        nama_kondisi = nama_kondisi + i
        if nama_kondisi == "Tidak memiliki riwayat kondisi":
            data_kondisi = 2

    data_kontak1 = 0
    nama_kontak1 = ""
    for k, i in zip(kontak1, item_kontak1):
        data_kontak1 = data_kontak1 + int(k)
        nama_kontak1 = nama_kontak1 + i
        if nama_kontak1 == "Tidak Pernah Berkontak dengan Pasien Positif atau Suspek Covid-19":
            data_kontak1 = 2

    data_kontak2 = 0
    nama_kontak2 = ""
    for k, i in zip(kontak2, item_kontak2):
        data_kontak2 = data_kontak2 + int(k)
        nama_kontak2 = nama_kontak2 + i
        if nama_kontak2 == "Tidak Pernah Berkontak dengan Pasien dalam Pengawasan (PDP)":
            data_kontak2 = 2

    data_kontak3 = 0
    nama_kontak3 = ""
    for k, i in zip(kontak3, item_kontak3):
        data_kontak3 = data_kontak3 + int(k)
        nama_kontak3 = nama_kontak3 + i
        if nama_kontak3 == "Tidak Terlibat Menangani Pasien":
            data_kontak3 = 2

    data_pergi = 0
    nama_tempat = ""
    for p, i in zip(pergi, item_pergi):
        data_pergi = data_pergi + int(p)
        nama_tempat = nama_tempat + i

    total = data_suhu + data_napas + data_gejala + data_gejala + \
        data_kondisi + data_kontak1 + data_kontak2 + data_kontak3 + data_pergi

    if form.validate_on_submit():
        return render_template(
            'pages/result.html',
            judul="Hasil Tes",
            total=total
        ).format(
            form.nama.data,
            form.umur.data,
            data_kelamin,
            form.nohp.data,
            form.email.data,
            form.ktp.data,
            form.alamat.data,
            index_suhu,
            index_napas,
            nama_gejala,
            nama_kondisi,
            nama_kontak1,
            nama_kontak2,
            nama_kontak3,
            nama_tempat,
            total
        )

    return render_template('pages/regist.html', judul="Tes Covid-19", form=form)


if __name__ == '__main__':
    app.run(debug=True)
