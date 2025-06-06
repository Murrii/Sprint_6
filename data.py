# Тексты ответов для проверки соответствия вопросов и ответов
answers_text = {
    0: 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
    1: 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
    2: 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
    3: 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
    4: 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
    5: 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
    6: 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
    7: 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
}

# Адрес главной страницы
main_page_url = 'https://qa-scooter.praktikum-services.ru/'

# Адрес страницы заказа
order_page_url = "https://qa-scooter.praktikum-services.ru/order"

# наборы данных для создания заказа
order_from_ivan= {
    'name': 'Иван',
    'surname': 'Человеков',
    'address': 'Комаринская 58',
    'phone': '12121212121',
    'rent_info_data': '20.07.2026',
    'rent_info_comment': 'Звонок не работает, для отклика свистнуть три раза молодецким посвистом, гаркнуть богатырским покриком'
}

order_from_galina= {
    'name': 'Галина',
    'surname': 'Бланка',
    'address': 'Буль-буль 15',
    'phone': '34343434343',
    'rent_info_data': '20.07.2026',
    'rent_info_comment': ''
}

# Варианты периода аренды самоката
rent_info_time = ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']