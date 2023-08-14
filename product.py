from app import app, Product, db

with app.app_context():

    new_product1 = Product(
        name="Fender American Pro II Stratocaster RW, Roasted Pine",
        make="Fender",
        description="Iconic. There's simply no other way to describe the Strat. It's thrived throughout decades of music.",
        price="1799.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/59/595174/600/preview_1.jpg"
    )

    new_product2 = Product(
        name="Fender American Ultra Stratocaster RW, Arctic Pearl",
        make="Fender",
        description="Fender American Ultra Stratocaster RW is the pathway to ultra-high performance and represents the next step in Fender's modern design",
        price="2049.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/51/515279/600/preview.jpg"
    )

    new_product3 = Product(
        name="Fender Nile Rodgers Hitmaker Stratocaster, Olympic White",
        make="Fender",
        description="The Fender Nile Rodgers Hitmaker Stratocaster is a hit making machine put straight into your hands. You've heard it, hummed along to it and now you can play it.",
        price="2299.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/83/833219/600/preview.jpg"
    )

    new_product4 = Product(
        name="Fender Player Stratocaster PF, Silver",
        make="Fender",
        description="The Fender Player Stratocaster PF, is the perfect companion for any guitarist, delivering Fenders iconic tone and classic style at an exceptional value. ",
        price="679.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/71/713326/600/preview.jpg"
    )

    new_product5 = Product(
        name="Fender Vintera 60s Telecaster w/ Bigsby PF, 3-Tone Sunburst",
        make="Fender",
        description="The quality speaks for itself. When you're picking away on the Fender Vintera '60s Telecaster w/Bigsby PF guitar, you'll notice just how awe inspiring it really is.",
        price="929.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/49/491828/600/preview.jpg"
    )

    new_product6 = Product(
        name="Fender Made in Japan Ltd Ed INTL Color Telecaster RW, Maui Blue",
        make="Fender",
        description="Fender Made in Japan Ltd Ed INTL Color Telecaster RW, Maui Blue",
        price="1199.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/91/915636/600/preview.jpg"
    )

    new_product7 = Product(
        name="Fender Gold Foil Telecaster, Ebony Fingerboard, White Blonde",
        make="Fender",
        description="The Fender Gold Foil Telecaster is a tribute to the garage rock bands of the 60s and the classic instruments they played. ",
        price="1099.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/91/913947/600/preview.jpg"
    )

    new_product8 = Product(
        name="Fender Player Jaguar PF, Candy Apple Red",
        make="Fender",
        description="The Fender Player Jaguar PF is classy style and scintillating sonics boiled down into one guitar. Equipped with Fender's finely balanced alnico III humbucker and an alnico II single coil pickup, you've got crisp, purring vintage voices at your disposal. ",
        price="689.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/92/921745/600/preview.jpg"
    )

    new_product9 = Product(
        name="Fender Limited Edition Player Jaguar HH, Daphne Blue",
        make="Fender",
        description="The Fender Limited Edition Player Jaguar HH is a lethal combination of vintage Fender tone with all the perks of modern technology.",
        price="719.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/87/872499/600/preview.jpg"
    )

    new_product10 = Product(
        name="Gibson Les Paul Standard Faded 60s, Vintage Cherry Burst",
        make="Gibson",
        description="Iconic. There's simply no other way to describe the Strat. It's thrived throughout decades of music.",
        price="2199.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/85/859940/600/preview.jpg"
    )

    new_product11 = Product(
        name="Gibson Slash Les Paul Standard, November Burst",
        make="Gibson",
        description="Your child may be sweet. But this'll be your new favourite member of the family. ",
        price="2599.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/64/643710/600/preview.jpg"
    )

    new_product12 = Product(
        name="Gibson Les Paul Standard 60s Left Handed, Iced Tea",
        make="Gibson",
        description="Fall in love with tone. The Gibson Les Paul Standard '60s Left Handed is your ticket to the iconic sounds of classic Les Pauls. ",
        price="2799.00",
        image_url="https://d1aeri3ty3izns.cloudfront.net/media/55/553606/600/preview.jpg"
    )


    db.session.add(new_product1)
    db.session.add(new_product2)
    db.session.add(new_product3)
    db.session.add(new_product4)
    db.session.add(new_product5)
    db.session.add(new_product6)
    db.session.add(new_product7)
    db.session.add(new_product8)
    db.session.add(new_product9)
    db.session.add(new_product10)
    db.session.add(new_product11)
    db.session.add(new_product12)
    db.session.commit()
