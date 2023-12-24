from entity import Etkinlik
from business.concrete import EtkinlikService
from data_access.concrete import MemoryEtkinlikDal
from web_app.forms import EtkinlikForm
from __main__ import app, render_template, url_for, redirect, login_required


etkinlik_service = EtkinlikService(etkinlik_dal=MemoryEtkinlikDal())

# ETKİNLİK ile ilgili sayfalar


# bütün etkinlikerin listelendiği sayfa
@app.route('/etkinlikler')
def get_all_etkinlikler():
    etkinlik_list = etkinlik_service.get_all()
    return render_template("etkinlikler.html", etkinlik_list=etkinlik_list)


# ilgili etkinliğin listelendiği sayfa
@app.route('/etkinlik/id/<int:id>')
def get_etkinlik(id):
    etkinlik = etkinlik_service.get_by_id(id)
    return render_template("etkinlik.html", etkinlik=etkinlik)


# sayfaya get isteği gelirse ilgili html sayfasına yönlendirme ve
# post istediği gelirse ilgili verilerin formdan alınıp uygunsa hafızaya eklenmesi ve ilgili etkinliğin detay sayfasına yönlendirme
@app.route('/add/etkinlik', methods=['POST', 'GET'])
@login_required
def add_etkinlik():
    etkinlik_form = EtkinlikForm()
    if etkinlik_form.validate_on_submit():
        etkinlik = get_form_fields(etkinlik_form)
        etkinlik_service.add(etkinlik)
        return redirect(url_for("get_etkinlik", id=etkinlik.etkinlik_id))
    else:
        return render_template("add_etkinlik.html", form=etkinlik_form)


# sayfaya get isteği gelirse ilgili verilerin html sayfasında dolu olarak gelmesi  ve
# post istediği gelirse ilgili verilerin formdan alınıp uygunsa hafızada güncellenmesi ve ilgili etkinliğin detay sayfasına yönlendirme
@app.route('/edit/etkinlik/<int:id>', methods=['POST', 'GET'])
@login_required
def edit_etkinlik(id):
    etkinlik_form = EtkinlikForm()
    if etkinlik_form.validate_on_submit():
        etkinlik = get_form_fields(etkinlik_form)
        etkinlik_service.update(etkinlik)
        return redirect(url_for("get_etkinlik", id=etkinlik.etkinlik_id))
    else:
        etkinlik = fill_form_fields(id, etkinlik_form)
        return render_template("edit_etkinlik.html", etkinlik=etkinlik, form=etkinlik_form)


# fonksiyon çağrıldığında ilgili etkinliğin hafızadan silinmesi
@app.route("/delete/etkinlik/<int:id>")
@login_required
def delete_etkinlik(id):
    etkinlik = etkinlik_service.get_by_id(id)
    etkinlik_service.delete(etkinlik)
    return redirect(url_for("get_all_etkinlikler"))


# post isteği atıldığında eserle ilgili form alanlarınındaki veriyi alıp Etkinlik öğesi olarak döndürür
def get_form_fields(etkinlik_form_param) -> Etkinlik:
    etkinlik_form = etkinlik_form_param
    etkinlik_id = etkinlik_form.etkinlik_id.data
    etkinlik_adi = etkinlik_form.etkinlik_adi.data
    etkinlik_tarihi = etkinlik_form.etkinlik_tarihi.data
    etkinlik_aciklama = etkinlik_form.etkinlik_aciklama.data
    return Etkinlik(etkinlik_id=etkinlik_id, etkinlik_adi=etkinlik_adi, etkinlik_tarihi=etkinlik_tarihi,
                     etkinlik_aciklama=etkinlik_aciklama)


# verilen eser formunun alanlarını verilen eser verisiyle doldurur ve döndürür
def fill_form_fields(id, etkinlik_form_param) -> Etkinlik:
    etkinlik_form = etkinlik_form_param
    etkinlik = etkinlik_service.get_by_id(id)
    etkinlik_form.etkinlik_id.data = etkinlik.etkinlik_id
    etkinlik_form.etkinlik_adi.data = etkinlik.etkinlik_adi
    etkinlik_form.etkinlik_tarihi.data = etkinlik.etkinlik_tarihi
    etkinlik_form.etkinlik_aciklama.data = etkinlik.etkinlik_aciklama
    return etkinlik
