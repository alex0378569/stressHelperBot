import datetime
import telebot
from telebot import types

bot = telebot.TeleBot('7642274915:AAHiYx8xH2nFb_RnrxSn64BfkYD-IoKyMRY', parse_mode='HTML')

stress = [
    f'<b>Стресс</b> — ответная реакция организма человека на <i>перенапряжение, негативные и позитивные эмоции</i>. \nВо время стресса организм человека вырабатывает гормон адреналин, который заставляет искать выход из проблемы.',
    f'Студенческая жизнь всегда наполнена переживаниями, напряжениями и волнительными ситуациями, которые препятствуют академической успеваемости и в перспективе ведут к <b>остановке личностного роста, психосоматическим заболеваниям.</b> \n\nСогласно данным Всемирной организации здравоохранения, около 45% всех заболеваний проявляются вследствие стрессоров. '
    f'\n\nСуществуют различные <b>симптомы</b> проявления студенческого стресса:'
    f'\n1. <code>эмоциональные</code> (ощущение общего недомогания; раздражительность; тревога; паника; растерянность; неуверенность; подавленность)'
    '\n2. <code>физиологические</code> (головная боль; перепады артериального давления; мышечное напряжение; учащенный пульс; углубление и учащение дыхания; тошнота)'
    '\n3. <code>когнитивные</code> (ухудшение памяти; рассеянность; ослабление концентрации внимания; кошмарные сновидения; неприятные воспоминания о своих или чужих провалах в прошлом; воображение негативных последствий после неудачи на экзамене)'
    '\n4. <code>поведенческие</code> (ухудшение аппетита и сна; нежелание учиться, проявляющееся в стремлении заняться любым другим делом)',
    f'В заключении стоит отметить, что <i>интенсивность</i> негативной реакции зависит не столько от вида стрессора, сколько от <i>личной значимости</i> воздействующего фактора. Кроме того, для каждого человека характерен <b>уникальный уровень волнения и страха</b>, который позволяет показать наилучшие результаты. \n\nЧтобы успешно мобилизовать свои силы на учебный процесс, одним студентам необходимо снизить уровень стресса, а другим нужно как следует «испугаться».']

reasons = f'''<b>Причины возникновения стресса</b> <u>сугубо индивидуальны</u>, но чаще всего проблемы с психологическим состоянием появляются из-за:
            \n1. Недостатка качественного сна \n(По данным Института физиологии РАО,  нормативы для 5-6 классов - 9-11 часов;  7-8 классов - 10 часов; 9 классов -  9,5 часов; 10-11 классов- 8,5-9 часов)
2. Нерационального планирования времени
3. Сомнения в своих способностях
4. Повышенной нагрузки
5. Потери интереса к учебной деятельности (выгорание)
6. Конфликтов с одноклассниками или преподавателями'''

methods = [f'''Ниже приведены <b>общие рекомендации</b>, способствующие избавлению от стрессовых ситуаций и лучшему пониманию собственных потребностей:
\n\n1. При планировании дальнейших действий разработайте <i>систему приоритетов</i>. Ответьте на вопрос: что для меня значимо в <i>настоящем</i>? \nСуществует множество техник тайм-менеджмента <b>(список дел, метод Айви Ли, метод Помодоро, 'разрежь слона на куски', 'съешь лягушку', матрица Эйзенхауэра, Канбан)</b>, каждую из которых можно неоднократно чередовать. Это поможет снизить прокрастинацию и сконцентрироваться  на  важных задачах.
\n\n2. Научитесь видеть свои пределы (после которых не сможете взять на себя доп.работу). \nПринимать решения необходимо, учитывая существующее физическое и ментальное состояние. \n\n<blockquote>Забудете про здоровый уход за организмом или будете игнорировать потребности - в дальнейшем ваш организм нанесет <b>двойной</b> удар.</blockquote> ''',
'''3. В ходе учебы не бойтесь уточнять дополнительную информацию у преподавателей или одноклассников. Существует  множество вариантов усвоения материала для разных типов личности: \n\n· визуалы (понимание через образы и наглядные примеры) \n· аудиалы (звуковое усвоение; подойдут лекции и аудиокниги) \n· кинестетики (чувственное восприятие; подойдет практика и соучастие в процессе) \n· дигиталы (понимание через анализ и вынесение четких суждений об информации). \n\nТак, например, некоторым больше подойдет обучение с одноклассниками или просмотр лекций с конспектированием, другим - запоминание через активный труд. Необходимо покопаться в себе и понять, что вам ближе.''',
'''\n\n4. Разграничивайте время для работы и отдыха. Последний компонент не менее важен - предпочитаете активный или пассивный отдых?\n Соберите стопку не просмотренных фильмов/сериалов/интересующих книг, прогуляйтесь на свежем воздухе, позанимайтесь спортом или погуглите возможные варианты хобби. <b>В момент свободы вытолкните внутреннего критика и поздравьте себя с долгожданным моментом счастья. <u>Вы этого заслужили</u>.</b>
\n\n5. В случае высокого уровня стресса пересмотрите значимость ситуации и найдите для себя причины, уменьшающие ее значимость (напомните себе о <i>кротковременности</i> сложных ситуаций; рассмотрите более приятные и желаемые мысли, <i>не особо связанные с настоящей проблемой</i>).\n Психологи также советуют отвлечься на окружающие события, заняться менее 'значимыми' хлопотами или просто помедитировать. ''']

