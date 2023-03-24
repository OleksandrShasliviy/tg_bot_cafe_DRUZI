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

    elif message.text =='Кальянне меню':
        await bot.send_message(message.from_user.id, 'Кальянне меню', reply_markup=nav.DymMenu)

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
        nav.add_to_basket(message.from_user.id, 'PePsi - 330 ml - 25')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'COCA-COLA - 250 ml - 25':
        nav.add_to_basket(message.from_user.id, 'COCA-COLA - 250 ml - 25')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    elif message.text == 'ШВЕПС - 330 ml - 25':
        nav.add_to_basket(message.from_user.id, 'ШВЕПС - 330 ml - 25')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'БОНАКВА - 500 ml - 30':
        nav.add_to_basket(message.from_user.id, 'БОНАКВА - 500 ml - 30')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'COLA/FANTA/SPRITE-1l-45':
        nav.add_to_basket(message.from_user.id, 'COLA/FANTA/SPRITE-1l-45')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'MONSTER ENERGY - 330 ml - 60':
        nav.add_to_basket(message.from_user.id, 'MONSTER ENERGY - 330 ml - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'CІК -220ml/430ml/1l -30/40/65':
        nav.add_to_basket(message.from_user.id, 'CІК -220ml/430ml/1l -30/40/65')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)



    #pasta dobavka

    elif message.text == 'КАРБОНАРА - 120':
        nav.add_to_basket(message.from_user.id, 'КАРБОНАРА - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ФЕТТУЧІНІ - 120':
        nav.add_to_basket(message.from_user.id, 'ФЕТТУЧІНІ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ПАСТА З КРИВЕТКОЮ - 150':
        nav.add_to_basket(message.from_user.id, 'ПАСТА З КРИВЕТКОЮ - 150')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)



    #steyk

    elif message.text == 'КУРЯЧИЙ У ВЕРШКОВОМУ СОУСІ - 60':
        nav.add_to_basket(message.from_user.id, 'КУРЯЧИЙ У ВЕРШКОВОМУ СОУСІ - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'СТЕЙК ЗІ СВИНИНИ - 90':
        nav.add_to_basket(message.from_user.id, 'СТЕЙК ЗІ СВИНИНИ - 90')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'СТЕЙК ЗІ СВИНИНИ - 90':
        nav.add_to_basket(message.from_user.id, 'СТЕЙК ЗІ СВИНИНИ - 90')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ЯЛОВИЧИЙ СТЕЙК - 120':
        nav.add_to_basket(message.from_user.id, 'ЯЛОВИЧИЙ СТЕЙК - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    #Firemenu

    elif message.text == 'ПАТЕЛЬНЯ З КУРКОЮ - 160':
        nav.add_to_basket(message.from_user.id, 'ПАТЕЛЬНЯ З КУРКОЮ - 160')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ПАТЕЛЬНЯ З КУРКОЮ ТА ЯЙЦЕМ - 170':
        nav.add_to_basket(message.from_user.id, 'ПАТЕЛЬНЯ З КУРКОЮ ТА ЯЙЦЕМ - 170')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ПАТЕЛЬНЯ БАВАРСЬКА - 170':
        nav.add_to_basket(message.from_user.id, 'ПАТЕЛЬНЯ БАВАРСЬКА - 170')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'КРЕМ СУП ДНЯ - 120':
        nav.add_to_basket(message.from_user.id, 'КРЕМ СУП ДНЯ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    #salatmenu
    elif message.text == 'ГРЕЦЬКИЙ - 120':
        nav.add_to_basket(message.from_user.id, 'ГРЕЦЬКИЙ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ЦЕЗАР З КУРКОЮ/ЛОСОСЕМ - 180':
        nav.add_to_basket(message.from_user.id, 'ЦЕЗАР З КУРКОЮ/ЛОСОСЕМ - 180')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'САЛАТ З КРЕВЕТКАМИ - 180':
        nav.add_to_basket(message.from_user.id, 'САЛАТ З КРЕВЕТКАМИ - 180')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'САЛАТ DRUZI':
        nav.add_to_basket(message.from_user.id, 'САЛАТ DRUZI')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    #sneckmenu
    elif message.text == 'КАРТОПЛЯ ФРІ - 40':
        nav.add_to_basket(message.from_user.id, 'КАРТОПЛЯ ФРІ - 40')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'НАГЕТСИ - 50':
        nav.add_to_basket(message.from_user.id, 'НАГЕТСИ - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ЦИБУЛЕВІ КІЛЬЦЯ - 50':
        nav.add_to_basket(message.from_user.id, 'ЦИБУЛЕВІ КІЛЬЦЯ - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'СИРНІ КУЛЬКИ - 50':
        nav.add_to_basket(message.from_user.id, 'СИРНІ КУЛЬКИ - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'СИРНІ ПАЛИЧКИ - 50':
        nav.add_to_basket(message.from_user.id, 'СИРНІ ПАЛИЧКИ - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ЧІКЕН СТРІПС - 60':
        nav.add_to_basket(message.from_user.id, 'ЧІКЕН СТРІПС - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'КРИЛЬЦЯ МЕХІ - 60':
        nav.add_to_basket(message.from_user.id, 'КРИЛЬЦЯ МЕХІ - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'БОЧОНОЧКИ ФІЛАДЕЛЬФІЯ - 70':
        nav.add_to_basket(message.from_user.id, 'БОЧОНОЧКИ ФІЛАДЕЛЬФІЯ - 70')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'КОРОЛІВСЬКІ КРИВЕТКИ - 100':
        nav.add_to_basket(message.from_user.id, 'КОРОЛІВСЬКІ КРИВЕТКИ - 100')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'СОУС (ДОДАТКОВО) - 15':
        nav.add_to_basket(message.from_user.id, 'СОУС (ДОДАТКОВО) - 15')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'БРУСКЕТИ МІКС - 120':
        nav.add_to_basket(message.from_user.id, 'БРУСКЕТИ МІКС - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    #blinmenu
    elif message.text == 'NUTELLA BANANA BLIN - 150':
        nav.add_to_basket(message.from_user.id, 'NUTELLA BANANA BLIN - 150')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ЦЕЗАР BLIN -150':
        nav.add_to_basket(message.from_user.id, 'ЦЕЗАР BLIN -150')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'CHEESE BLIN - 150':
        nav.add_to_basket(message.from_user.id, 'CHEESE BLIN - 150')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'FISH BLIN - 150':
        nav.add_to_basket(message.from_user.id, 'FISH BLIN - 150')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'МІСЛІВЕЦЬ BLIN - 150':
        nav.add_to_basket(message.from_user.id, 'МІСЛІВЕЦЬ BLIN - 150')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'PORK BLIN - 150':
        nav.add_to_basket(message.from_user.id, 'PORK BLIN - 150')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'CHICKEN BLIN - 150':
        nav.add_to_basket(message.from_user.id, 'CHICKEN BLIN - 150')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ШИНКА BLIN - 150':
        nav.add_to_basket(message.from_user.id, 'ШИНКА BLIN - 150')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    #desert

    elif message.text == 'СИРНИКИ - 120':
        nav.add_to_basket(message.from_user.id, 'СИРНИКИ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'БЕЛЬГІЙСЬКІ ВАФЛІ - 120':
        nav.add_to_basket(message.from_user.id, 'БЕЛЬГІЙСЬКІ ВАФЛІ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ФОНДАН - 120':
        nav.add_to_basket(message.from_user.id, 'ФОНДАН - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    #Cockteil
    elif message.text == 'ОУШЕН - 120':
        nav.add_to_basket(message.from_user.id, 'ОУШЕН - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ПАЛОМА - 120':
        nav.add_to_basket(message.from_user.id, 'ПАЛОМА - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ГЕТСБІ - 120':
        nav.add_to_basket(message.from_user.id, 'ГЕТСБІ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ДЖИНТОНІК - 120':
        nav.add_to_basket(message.from_user.id, 'ДЖИНТОНІК - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ТОМКОЛІНС - 120':
        nav.add_to_basket(message.from_user.id, 'ТОМКОЛІНС - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'АПЕРОЛЬШПРИЦ - 120':
        nav.add_to_basket(message.from_user.id, 'АПЕРОЛЬШПРИЦ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'НЕГРОНІ - 120':
        nav.add_to_basket(message.from_user.id, 'НЕГРОНІ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'БРІТНІ - 120':
        nav.add_to_basket(message.from_user.id, 'БРІТНІ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    elif message.text == 'ГРІЗЛІ - 120':
        nav.add_to_basket(message.from_user.id, 'ГРІЗЛІ - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    elif message.text == 'ЛОНГАЙЛЕНД - 120':
        nav.add_to_basket(message.from_user.id, 'ЛОНГАЙЛЕНД - 120')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)



    #Shot
    elif message.text == 'B-52 - 60':
        nav.add_to_basket(message.from_user.id, 'B-52 - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ХІРОСІМА - 60':
        nav.add_to_basket(message.from_user.id, 'ХІРОСІМА - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ЗЕЛЕНИЙ МЕКС. - 60':
        nav.add_to_basket(message.from_user.id, 'ЗЕЛЕНИЙ МЕКС. - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'BMW - 60':
        nav.add_to_basket(message.from_user.id, 'BMW - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    elif message.text == 'AUDI - 60':
        nav.add_to_basket(message.from_user.id, 'AUDI - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'Медуза - 60':
        nav.add_to_basket(message.from_user.id, 'Медуза - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'COLA/FANTA/SPRITE - 60':
        nav.add_to_basket(message.from_user.id, 'COLA/FANTA/SPRITE - 60')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    #alko

    elif message.text == 'КОНЬЯК - 35/40/45':
        nav.add_to_basket(message.from_user.id, 'КОНЬЯК - 35/40/45')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ГОРІЛКА FINLANDIA - 50':
        nav.add_to_basket(message.from_user.id, 'ГОРІЛКА FINLANDIA - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    elif message.text == 'ДЖИН - 55':
        nav.add_to_basket(message.from_user.id, 'ДЖИН - 55')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'САМБУКА - 55':
        nav.add_to_basket(message.from_user.id, 'САМБУКА - 55')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'РОМ - 55':
        nav.add_to_basket(message.from_user.id, 'РОМ - 55')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ТЕКІЛА - 60/70':
        nav.add_to_basket(message.from_user.id, 'ТЕКІЛА - 60/70')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'РВІСКІ PASSPORT SCOTCH - 40':
        nav.add_to_basket(message.from_user.id, 'ВІСКІ PASSPORT SCOTCH - 40')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ВІСКІ BELLS - 55':
        nav.add_to_basket(message.from_user.id, 'ВІСКІ BELLS - 55')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'ВІСКІ JAMESON - 65':
        nav.add_to_basket(message.from_user.id, 'ВІСКІ JAMESON - 65')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    elif message.text == 'ВІСКІ JACK DANIELS':
        nav.add_to_basket(message.from_user.id, 'ВІСКІ JACK DANIELS')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)



    #Pivko

    elif message.text == '1715/500ml - 40':
        nav.add_to_basket(message.from_user.id, '1715/500ml - 40')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'TUBORG/500ml - 50':
        nav.add_to_basket(message.from_user.id, 'TUBORG/500ml - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'BUD/500ml - 50':
        nav.add_to_basket(message.from_user.id, 'BUD/500ml - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'GARAGE/500ml - 50':
        nav.add_to_basket(message.from_user.id, 'GARAGE/500ml - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'SOMERSBY/500ml - 50':
        nav.add_to_basket(message.from_user.id, 'SOMERSBY/500ml - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'BLANC/500ml - 50':
        nav.add_to_basket(message.from_user.id, 'BLANC/500ml - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'STELLA/500ml - 50':
        nav.add_to_basket(message.from_user.id, 'STELLA/500ml - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'CORONA EXTRA/300ml - 70':
        nav.add_to_basket(message.from_user.id, 'CORONA EXTRA/300ml - 70')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)

    elif message.text == 'HOEGAARDEN/500ml - 50':
        nav.add_to_basket(message.from_user.id, 'HOEGAARDEN/500ml - 50')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)


    #kalian

    elif message.text == 'Кальянного майстра в корзину':
        nav.add_to_basket(message.from_user.id, 'Кальянного майстра в корзину')
        basket_text = nav.get_basket_text(nav.basket.get(message.from_user.id))
        await bot.send_message(message.from_user.id, basket_text)



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






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
