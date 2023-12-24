from entity import  Sergi

# post isteği atıldığında sergiyle ilgili form alanlarınındaki veriyi alıp Sergi öğesi olarak döndürür
def get_sergi_fields(sergi_form_param, eser_service) -> Sergi:
    sergi_form = sergi_form_param
    sergi_id = int(sergi_form.sergi_id.data)
    sergi_adi = sergi_form.sergi_adi.data
    sergi_tipi = sergi_form.sergi_tipi.data
    sergi_tarihi = sergi_form.sergi_tarihi.data
    sergi_aciklama = sergi_form.sergi_aciklama.data
    sergideki_eserler = sergi_form.sergideki_eserler.data
    sergideki_eserler = [eser_service.get_by_id(id) for id in sergideki_eserler]
    return Sergi(sergi_id=sergi_id, sergi_adi=sergi_adi, sergi_tipi=sergi_tipi, sergi_tarihi=sergi_tarihi,
                                sergi_aciklama=sergi_aciklama, sergideki_eserler=sergideki_eserler)


# verilen sergi formunun alanlarını verilen sergi verisiyle doldurur
def fill_sergi_fields(sergi_form_param, sergi: Sergi):
    sergi_form = sergi_form_param
    sergi_form.sergi_id.data = sergi.sergi_id
    sergi_form.sergi_adi.data = sergi.sergi_adi
    sergi_form.sergi_tipi.data = sergi.sergi_tipi
    sergi_form.sergi_tarihi.data = sergi.sergi_tarihi
    sergi_form.sergi_aciklama.data = sergi.sergi_aciklama
    sergi_form.sergideki_eserler.data = [eser.eser_id for eser in sergi.sergideki_eserler]
    return sergi
