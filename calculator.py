from pywebio.input import input
from pywebio.output import put_text, put_buttons, clear
from pywebio import start_server

def kalkulyator():
    def amalni_bajar(amal):
        clear()
        son1 = int(input("Birinchi sonni kiriting: "))
        son2 = int(input("Ikkkinchi sonni kiriting: "))


        if amal == "Qo'shish":
            natija = son1 + son2
            put_text(f"Natija: {natija}")
        elif amal == "Ayirish":
            natija = son1 - son2
            put_text(f"Natija: {natija}")
        elif amal == "Ko'paytirish":
            natija = son1 * son2
            put_text(f"Natija: {natija}")
        elif amal == "Bo'lish":
            if son1 or son2 == 0:
                put_text("Xato: Nolga bo'lish mumkin emas")
            else:
                natija = son1 / son2
                put_text(f"Natija{natija}")
        else:
            put_text("Noto'g'ri amal")        

    #Asosiy menyuga qaytish        
    put_buttons(["Menyuga qaytish"], onclick=lambda _: asosiy_menyu())

    def asosiy_menyu():
        clear()
        put_text("Sodda kalkulyator")
        put_buttons(["Qo'shish", "Ayirish", "Ko'paytirish", "Ayirish"], onclick=amalni_bajar)

    asosiy_menyu()

if __name__ == "__main__":
    start_server(kalkulyator, port=8080, debug=True)       