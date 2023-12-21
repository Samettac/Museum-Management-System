from flask import Flask, render_template, redirect, url_for
from entity import Eser, Sergi
from business.concrete import SergiService, EserService
from data_access.concrete import MemorySergiDal, MemoryEserDal
from web_app.forms import EserForm, SergiForm

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


eser_service = EserService(eser_dal=MemoryEserDal())
sergi_service = SergiService(sergi_dal=MemorySergiDal())


@app.route('/')
def home():
    sergi_list = sergi_service.get_all()
    return render_template("index.html", sergi_list=sergi_list)


@app.route('/sergi/id/<int:id>')
def get_sergi(id):
    sergi = sergi_service.get_by_id(id)
    return render_template("sergi.html", sergi=sergi)


@app.route('/add/sergi', methods=['POST', 'GET'])
def add_sergi():
    sergi_form = SergiForm()
    sergi_form.sergideki_eserler.choices = [(eser.eser_id, eser.eser_adi) for eser in eser_service.get_all()]
    if sergi_form.validate_on_submit():
        sergi_id = sergi_form.sergi_id.data
        sergi_adi = sergi_form.sergi_adi.data
        sergi_tipi = sergi_form.sergi_tipi.data
        sergi_tarihi = sergi_form.sergi_tarihi.data
        eser_aciklama = sergi_form.sergi_aciklama.data
        sergideki_eserler = sergi_form.sergideki_eserler.data
        sergideki_eserler = [eser_service.get_by_id(id) for id in sergideki_eserler]
        sergi_service.add(Sergi(sergi_id=sergi_id, sergi_adi=sergi_adi, sergi_tipi=sergi_tipi, sergi_tarihi=sergi_tarihi,
                                sergi_aciklama=eser_aciklama, sergideki_eserler=sergideki_eserler))
        return redirect(url_for("get_sergi", id=sergi_id))
    else:
        return render_template("add_sergi.html", form=sergi_form)


@app.route('/edit/sergi/<int:id>', methods=['POST', 'GET'])
def edit_sergi(id):
    sergi_form = SergiForm()
    sergi_form.sergideki_eserler.choices = [(eser.eser_id, eser.eser_adi) for eser in eser_service.get_all()]
    if sergi_form.is_submitted():
        sergi_id = int(sergi_form.sergi_id.data)
        sergi_adi = sergi_form.sergi_adi.data
        sergi_tipi = sergi_form.sergi_tipi.data
        sergi_tarihi = sergi_form.sergi_tarihi.data
        sergi_aciklama = sergi_form.sergi_aciklama.data
        sergideki_eserler = sergi_form.sergideki_eserler.data
        sergideki_eserler = [eser_service.get_by_id(id) for id in sergideki_eserler]
        # print(type(sergideki_eserler))
        # print(sergideki_eserler)
        sergi_service.update(Sergi(sergi_id=sergi_id, sergi_adi=sergi_adi, sergi_tipi=sergi_tipi,
                                   sergi_tarihi=sergi_tarihi, sergi_aciklama=sergi_aciklama, sergideki_eserler=sergideki_eserler))
        # for sergi in sergi_service.get_all():
        #     print(sergi)
        return redirect(url_for("get_sergi", id=sergi_id))
    else:
        sergi = sergi_service.get_by_id(id)
        sergi_form.sergi_id.data = sergi.sergi_id
        sergi_form.sergi_adi.data = sergi.sergi_adi
        sergi_form.sergi_tipi.data = sergi.sergi_tipi
        sergi_form.sergi_tarihi.data = sergi.sergi_tarihi
        sergi_form.sergi_aciklama.data = sergi.sergi_aciklama

        return render_template("edit_sergi.html", form=sergi_form, sergi=sergi)


@app.route('/eser/id/<int:id>')
def get_eser(id):
    eser = eser_service.get_by_id(id)
    return render_template("eser.html", eser=eser)


@app.route('/add/eser', methods=['POST', 'GET'])
def add_eser():
    eser_form = EserForm()
    if eser_form.validate_on_submit():
        eser_id = eser_form.eser_id.data
        eser_adi = eser_form.eser_adi.data
        eser_yazar = eser_form.eser_yazari.data
        eser_tarihi = eser_form.eser_tarihi.data
        eser_aciklama = eser_form.eser_aciklama.data
        eser_service.add(Eser(eser_id=eser_id, eser_adi=eser_adi, eser_yazari=eser_yazar, eser_tarihi=eser_tarihi,
                              eser_aciklama=eser_aciklama))
        return redirect(url_for("get_eser", id=eser_id))
    else:
        return render_template("add_eser.html", form=eser_form)


@app.route('/edit/eser/<int:id>', methods=['POST', 'GET'])
def edit_eser(id):
    eser_form = EserForm()
    if eser_form.validate_on_submit():
        eser_id = eser_form.eser_id.data
        eser_adi = eser_form.eser_adi.data
        eser_yazar = eser_form.eser_yazari.data
        eser_tarihi = eser_form.eser_tarihi.data
        eser_aciklama = eser_form.eser_aciklama.data
        eser_service.update(Eser(eser_id=eser_id, eser_adi=eser_adi, eser_yazari=eser_yazar, eser_tarihi=eser_tarihi,
                                 eser_aciklama=eser_aciklama))
        return redirect(url_for("get_eser", id=eser_id))
    else:
        eser = eser_service.get_by_id(id)
        eser_form.eser_id.data = eser.eser_id
        eser_form.eser_adi.data = eser.eser_adi
        eser_form.eser_yazari.data = eser.eser_yazari
        eser_form.eser_tarihi.data = eser.eser_tarihi
        eser_form.eser_aciklama.data = eser.eser_aciklama
        return render_template("edit_eser.html", eser=eser, form=eser_form)


def delete_eser(eser: Eser):
    eser_service.delete(eser)
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)
