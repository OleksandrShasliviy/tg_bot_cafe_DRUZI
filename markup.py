from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Корзини для кожного користувача
basket = {}

def get_basket_text(basket):
    if not basket:
        return "У вашій корзині поки немає жодних позицій."
    items = "\n".join(basket)
    return f"У вашій корзині наразі наступні позиції:\n{items}"

# Функція додавання товару до корзини для конкретного користувача
def add_to_basket(user_id, item):
    if user_id not in basket:
        basket[user_id] = []
    basket[user_id].append(item)
    return "Товар успішно доданий до корзини."

# Функція очищення корзини для конкретного користувача
def clear_basket(user_id):
    if user_id in basket:
        basket[user_id].clear()
    return "Корзина успішно очищена."




btnMain = KeyboardButton('Початкова сторінка')
btnBasket = KeyboardButton('Корзина')


# -----Main Menu----

btnMenu = KeyboardButton('Головне меню')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMenu,btnBasket)


btnStolik = KeyboardButton('Виберіть ваш столик')
basketMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStolik, btnMain)
# друге меню корзини
btnClearBasket = KeyboardButton('Очистити корзину')
btnVisionBasket = KeyboardButton('Переглянути корзину')
btnZakaz = KeyboardButton('Відправити замовлення офіціанту')
basketMenu3 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnClearBasket,btnVisionBasket,btnZakaz, btnMain)

#меню столів
btnStil1 = KeyboardButton('Стіл № 1')
btnStil2 = KeyboardButton('Стіл № 2')
btnStil3 = KeyboardButton('Стіл № 3')
btnStil4 = KeyboardButton('Стіл № 4')
btnStil5 = KeyboardButton('Стіл № 5')
btnStil6 = KeyboardButton('Стіл № 6')
btnStil7 = KeyboardButton('Стіл № 7')
btnStil8 = KeyboardButton('Стіл № 8')
btnStil9 = KeyboardButton('Стіл № 9')
btnStil10 = KeyboardButton('Стіл № 10')
stilMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStil1,btnStil2,btnStil3,btnStil4,btnStil5,btnStil6,
                                                         btnStil7,btnStil8,btnStil9,btnStil10,btnMain)










# ______Main menu______ кномки головного меню
btnKruasan = KeyboardButton('Меню круасанів')
btnPizza = KeyboardButton('Меню піц')
btnPasta = KeyboardButton('Меню із пастами')
btnSteyk = KeyboardButton('Меню із стейками')
btnFire = KeyboardButton('Меню із гарячцми стравами')
btnSalat = KeyboardButton('Меню із салатами')
btnSneck = KeyboardButton('Меню із снеками')
btnCrap = KeyboardButton('Меню із млинцями')
btnDessert = KeyboardButton('Меню із десертами')
btnCocktail = KeyboardButton('Меню із коктейлями')
btnShot = KeyboardButton('Меню із шотами')
btnAlko = KeyboardButton('Меню із алкоголем')
btnBear = KeyboardButton('Меню із пивом')
btnDrinck = KeyboardButton('Меню із холодними напоями')


# Submenu buttons for 'Меню із холодними напоями'
btnPepsi = KeyboardButton('PePsi - 330 ml - 25')
btnCocaCola = KeyboardButton('COCA-COLA - 250 ml - 25')
btnSchweppes = KeyboardButton('ШВЕПС - 330 ml - 25')
btnBonaqua = KeyboardButton('БОНАКВА - 500 ml - 30')
btnLitrVoda = KeyboardButton('COLA/FANTA/SPRITE-1l-45')
btnMonstr = KeyboardButton('MONSTER ENERGY - 330 ml - 60')
btnSock = KeyboardButton('CІК -220ml/430ml/1l -30/40/65')


coldDrinksMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPepsi, btnCocaCola,btnSchweppes,btnBonaqua,
                                                               btnLitrVoda,btnMonstr,btnSock).add(btnMain)
#кдобавлення кнопок головного меню
GlovMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnKruasan,btnPizza,btnPasta,btnSteyk,btnFire,btnSalat,
                                                         btnSneck,btnCrap,btnDessert,btnCocktail,btnShot,
                                                         btnAlko,btnBear,btnDrinck,btnMain)

#добавляєм підменю і кнопки до меню круасанів
btnCRHamGR = KeyboardButton('З ХАМОНОМ ТА ГРУШЕЮ - 120')
btnCRAiL = KeyboardButton('З АВОКАДО ІЗ ЛОСОСЕМ - 120')
btnCRYaiSchocled = KeyboardButton('З ЯЙЦЕМ ТА БЕКОНОМ - 120')
btnCRBananaSchocled = KeyboardButton('З БАНАНОМ ТА ШОКОЛАДОМ - 100')

cruasanMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCRHamGR,btnCRAiL,btnCRYaiSchocled,btnCRBananaSchocled).add(btnMain)

