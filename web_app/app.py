'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''


from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from flask_bootstrap import Bootstrap5

from business.concrete import UserService, SergiService, EserService, EtkinlikService
from data_access.concrete import MemoryUserDal, MemorySergiDal, MemoryEserDal, MemoryEtkinlikDal
from web_app.forms import EtkinlikForm, EserForm, SergiForm

from eser_view import get_eser_fields, fill_eser_fields
from sergi_view import get_sergi_fields, fill_sergi_fields

# flask uygulamasını, formlar için bootstrapi ve login managerı başladığı yer
app = Flask(__name__)
Bootstrap5(app)
app.secret_key = "gizli kod"
login_manager = LoginManager()
login_manager.init_app(app)

# etkinlik ile ilgili sayfaların importu
import web_app.etkinlik_view

# ilgili classların iş kodlarına erişmek için instance oluşturulması
user_service = UserService(user_dal=MemoryUserDal())
eser_service = EserService(eser_dal=MemoryEserDal())
sergi_service = SergiService(sergi_dal=MemorySergiDal())


# login yapan kişinin kim olduğunu bilmek için flask-login modülünün verdiği fonksiyon
@login_manager.user_loader
def load_user(user_id):
    user = user_service.get_by_id(int(user_id))
    if user:
        return user
    else:
        return None

# sayfaya get isteği gelirse ilgili html sayfasına yönlendirme ve
# post istediği gelirse ilgili verilerin hafızadakilerle karşılaştırılıp uygunsa ana sayfaya yönlendirilmesi
@app.route('/login', methods=['POST', 'GET'])
def login():
    print(len(user_service.get_all()))
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = [user for user in user_service.get_all() if username == user.kullanıcı_adi]
        if not user:
            return render_template('login.html', info='Kullanıcıadı hatalı!')
        else:
            user = user[0]
            if user.kullanıcı_sifre != password:
                return render_template('login.html', info='Şifre hatalı!')
            else:
                login_user(user)

                return redirect(url_for("home"))
    else:
        return render_template('login.html')


# çıkış yapma fonksiyonu
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


# anasayfa (kök dizin)
@app.route('/')
def hello_world():
    return redirect(url_for("home"))


# anasayfa
@app.route('/home')
def home():
    return render_template("test.html")


# ESERLER ile ilgili sayfalar

# bütün eserlerin listelendiği sayfa
@app.route('/eserler')
def get_all_eserler():
    eser_list = eser_service.get_all()
    return render_template("eserler.html", eser_list=eser_list)


# ilgili eserin listelendiği sayfa
@app.route('/eser/id/<int:id>')
def get_eser(id):
    eser = eser_service.get_by_id(id)
    return render_template("eser.html", eser=eser)


# sayfaya get isteği gelirse ilgili html sayfasına yönlendirme ve
# post istediği gelirse ilgili verilerin formdan alınıp uygunsa hafızaya eklenmesi ve ilgili eserin detay sayfasına yönlendirme
@app.route('/add/eser', methods=['POST', 'GET'])
@login_required
def add_eser():
    eser_form = EserForm()
    if eser_form.validate_on_submit():
        eser = get_eser_fields(eser_form)
        eser_service.add(eser)
        return redirect(url_for("get_eser", id=eser.eser_id))
    else:
        return render_template("add_eser.html", form=eser_form)


# sayfaya get isteği gelirse ilgili verilerin html sayfasında dolu olarak gelmesi  ve
# post istediği gelirse ilgili verilerin formdan alınıp uygunsa hafızada güncellenmesi ve ilgili eserin detay sayfasına yönlendirme
@app.route('/edit/eser/<int:id>', methods=['POST', 'GET'])
@login_required
def edit_eser(id):
    eser_form = EserForm()
    if eser_form.validate_on_submit():
        eser = get_sergi_fields(eser_form)
        eser_service.add(eser)
        eser_service.update(eser)
        return redirect(url_for("get_eser", id=eser.eser_id))
    else:
        eser = eser_service.get_by_id(id)
        fill_eser_fields(eser_form, eser)
        return render_template("edit_eser.html", eser=eser, form=eser_form)


# fonksiyon çağrıldığında ilgili eserin hafızadan silinmesi
@app.route("/delete/eser/<int:id>")
@login_required
def delete_eser(id):
    eser = eser_service.get_by_id(id)
    eser_service.delete(eser)
    sergi_service.delete_eser_from_sergi(eser_to_delete=eser)
    return redirect(url_for("get_all_eserler"))


# SERGİ ile ilgili sayfalar


# bütün sergilerin listelendiği sayfa
@app.route('/sergiler')
def get_all_sergiler():
    sergi_list = sergi_service.get_all()
    return render_template("sergiler.html", sergi_list=sergi_list)


# ilgili serginin listelendiği sayfa
@app.route('/sergi/id/<int:id>')
def get_sergi(id):
    sergi = sergi_service.get_by_id(id)
    return render_template("sergi.html", sergi=sergi)



# sayfaya get isteği gelirse ilgili html sayfasına yönlendirme ve
# post istediği gelirse ilgili verilerin formdan alınıp uygunsa hafızaya eklenmesi ve ilgili serginin detay sayfasına yönlendirme
@app.route('/add/sergi', methods=['POST', 'GET'])
@login_required
def add_sergi():
    sergi_form = SergiForm()
    sergi_form.sergideki_eserler.choices = [(eser.eser_id, eser.eser_adi) for eser in eser_service.get_all()]
    if sergi_form.validate_on_submit():
        sergi = get_sergi_fields(sergi_form, eser_service)
        sergi_service.add(sergi)
        return redirect(url_for("get_sergi", id=sergi.sergi_id))
    else:
        return render_template("add_sergi.html", form=sergi_form)



# sayfaya get isteği gelirse ilgili verilerin html sayfasında dolu olarak gelmesi  ve
# post istediği gelirse ilgili verilerin formdan alınıp uygunsa hafızada güncellenmesi ve ilgili serginin detay sayfasına yönlendirme
@app.route('/edit/sergi/<int:id>', methods=['POST', 'GET'])
@login_required
def edit_sergi(id):
    sergi_form = SergiForm()
    sergi_form.sergideki_eserler.choices = [(eser.eser_id, eser.eser_adi) for eser in eser_service.get_all()]
    if sergi_form.is_submitted():
        sergi = get_sergi_fields(sergi_form, eser_service)
        sergi_service.update(sergi)
        return redirect(url_for("get_sergi", id=sergi.sergi_id))
    else:
        sergi = sergi_service.get_by_id(id)
        fill_sergi_fields(sergi_form, sergi)
        return render_template("edit_sergi.html", form=sergi_form, sergi=sergi)


# fonksiyon çağrıldığında ilgili serginin hafızadan silinmesi
@app.route("/delete/sergi/<int:id>")
@login_required
def delete_sergi(id):
    sergi = sergi_service.get_by_id(id)
    sergi_service.delete(sergi)
    return redirect(url_for("get_all_sergiler"))


# app.py çalışırsa app çalıştırılacak
if __name__ == "__main__":
    app.run(debug=True)
