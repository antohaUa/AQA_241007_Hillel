import db_model
from db_orm import Db

db = Db()
data = db.session.query(db_model.User).filter_by(login='pp').first()
print(type(data))
breakpoint()
print(data.name)

columns = (db_model.Reservation.time.label('reservation.time'),
           db_model.Service.duration.label('service.duration'),
           db_model.Service.id.label('service.id'))
data2 = db.session.query(*columns).join(db_model.Service).filter(db_model.Reservation.date == '2024-06-10',
                                                                 db_model.Reservation.trainer == 1).all()
print(data2)