facts = ['''<b>Медицинские факты</b>
\n 1. Стресс ухудшает работу мозга \n Из-за воздействия стресса в организме человека увеличивается количество белков, замедляющих или устанавливающих рост синапсов, служащих соединительными элементами нейронных сетей. <i>При высокой стрессовой интенсивности головной мозг начинает усыхать, а масса префронтальной коры, отвечающая за принятие решений, становится меньше.</i>\n В результате может развиться болезнь Альцгеймера.
\n\n2. Стресс влияет на человека на физиологическом уровне. Яркие примеры изменений в человеческом организме: \n· выпадение волос \n· ожирение или похудение \n· тугоухость \n· цирроз печени \n· рак \n· проблемы с сердечно-сосудистой системой \n· повышение артериального давления \n· сахарный диабет.
\n\n3. Стресс лишает смелости. \n Головные боли сопровождаются перенаправлением потока крови к сердцу и конечностям. <i>В результате путается мышление, мозг перестает нормально работать.</i> Так, в ситуациях, требующих немедленное действие, человек может постоянно сомневаться и бояться принятия решения. ''',
'''<b>Мировые факты</b>
\n1. В Японии студенты справляются со стрессом перед экзаменами с помощью самодисциплины и совершения 'ритуалов': множество молодых людей посещают храмы, молятся за благополучие результатов на экзамене.
\n\n2. Во Франции студенты предпочитают готовится к важным событиям в группах: коллективно обмениваются знаниями, оказывают взаимоподдержку. \nФранцузы любят посещать культурные мероприятия, веря, что разнообразие культурного опыта поможет лучше усваивать материал.
\n\n3. В Германии студенты известны структурированным и дисциплинированным подходом к учебе. \nРебята создают подробные планы по подготовке, разделяя учебный план на небольшие части. Однако большинство предпочитают активный отдых перед экзаменами: спорт, пробежка на свежем воздухе, прогулка с близкими ''',
'''<b>Исторические факты</b>
\nСамый распространенный и критичный по значимости в современном мире - <i>информационный стресс</i>. Мозг не успевает разложить всю поступающую в него информацию, стараясь обработать ее. В момент разделения данных задействовано <i>левое полушарие</i>, из-за чего возникает нарушение межполушарного равновесия, как следствие - депрессия.
\nЖители Древнего мира переживали и нервничали, но другим образом. По словам палеонтолога Станислава Добрышевского существуют 'маркеры' неспецифического стресса: <i>отметины на костях, зубах, внутренней части черепа</i>, свидетельствующие о попытке древнего человека приспособиться к изменениям.
\nЖивущих в XVll веке поражала "вялость", современников XVlll века - "разбитость". Апогей эволюции усталости французский историк Жорж Вигарелло называет "упадок сил" рабочих XIX века. \n\n<b>Получается, что постепенно человек стал концентрироваться на внутреннем мире, проводить самоанализ. В результате состояния сфокусированности на себе мы добрались до настоящих дней с большим букетом психологических заболеваний и крайних (между нормой и патологий) состояний.</b>''']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    date = datetime.datetime.now()
    hour = date.hour
    if 0 < hour < 4:
        time = '🌔 Доброй ночи'
        bot.send_message(message.chat.id, f'<b>{time}, <i>{message.from_user.first_name}</i></b>.\n\nОсновная задача бота: информирование о стрессе в студенческую пору. \n\nМаршрутизация через доступные команды: \n1. /stress - введение и симптомы проявления стресса у подростков в учебный период  \n2. /reasons - причины формирования стресса \n3. /methods - методы борьбы с плохим самочувствием \n4. /facts - интересные научные факты, затрагивающие медицину и историю стресса. \n\n <b>Приятного прочтения ☺</b>', parse_mode='html')
    elif 4 <= hour < 12:
        time = '☀ Доброе утро'
        bot.send_message(message.chat.id, f'<b>{time}, <i>{message.from_user.first_name}</i></b>.\n\nОсновная задача бота: информирование о стрессе в студенческую пору. \n\nМаршрутизация через доступные команды: \n1. /stress - введение и симптомы проявления стресса у подростков в учебный период  \n2. /reasons - причины формирования стресса \n3. /methods - методы борьбы с плохим самочувствием \n4. /facts - интересные научные факты, затрагивающие медицину и историю стресса. \n\n <b>Приятного прочтения ☺</b>', parse_mode='html')
    elif 12 <= hour < 17:
        time = '🕊 Добрый день'
        bot.send_message(message.chat.id, f'<b>{time}, <i>{message.from_user.first_name}</i></b>.\n\nОсновная задача бота: информирование о стрессе в студенческую пору. \n\nМаршрутизация через доступные команды: \n1. /stress - введение и симптомы проявления стресса у подростков в учебный период  \n2. /reasons - причины формирования стресса \n3. /methods - методы борьбы с плохим самочувствием \n4. /facts - интересные научные факты, затрагивающие медицину и историю стресса. \n\n <b>Приятного прочтения ☺</b>', parse_mode='html')
    elif 17 <= hour <= 23:
        time = '🌃 Добрый вечер'
        bot.send_message(message.chat.id, f'<b>{time}, <i>{message.from_user.first_name}</i></b>.\n\nОсновная задача бота: информирование о стрессе в студенческую пору. \n\nМаршрутизация через доступные команды: \n1. /stress - введение и симптомы проявления стресса у подростков в учебный период  \n2. /reasons - причины формирования стресса \n3. /methods - методы борьбы с плохим самочувствием \n4. /facts - интересные научные факты, затрагивающие медицину и историю стресса. \n\n <b>Приятного прочтения ☺</b>', parse_mode='html')