#меню піц
btnMargarita = KeyboardButton('МАРГАРИТА 100/130/160 -30/35/40 см')
btn4Sira = KeyboardButton('4 СИРА 140/180/220 -30/35/40 см')
btnMasna = KeyboardButton("М'ЯСНА 140/180/220 -30/35/40 см")
btnTseshar = KeyboardButton('ЦЕЗАР 140/180/220 -30/35/40 см')
btnMore = KeyboardButton('МОРСЬКА 160/200/250 -30/35/40 см')
btnSalami = KeyboardButton('САЛЯМІ 120/160/200 -30/35/40 см')
btnGrisDorblu = KeyboardButton('З ГРУШЕЮ І ДОРБЛЮ 120/160/200 -30/35/40 см')
btnGavai = KeyboardButton('ГАВАЙСЬКА 120/160/200 -30/35/40 см')

PizzaMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMargarita,btn4Sira,btnMasna,btnTseshar,btnMore,btnSalami,btnGrisDorblu,
                                                          btnGavai,).add(btnMain)
#pasta
btnPastaKarbonara = KeyboardButton('КАРБОНАРА - 120')
btnPastaFettu4ini = KeyboardButton('ФЕТТУЧІНІ - 120')
btnPastazKrivetkoyu = KeyboardButton('ПАСТА З КРИВЕТКОЮ - 150')

PasstaMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPastaKarbonara,btnPastaFettu4ini,
                                                           btnPastazKrivetkoyu).add(btnMain)
#steyk
btnSteykKura = KeyboardButton('КУРЯЧИЙ У ВЕРШКОВОМУ СОУСІ - 60')
btnSteykSvinina = KeyboardButton('СТЕЙК ЗІ СВИНИНИ - 90')
btnSteykGovyada = KeyboardButton('ЯЛОВИЧИЙ СТЕЙК - 120')

SteykMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSteykKura,btnSteykSvinina,btnSteykGovyada).add(btnMain)


#firefud
btnFireKur = KeyboardButton('ПАТЕЛЬНЯ З КУРКОЮ - 160')
btnFireKurisYaytso = KeyboardButton('ПАТЕЛЬНЯ З КУРКОЮ ТА ЯЙЦЕМ - 170')
btnFireBavarska = KeyboardButton('ПАТЕЛЬНЯ БАВАРСЬКА - 170')
btnFireKremSup = KeyboardButton('КРЕМ СУП ДНЯ - 120')

FireMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFireKur,btnFireKurisYaytso,btnFireBavarska,
                                                         btnFireKremSup).add(btnMain)

#Salatmenu
btnSalatGretskiy = KeyboardButton('ГРЕЦЬКИЙ - 120')
btnSalatTsezar = KeyboardButton('ЦЕЗАР З КУРКОЮ/ЛОСОСЕМ - 180')
btnSalatzKrivetkoy = KeyboardButton('САЛАТ З КРЕВЕТКАМИ - 180')
btnSalatDruzi = KeyboardButton('САЛАТ DRUZI')

SalatMenu =ReplyKeyboardMarkup(resize_keyboard=True).add(btnSalatGretskiy,btnSalatTsezar,btnSalatzKrivetkoy,
                                                         btnSalatDruzi).add(btnMain)

#snek
btnFri = KeyboardButton('КАРТОПЛЯ ФРІ - 40')
btnNagets = KeyboardButton('НАГЕТСИ - 50')
btnTsibulaKiltsa = KeyboardButton('ЦИБУЛЕВІ КІЛЬЦЯ - 50')
btnChisKulka = KeyboardButton('СИРНІ КУЛЬКИ - 50')
btnChisPalka = KeyboardButton('СИРНІ ПАЛИЧКИ - 50')
btn4ikenStrips = KeyboardButton('ЧІКЕН СТРІПС - 60')
btnKriltsaMexi = KeyboardButton('КРИЛЬЦЯ МЕХІ - 60')
btnBo4onokFila = KeyboardButton('БОЧОНОЧКИ ФІЛАДЕЛЬФІЯ - 70')
btnKingKrivetka = KeyboardButton('КОРОЛІВСЬКІ КРИВЕТКИ - 100')
btnSous = KeyboardButton('СОУС (ДОДАТКОВО) - 15')
btnBrusketMix = KeyboardButton('БРУСКЕТИ МІКС - 120')

SneckMenu =ReplyKeyboardMarkup(resize_keyboard=True).add(btnFri,btnNagets,btnTsibulaKiltsa,btnChisKulka,
                                                         btnChisPalka,btn4ikenStrips,btnKriltsaMexi,
                                                         btnBo4onokFila,btnKingKrivetka,btnSous,
                                                         btnBrusketMix).add(btnMain)

#mluntsi
btnNutelaBlin = KeyboardButton('NUTELLA BANANA BLIN - 150')
btnChesarBlin = KeyboardButton('ЦЕЗАР BLIN -150')
btnCheeseBlin = KeyboardButton('CHEESE BLIN - 150')
btnFishBlin = KeyboardButton('FISH BLIN - 150')
btnHanterBlin = KeyboardButton('МІСЛІВЕЦЬ BLIN - 150')
btnPorkBlin = KeyboardButton('PORK BLIN - 150')
btnChikenBlin = KeyboardButton('CHICKEN BLIN - 150')
btnShinkaBlin = KeyboardButton('ШИНКА BLIN - 150')

