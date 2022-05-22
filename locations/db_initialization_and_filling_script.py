from app import db
from app.models import Users, Region, City


db.create_all()

region1 = Region('Volgograd Oblast')
region2 = Region('Rostov Oblast')
region3 = Region('Novosibirsk Oblast')
region4 = Region('Kamchatka Krai')
region5 = Region('Kaliningrad Oblast')
region6 = Region('Murmansk Oblast')
region7 = Region('Amur Oblast')
region8 = Region('Republik of Bashkortostan')
region9 = Region('Krasnoyarsk Krai')
region10 = Region('Leningrad Oblast')

db.session.add_all([region1, region2, region3, region4, region5,
                    region6, region7, region8, region9, region10])
db.session.commit()

city1 = City('Volgograd', 1)
city2 = City('Volzhskiy', 1)
city3 = City('Uryupinsk', 1)
city4 = City('Rostov-on-Don', 2)
city5 = City('Taganrog', 2)
city6 = City('Azov', 2)
city7 = City('Novocherkassk', 2)
city8 = City('Novosibirsk', 3)
city9 = City('Koltsovo', 3)
city10 = City('Petropavlovsk Kamchatskiy', 4)
city11 = City('Elizovo', 4)
city12 = City('Koryaki', 4)
city13 = City('Kaliningrad', 5)
city14 = City('Baltiysk', 5)
city15 = City('Svetlogorsk', 5)
city16 = City('Sovetsk', 5)
city17 = City('Murmansk', 6)
city18 = City('Severomorsk', 6)
city19 = City('Apatity', 6)
city20 = City('Blagoveschensk', 7)
city21 = City('Belogorsk', 7)
city22 = City('Shimanovsk', 7)
city23 = City('Ufa', 8)
city24 = City('Salavat', 8)
city25 = City('Krasnoyarsk', 9)
city26 = City('Norilsk', 9)
city27 = City('Kansk', 9)
city28 = City('Vsevolzhsk', 10)
city29 = City('Vyborg', 10)
city30 = City('Gatchina', 10)

db.session.add_all([city1, city2, city3, city4, city5, city6, city7,
                    city8, city9, city10, city11, city12, city13, city14,
                    city15, city16, city17, city18, city19, city20, city21,
                    city22, city23, city24, city25, city26, city27, city28,
                    city29, city30])
db.session.commit()

user1 = Users(username='John')
user1.set_password('john_password')
user2 = Users(username='Bill')
user2.set_password('bill_password')

db.session.add_all([user1, user2])
db.session.commit()