@bot.message_handler(content_types=['text'])
def main_func(message):
    if message.text == '/stress':
       bot.send_message(message.chat.id, stress[0], parse_mode='html', reply_markup=get_kb(0, name='stress'))
    elif message.text == '/reasons':
       bot.send_message(message.chat.id, reasons, parse_mode='html', reply_markup=get_kb(0, name='reasons'))
    elif message.text == '/methods':
       bot.send_message(message.chat.id, methods[0], parse_mode='html', reply_markup=get_kb(0, name='methods'))
    elif message.text == '/facts':
       bot.send_message(message.chat.id, facts[0], parse_mode='html', reply_markup=get_kb(0, name='facts'))
    else:
        img = open('assets/meme.jpg', 'rb')
        bot.send_photo(message.chat.id, img, 'Я не понимаю Вас. Введите одну из существующих команд, пожалуйста: /stress, /methods, /reasons, /facts.')
        img.close()

def get_kb(index, name):
    kb = types.InlineKeyboardMarkup(row_width=2)
    if name == 'stress':
     if index == 0:
        btn_next = types.InlineKeyboardButton('Далее', callback_data='stress_1')
        kb.add(btn_next)
     elif index > 0 and index + 1 < len(stress):
        btn_prev = types.InlineKeyboardButton('Назад', callback_data=f'stress_{index - 1}')
        btn_next = types.InlineKeyboardButton('Далее', callback_data=f'stress_{index + 1}')
        kb.add(btn_next, btn_prev)
     else:
        btn_prev = types.InlineKeyboardButton('Назад', callback_data=f'stress_{index - 1}')
        btn_to_reasons = types.InlineKeyboardButton('Перейти к причинам', callback_data='to_reasons')
        kb.add(btn_prev)
        kb.add(btn_to_reasons)

    elif name == 'reasons':
        btn_to_methods = types.InlineKeyboardButton('Перейти к методам', callback_data='to_methods')
        kb.add(btn_to_methods)

    elif name == 'methods':
     btn_to_facts = types.InlineKeyboardButton('Перейти к фактам', callback_data='to_facts')
     if index == 0:
        btn_next = types.InlineKeyboardButton('Далее', callback_data='methods_1')
        kb.add(btn_next)
     elif index > 0 and index + 1 < len(methods):
        btn_prev = types.InlineKeyboardButton('Назад', callback_data=f'methods_{index - 1}')
        btn_next = types.InlineKeyboardButton('Далее', callback_data=f'methods_{index + 1}')
        kb.add(btn_next, btn_prev)
     else:
        btn_prev = types.InlineKeyboardButton('Назад', callback_data=f'methods_{index - 1}')
        kb.add(btn_prev)
        kb.add(btn_to_facts)


    elif name == 'facts':
     btn_to_rate = types.InlineKeyboardButton('Перейти к оценке',callback_data='to_rate')
     if index == 0:
        btn_next = types.InlineKeyboardButton('Далее', callback_data='facts_1')
        kb.add(btn_next)
     elif index > 0 and index + 1 < len(facts):
        btn_prev = types.InlineKeyboardButton('Назад', callback_data=f'facts_{index - 1}')
        btn_next = types.InlineKeyboardButton('Далее', callback_data=f'facts_{index + 1}')
        kb.add(btn_next, btn_prev)
     else:
        btn_prev = types.InlineKeyboardButton('Назад', callback_data=f'facts_{index - 1}')
        kb.add(btn_prev)
        kb.add(btn_to_rate)

    return kb

