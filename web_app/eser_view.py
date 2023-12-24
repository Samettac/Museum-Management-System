from entity import Eser

# post isteği atıldığında eserle ilgili form alanlarınındaki veriyi alıp Eser öğesi olarak döndürür
def get_eser_fields(eser_form_param) -> Eser:
    eser_form = eser_form_param
    eser_id = eser_form.eser_id.data
    eser_adi = eser_form.eser_adi.data
    eser_yazar = eser_form.eser_yazari.data
    eser_tarihi = eser_form.eser_tarihi.data
    eser_aciklama = eser_form.eser_aciklama.data
    return Eser(eser_id=eser_id, eser_adi=eser_adi, eser_yazari=eser_yazar, eser_tarihi=eser_tarihi,
                eser_aciklama=eser_aciklama)

# verilen eser formunun alanlarını verilen eser verisiyle doldurur
def fill_eser_fields(eser_form_param, eser: Eser):
    eser_form = eser_form_param
    eser_form.eser_id.data = eser.eser_id
    eser_form.eser_adi.data = eser.eser_adi
    eser_form.eser_yazari.data = eser.eser_yazari
    eser_form.eser_tarihi.data = eser.eser_tarihi
    eser_form.eser_aciklama.data = eser.eser_aciklama