BlinMenu =ReplyKeyboardMarkup(resize_keyboard=True).add(btnNutelaBlin,btnChesarBlin,btnCheeseBlin,btnFishBlin,
                                                        btnHanterBlin,btnPorkBlin,btnChikenBlin,btnShinkaBlin).add(btnMain)

#desert
btnSirnick = KeyboardButton('СИРНИКИ - 120')
btnBelgVafla = KeyboardButton('БЕЛЬГІЙСЬКІ ВАФЛІ - 120')
btnFondan = KeyboardButton('ФОНДАН - 120')

DesertMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSirnick,btnBelgVafla,btnFondan).add(btnMain)

#Ckokteil
btnCocktOushen = KeyboardButton('ОУШЕН - 120')
btnCocktPaloma = KeyboardButton('ПАЛОМА - 120')
btnCocktGetsbi = KeyboardButton('ГЕТСБІ - 120')
btnCocktDgintonick = KeyboardButton('ДЖИНТОНІК - 120')
btnCoctTomckolins = KeyboardButton('ТОМКОЛІНС - 120')
btnCoctAperol = KeyboardButton('АПЕРОЛЬШПРИЦ - 120')
btnCoctNegroni = KeyboardButton('НЕГРОНІ - 120')
btnCoctBritni = KeyboardButton('БРІТНІ - 120')
btnCocktGrizli = KeyboardButton('ГРІЗЛІ - 120')
btnCocktLong = KeyboardButton('ЛОНГАЙЛЕНД - 120')


CkocteilMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCocktOushen,btnCocktPaloma,btnCocktGetsbi,
                                                             btnCocktDgintonick,btnCoctTomckolins,btnCoctAperol,
                                                             btnCoctNegroni,btnCoctBritni,btnCocktGrizli,
                                                             btnCocktLong).add(btnMain)

#shot
btnShotB_52 = KeyboardButton('B-52 - 60')
btnShotHirosima = KeyboardButton('ХІРОСІМА - 60')
btnShotMeks = KeyboardButton('ЗЕЛЕНИЙ МЕКС. - 60')
btnShotBmw = KeyboardButton('BMW - 60')
btnShotAudi = KeyboardButton('AUDI - 60')
btnShotDuza = KeyboardButton('Медуза - 60')
btnShotVoda = KeyboardButton('COLA/FANTA/SPRITE - 60')

ShotMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnShotB_52,btnShotHirosima,btnShotMeks,
                                                           btnShotBmw,btnShotAudi,btnShotDuza,btnShotVoda).add(btnMain)


#alkogol

btnAlkoKonyak = KeyboardButton('КОНЬЯК - 35/40/45')
btnAlkoFinka = KeyboardButton('ГОРІЛКА FINLANDIA - 50')
btnAlkoDjin = KeyboardButton('ДЖИН - 55')
btnAlkoSambuka = KeyboardButton('САМБУКА - 55')
btnAlkoRom = KeyboardButton('РОМ - 55')
btnAlkoTekila = KeyboardButton('ТЕКІЛА - 60/70')
btnAlkoPasport = KeyboardButton('ВІСКІ PASSPORT SCOTCH - 40')
btnAlkoBells = KeyboardButton('ВІСКІ BELLS - 55')
btnAlkoJemison = KeyboardButton('ВІСКІ JAMESON - 65')
btnAlkoJack = KeyboardButton('ВІСКІ JACK DANIELS')

AlkoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAlkoKonyak,btnAlkoFinka,btnAlkoDjin,btnAlkoSambuka,
                                                         btnAlkoRom,btnAlkoTekila,btnAlkoPasport,btnAlkoBells,
                                                         btnAlkoJemison,btnAlkoJack).add(btnMain)
#Pivo

btnPivo1715 = KeyboardButton('1715/500ml - 40')
btnPivoTuborg = KeyboardButton('TUBORG/500ml - 50')
btnPivoBud = KeyboardButton('BUD/500ml - 50')
btnPivoGarage = KeyboardButton('GARAGE/500ml - 50')
btnPivoSomers = KeyboardButton('SOMERSBY/500ml - 50')
btnPivoBlanc = KeyboardButton('BLANC/500ml - 50')
btnPivoStella = KeyboardButton('STELLA/500ml - 50')
btnPivoCorona = KeyboardButton('CORONA EXTRA/300ml - 70')
btnPivoHugard = KeyboardButton('HOEGAARDEN/500ml - 50')

PivkoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPivo1715,btnPivoTuborg,btnPivoBud,btnPivoGarage,
                                                          btnPivoSomers,btnPivoBlanc,btnPivoStella,
                                                          btnPivoCorona,btnPivoHugard).add(btnMain)
