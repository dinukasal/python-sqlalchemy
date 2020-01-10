from db import session,Base
from models.users import User

session.query(User).delete()

session.add_all([
    User(phoneNumber="071654564", name="Sala"),
    User(phoneNumber="0714697757", name="Dinuka")
])

session.commit()
