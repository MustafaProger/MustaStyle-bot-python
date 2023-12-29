models_watch = {
    'Rolex': {
        'Submariner': '600,000 - 2,700,000 руб.',
        'Datejust': '525,000 - 3,750,000 руб.',
        'Day-Date': '1,875,000 - 7,500,000 руб.',
        'GMT-Master II': '675,000 - 3,750,000 руб.',
        'Explorer': '450,000 - 1,875,000 руб.',
        'Yacht-Master': '825,000 - 3,750,000 руб.',
        'Sea-Dweller': '825,000 - 1,500,000 руб.',
        'Daytona': '975,000 - 6,000,000 руб.',
        'Milgauss': '600,000 - 1,500,000 руб.',
        'Oyster Perpetual': '375,000 - 1,500,000 руб.',
    },
    'Omega': {
        'Speedmaster': '400,000 - 2,000,000 руб.',
        'Seamaster': '350,000 - 1,800,000 руб.',
        'Constellation': '500,000 - 2,500,000 руб.',
        'De Ville': '450,000 - 2,000,000 руб.',
        'Aqua Terra': '300,000 - 1,500,000 руб.',
        'Planet Ocean': '600,000 - 3,000,000 руб.',
        'Railmaster': '350,000 - 1,500,000 руб.',
        'Globemaster': '600,000 - 3,500,000 руб.',
        'Bullhead': '500,000 - 2,500,000 руб.',
        'Ploprof': '700,000 - 3,500,000 руб.',
    }
}


for company, models in models_watch.items():
    for model, price_range in models.items():
        print(f"Выбранная модель часов {company} {model} имеет стоимость в пределах {price_range} в зависимости от комплектации.")

