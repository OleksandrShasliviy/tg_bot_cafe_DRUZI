import logging
from aiogram import Bot, Dispatcher, executor, types
import markup as nav
import telegram




TOKEN = "6023629935:AAHxG-_5-4l1xqUwz0M15W6ZjHx3wakPKYI"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
chat_id = -1001920474173









@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Првіт {0.first_name} 😃Ласкаво просимо до нашого дружнього товариства☺️'
                                                 'Для зручності вкажи свії столик  та опріділись із меню і викликай офіціанта.'.format(message.from_user),reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    #await bot.send_message(message.from_user.id, message.text)
    if message.text =='Головне меню':
        await bot.send_message(message.from_user.id, 'Головне меню', reply_markup=nav.GlovMenu)

    elif message.text =='Початкова сторінка':
        await bot.send_message(message.from_user.id, 'Початкова сторінка', reply_markup=nav.mainMenu)

    elif message.text =='Меню із холодними напоями':
        await bot.send_message(message.from_user.id, 'Меню із холодними напоями', reply_markup=nav.coldDrinksMenu)

    elif message.text =='Меню круасанів':
        await bot.send_message(message.from_user.id, 'Меню круасанів', reply_markup=nav.cruasanMenu)

    elif message.text =='Меню піц':
        await bot.send_message(message.from_user.id, 'Меню піц', reply_markup=nav.PizzaMenu)

    elif message.text =='Меню із пастами':
        await bot.send_message(message.from_user.id, 'Меню піц', reply_markup=nav.PasstaMenu)

    elif message.text =='Меню із стейками':
        await bot.send_message(message.from_user.id, 'Меню піц', reply_markup=nav.SteykMenu)

    elif message.text =='Меню із гарячцми стравами':
        await bot.send_message(message.from_user.id, 'Меню піц', reply_markup=nav.FireMenu)

    elif message.text =='Меню із салатами':
        await bot.send_message(message.from_user.id, 'Меню піц', reply_markup=nav.SalatMenu)

    elif message.text =='Меню із снеками':
        await bot.send_message(message.from_user.id, 'Меню піц', reply_markup=nav.SneckMenu)

    elif message.text =='Меню із млинцями':
        await bot.send_message(message.from_user.id, 'Меню із млинцями', reply_markup=nav.BlinMenu)

    elif message.text =='Меню із десертами':
        await bot.send_message(message.from_user.id, 'Меню із десертами', reply_markup=nav.DesertMenu)

    elif message.text =='Меню із коктейлями':
        await bot.send_message(message.from_user.id, 'Меню із коктейлями', reply_markup=nav.CkocteilMenu)

    elif message.text =='Меню із шотами':
        await bot.send_message(message.from_user.id, 'Меню із шотами', reply_markup=nav.ShotMenuMenu)

    elif message.text =='Меню із алкоголем':
        await bot.send_message(message.from_user.id, 'Меню із алкоголем', reply_markup=nav.AlkoMenu)

    elif message.text =='Меню із пивом':
        await bot.send_message(message.from_user.id, 'Меню із пивом', reply_markup=nav.PivkoMenu)

    elif message.text =='Корзина':
        await bot.send_message(message.from_user.id, 'Корзина', reply_markup=nav.basketMenu)

    elif message.text == 'Виберіть ваш столик':
        await bot.send_message(message.from_user.id, 'Виберіть ваш столик', reply_markup=nav.stilMenu)

    elif message.text == 'Стіл № 1':
        nav.add_to_basket(message.from_user.id, 'Стіл № 1')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text,reply_markup=nav.basketMenu3)

    elif message.text == 'Стіл № 2':
        nav.add_to_basket(message.from_user.id, 'Стіл № 2')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text,reply_markup=nav.basketMenu3)

    elif message.text == 'Стіл № 3':
        nav.add_to_basket(message.from_user.id, 'Стіл № 3')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text,reply_markup=nav.basketMenu3)

    elif message.text == 'Стіл № 4':
        nav.add_to_basket(message.from_user.id, 'Стіл № 4')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text,reply_markup=nav.basketMenu3)

    elif message.text == 'Стіл № 5':
        nav.add_to_basket(message.from_user.id, 'Стіл № 5')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text,reply_markup=nav.basketMenu3)

    elif message.text == 'Стіл № 6':
        nav.add_to_basket(message.from_user.id, 'Стіл № 6')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text,reply_markup=nav.basketMenu3)

    elif message.text == 'Стіл № 7':
        nav.add_to_basket(message.from_user.id, 'Стіл № 7')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text,reply_markup=nav.basketMenu3)

    elif message.text == 'Стіл № 8':
        nav.add_to_basket(message.from_user.id, 'Стіл № 8')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text,reply_markup=nav.basketMenu3)


    elif message.text == 'Стіл № 9':
        nav.add_to_basket(message.from_user.id, 'Стіл № 9')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text, reply_markup=nav.basketMenu3)


    elif message.text == 'Стіл № 10':
        nav.add_to_basket(message.from_user.id, 'Стіл № 10')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text,reply_markup=nav.basketMenu3)


    # Перегляд корзини

    elif message.text == 'Переглянути корзину':
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    #Добавлення в корзину

    elif message.text == 'З ХАМОНОМ ТА ГРУШЕЮ - 120':
        nav.add_to_basket(message.from_user.id, 'З ХАМОНОМ ТА ГРУШЕЮ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    elif message.text == 'З ЯЙЦЕМ ТА БЕКОНОМ - 120':
        nav.add_to_basket(message.from_user.id, 'З ЯЙЦЕМ ТА БЕКОНОМ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'З АВОКАДО ІЗ ЛОСОСЕМ - 120':
        nav.add_to_basket(message.from_user.id, 'З АВОКАДО ІЗ ЛОСОСЕМ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'З БАНАНОМ ТА ШОКОЛАДОМ - 100':
        nav.add_to_basket(message.from_user.id, 'З БАНАНОМ ТА ШОКОЛАДОМ - 100')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

       #pizza
    elif message.text == 'МАРГАРИТА 100/130/160 -30/35/40 см':
        nav.add_to_basket(message.from_user.id, 'МАРГАРИТА 100/130/160 -30/35/40 см')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == '4 СИРА 140/180/220 -30/35/40 см':
        nav.add_to_basket(message.from_user.id, '4 СИРА 140/180/220 -30/35/40 см')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == "М'ЯСНА 140/180/220 -30/35/40 см":
        nav.add_to_basket(message.from_user.id, "М'ЯСНА 140/180/220 -30/35/40 см")
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ЦЕЗАР 140/180/220 -30/35/40 см':
        nav.add_to_basket(message.from_user.id, 'ЦЕЗАР 140/180/220 -30/35/40 см')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'МОРСЬКА 160/200/250 -30/35/40 см':
        nav.add_to_basket(message.from_user.id, 'МОРСЬКА 160/200/250 -30/35/40 см')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'САЛЯМІ 120/160/200 -30/35/40 см':
        nav.add_to_basket(message.from_user.id, 'САЛЯМІ 120/160/200 -30/35/40 см')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'З ГРУШЕЮ І ДОРБЛЮ 120/160/200 -30/35/40 см':
        nav.add_to_basket(message.from_user.id, 'З ГРУШЕЮ І ДОРБЛЮ 120/160/200 -30/35/40 см')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ГАВАЙСЬКА 120/160/200 -30/35/40 см':
        nav.add_to_basket(message.from_user.id, 'ГАВАЙСЬКА 120/160/200 -30/35/40 см')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    # Submenu buttons for 'Меню із холодними напоями'
    elif message.text == 'PePsi - 330 ml - 25':
        nav.basket.append('PePsi - 330 ml - 25')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'COCA-COLA - 250 ml - 25':
        nav.basket.append('COCA-COLA - 250 ml - 25 ')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ШВЕПС - 330 ml - 25':
        nav.basket.append('ШВЕПС - 330 ml - 25 ')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'БОНАКВА - 500 ml - 30':
        nav.basket.append('БОНАКВА - 500 ml - 30 ')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'COLA/FANTA/SPRITE-1l-45':
        nav.basket.append('COLA/FANTA/SPRITE-1l-45 ')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'MONSTER ENERGY - 330 ml - 60':
        nav.basket.append('MONSTER ENERGY - 330 ml - 60 ')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'CІК -220ml/430ml/1l -30/40/65':
        nav.basket.append('CІК -220ml/430ml/1l -30/40/65 ')
        await bot.send_message(message.from_user.id, nav.basket)

    #pasta dobavka
    elif message.text == 'КАРБОНАРА - 120':
        nav.basket.append('КАРБОНАРА - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ФЕТТУЧІНІ - 120':
        nav.basket.append('ФЕТТУЧІНІ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ПАСТА З КРИВЕТКОЮ - 150':
        nav.basket.append('ПАСТА З КРИВЕТКОЮ - 150')
        await bot.send_message(message.from_user.id, nav.basket)

    #steyk
    elif message.text == 'КУРЯЧИЙ У ВЕРШКОВОМУ СОУСІ - 60':
        nav.basket.append('КУРЯЧИЙ У ВЕРШКОВОМУ СОУСІ - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'СТЕЙК ЗІ СВИНИНИ - 90':
        nav.basket.append('СТЕЙК ЗІ СВИНИНИ - 90')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ЯЛОВИЧИЙ СТЕЙК - 120':
        nav.basket.append('ЯЛОВИЧИЙ СТЕЙК - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    #Firemenu
    elif message.text == 'ПАТЕЛЬНЯ З КУРКОЮ - 160':
        nav.basket.append('ПАТЕЛЬНЯ З КУРКОЮ - 160')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ПАТЕЛЬНЯ З КУРКОЮ ТА ЯЙЦЕМ - 170':
        nav.basket.append('ПАТЕЛЬНЯ З КУРКОЮ ТА ЯЙЦЕМ - 170')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ПАТЕЛЬНЯ БАВАРСЬКА - 170':
        nav.basket.append('ПАТЕЛЬНЯ БАВАРСЬКА - 170')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'КРЕМ СУП ДНЯ - 120':
        nav.basket.append('КРЕМ СУП ДНЯ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    #salatmenu
    elif message.text == 'ГРЕЦЬКИЙ - 120':
        nav.basket.append('ГРЕЦЬКИЙ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ЦЕЗАР З КУРКОЮ/ЛОСОСЕМ - 180':
        nav.basket.append('ЦЕЗАР З КУРКОЮ/ЛОСОСЕМ - 180')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'САЛАТ З КРЕВЕТКАМИ - 180':
        nav.basket.append('САЛАТ З КРЕВЕТКАМИ - 180')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'САЛАТ DRUZI':
        nav.basket.append('САЛАТ DRUZI')
        await bot.send_message(message.from_user.id, nav.basket)

    #sneckmenu
    elif message.text == 'КАРТОПЛЯ ФРІ - 40':
        nav.basket.append('КАРТОПЛЯ ФРІ - 40')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'НАГЕТСИ - 50':
        nav.basket.append('НАГЕТСИ - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ЦИБУЛЕВІ КІЛЬЦЯ - 50':
        nav.basket.append('ЦИБУЛЕВІ КІЛЬЦЯ - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'СИРНІ КУЛЬКИ - 50':
        nav.basket.append('СИРНІ КУЛЬКИ - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'СИРНІ ПАЛИЧКИ - 50':
        nav.basket.append('СИРНІ ПАЛИЧКИ - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ЧІКЕН СТРІПС - 60':
        nav.basket.append('ЧІКЕН СТРІПС - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'КРИЛЬЦЯ МЕХІ - 60':
        nav.basket.append('КРИЛЬЦЯ МЕХІ - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'БОЧОНОЧКИ ФІЛАДЕЛЬФІЯ - 70':
        nav.basket.append('БОЧОНОЧКИ ФІЛАДЕЛЬФІЯ - 70')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'КОРОЛІВСЬКІ КРИВЕТКИ - 100':
        nav.basket.append('КОРОЛІВСЬКІ КРИВЕТКИ - 100')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'СОУС (ДОДАТКОВО) - 15':
        nav.basket.append('СОУС (ДОДАТКОВО) - 15')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'БРУСКЕТИ МІКС - 120':
        nav.basket.append('БРУСКЕТИ МІКС - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    #blinmenu
    elif message.text == 'NUTELLA BANANA BLIN - 150':
        nav.basket.append('NUTELLA BANANA BLIN - 150')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ЦЕЗАР BLIN -150':
        nav.basket.append('ЦЕЗАР BLIN -150')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'CHEESE BLIN - 150':
        nav.basket.append('CHEESE BLIN - 150')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'FISH BLIN - 150':
        nav.basket.append('FISH BLIN - 150')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'МІСЛІВЕЦЬ BLIN - 150':
        nav.basket.append('МІСЛІВЕЦЬ BLIN - 150')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'PORK BLIN - 150':
        nav.basket.append('PORK BLIN - 150')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'CHICKEN BLIN - 150':
        nav.basket.append('CHICKEN BLIN - 150')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ШИНКА BLIN - 150':
        nav.basket.append('ШИНКА BLIN - 150')
        await bot.send_message(message.from_user.id, nav.basket)

    #desert
    elif message.text == 'СИРНИКИ - 120':
        nav.basket.append('СИРНИКИ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'БЕЛЬГІЙСЬКІ ВАФЛІ - 120':
        nav.basket.append('БЕЛЬГІЙСЬКІ ВАФЛІ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ФОНДАН - 120':
        nav.basket.append('ФОНДАН - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    #Cockteil
    elif message.text == 'ОУШЕН - 120':
        nav.basket.append('ОУШЕН - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ПАЛОМА - 120':
        nav.basket.append('ПАЛОМА - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ГЕТСБІ - 120':
        nav.basket.append('ГЕТСБІ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ДЖИНТОНІК - 120':
        nav.basket.append('ДЖИНТОНІК - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ТОМКОЛІНС - 120':
        nav.basket.append('ТОМКОЛІНС - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'АПЕРОЛЬШПРИЦ - 120':
        nav.basket.append('АПЕРОЛЬШПРИЦ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'НЕГРОНІ - 120':
        nav.basket.append('НЕГРОНІ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'БРІТНІ - 120':
        nav.basket.append('БРІТНІ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ГРІЗЛІ - 120':
        nav.basket.append('ГРІЗЛІ - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ЛОНГАЙЛЕНД - 120':
        nav.basket.append('ЛОНГАЙЛЕНД - 120')
        await bot.send_message(message.from_user.id, nav.basket)

    #Shot
    elif message.text == 'B-52 - 60':
        nav.basket.append('B-52 - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ХІРОСІМА - 60':
        nav.basket.append('ХІРОСІМА - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ЗЕЛЕНИЙ МЕКС. - 60':
        nav.basket.append('ЗЕЛЕНИЙ МЕКС. - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'BMW - 60':
        nav.basket.append('BMW - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'AUDI - 60':
        nav.basket.append('AUDI - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'Медуза - 60':
        nav.basket.append('Медуза - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'COLA/FANTA/SPRITE - 60':
        nav.basket.append('COLA/FANTA/SPRITE - 60')
        await bot.send_message(message.from_user.id, nav.basket)

    #alko

    elif message.text == 'КОНЬЯК - 35/40/45':
        nav.basket.append('КОНЬЯК - 35/40/45')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ГОРІЛКА FINLANDIA - 50':
        nav.basket.append('ГОРІЛКА FINLANDIA - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ДЖИН - 55':
        nav.basket.append('ДЖИН - 55')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'САМБУКА - 55':
        nav.basket.append('САМБУКА - 55')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'РОМ - 55':
        nav.basket.append('РОМ - 55')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ТЕКІЛА - 60/70':
        nav.basket.append('ТЕКІЛА - 60/70')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ВІСКІ PASSPORT SCOTCH - 40':
        nav.basket.append('ВІСКІ PASSPORT SCOTCH - 40')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ВІСКІ BELLS - 55':
        nav.basket.append('ВІСКІ BELLS - 55')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ВІСКІ JAMESON - 65':
        nav.basket.append('ВІСКІ JAMESON - 65')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'ВІСКІ JACK DANIELS':
        nav.basket.append('ВІСКІ JACK DANIELS')
        await bot.send_message(message.from_user.id, nav.basket)


    #Pivko
    elif message.text == '1715/500ml - 40':
        nav.basket.append('1715/500ml - 40')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'TUBORG/500ml - 50':
        nav.basket.append('TUBORG/500ml - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'BUD/500ml - 50':
        nav.basket.append('BUD/500ml - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'GARAGE/500ml - 50':
        nav.basket.append('GARAGE/500ml - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'SOMERSBY/500ml - 50':
        nav.basket.append('SOMERSBY/500ml - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'BLANC/500ml - 50':
        nav.basket.append('BLANC/500ml - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'STELLA/500ml - 50':
        nav.basket.append('STELLA/500ml - 50')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'CORONA EXTRA/300ml - 70':
        nav.basket.append('CORONA EXTRA/300ml - 70')
        await bot.send_message(message.from_user.id, nav.basket)

    elif message.text == 'HOEGAARDEN/500ml - 50':
        nav.basket.append('HOEGAARDEN/500ml - 50')
        await bot.send_message(message.from_user.id, nav.basket)




    # Очищення корзини
    elif message.text == 'Очистити корзину':
        nav.clear_basket(message.from_user.id)
        await bot.send_message(message.from_user.id, "Корзина успішно очищена.", reply_markup=nav.basketMenu)

    elif message.text == 'Переглянути корзину':
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)



    elif message.text == 'Відправити замовлення офіціанту':
        # send basket to user
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(chat_id, nav.get_basket_text(nav.basket.get(message.from_user.id)))

    #await bot.send_message(chat_id, message.from_user.id, basket_text)
    # basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        #await bot.send_message(chat_id, message.from_user.id, basket_text)

    # відправка фіцу
   # elif message.text == 'Відправити замовлення офіціанту':
     #   await bot.send_message(chat_id, nav.get_basket_text(nav.basket))




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