def rate_kb():
    rate = types.InlineKeyboardMarkup(row_width=5)
    btn_1 = types.InlineKeyboardButton('🌟', callback_data='rate_one')
    btn_2 = types.InlineKeyboardButton('🌟🌟', callback_data='rate_two')
    btn_3 = types.InlineKeyboardButton('🌟🌟🌟', callback_data='rate_three')
    btn_4 = types.InlineKeyboardButton('🌟🌟🌟🌟', callback_data='rate_four')
    btn_5 = types.InlineKeyboardButton('🌟🌟🌟🌟🌟', callback_data='rate_five')
    rate.add(btn_1, btn_2, btn_3, btn_4, btn_5)
    return rate

@bot.callback_query_handler(func=lambda call: True)
def main(call):
    if call.data.startswith('stress'):
        call_stress(call)
    elif call.data.startswith('methods'):
        call_methods(call)
    elif call.data.startswith('facts'):
        call_facts(call)
    if call.data.startswith('rate'):
        call_rate(call)


    if 'to' in call.data:
        if call.data.endswith('_reasons'):
            bot.edit_message_text(reasons, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=get_kb(index=1, name='reasons'))
        elif call.data.endswith('_methods'):
            bot.edit_message_text(methods[0], chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=get_kb(index=0, name='methods'))
        elif call.data.endswith('_facts'):
            bot.edit_message_text(facts[0], chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=get_kb(index=0, name='facts'))
        elif call.data.endswith('_rate'):
            bot.edit_message_text('Спасибо, что дочитали до конца. \nПожалуйста, оцените бота (очень важно для дальнейшего развития)', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=rate_kb())



def call_stress(call):
    index = int(call.data.split('_')[1])
    message_id = call.message.message_id
    chat_id = call.message.chat.id
    bot.edit_message_text(stress[index], chat_id=chat_id, message_id=message_id, reply_markup=get_kb(index, name='stress'))

def call_methods(call):
    index = int(call.data.split('_')[1])
    message_id = call.message.message_id
    chat_id = call.message.chat.id
    bot.edit_message_text(methods[index], chat_id=chat_id, message_id=message_id, reply_markup=get_kb(index, name='methods'))

def call_facts(call):
    index = int(call.data.split('_')[1])
    message_id = call.message.message_id
    chat_id = call.message.chat.id
    bot.edit_message_text(facts[index], chat_id=chat_id, message_id=message_id, reply_markup=get_kb(index, name='facts'))

prev_msg_id = None
def call_rate(call):
    global prev_msg_id
    rate = call.data.split('_')[1]
    if rate == 'one':
        bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за оценку! Я постараюсь научиться на своих ошибках и стать лучше.')
        new_param = 'one'
    elif rate == 'two':
       bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за оценку! Я постараюсь научиться на своих ошибках и стать лучше.')
       new_param = 'two'
    #    send_gif(call, param='one_to_three')
    elif rate == 'three':
       bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за оценку! Я постараюсь научиться на своих ошибках и стать лучше.')
       new_param = 'three'
    #    send_gif(call, param='four_to_five')
    elif rate == 'four':
       bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за оценку! Рада, что вам понравилось. Держите милого котика')
       new_param = 'four'
    elif rate == 'five':
       bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за оценку! Рада, что вам понравилось. Держите милого котика')
       new_param = 'five'

    if prev_msg_id:
        try:
         bot.delete_message(chat_id=call.message.chat.id, message_id=prev_msg_id )
        except Exception as e:
            print(f'Ошибка удаления сообщения: {e}')

    prev_msg_id = send_gif(call, param=new_param)


def send_gif(call, param):
    if param=='one':
        gif = open('assets/rate_one.gif', 'rb')
        message = bot.send_video(call.message.chat.id, gif, None, 'Sad')
        gif.close()

    elif param=='two':
        gif = open('assets/rate_two.gif', 'rb')
        message = bot.send_video(call.message.chat.id, gif, None, 'Sad')
        gif.close()

    elif param=='three':
        gif = open('assets/rate_three.gif', 'rb')
        message = bot.send_video(call.message.chat.id, gif, None, 'Sad')
        gif.close()

    elif param=='four':
        gif = open('assets/rate_four.gif', 'rb')
        message = bot.send_video(call.message.chat.id, gif, None, 'Happy')
        gif.close()

    elif param=='five':
        gif = open('assets/rate_five.gif', 'rb')
        message = bot.send_video(call.message.chat.id, gif, None, 'Happy')
        gif.close()

    return message.message_id

if __name__ == '__main__':
    bot.polling(none_stop=True)
