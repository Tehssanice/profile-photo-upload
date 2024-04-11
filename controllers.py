import uuid
from dbschema import User

IMAGEDIR ='images/'
def create_user(name, age, email, session, photo):
    if photo is not None:
      photo_ext = photo.filename.split('.')[-1]
      if photo_ext not in ["jpg", "jpeg", "png", "svg"]:
         return {"error": "Invalid Format"}
      photo.filename = f"{uuid.uuid4()}.{photo_ext}"
      with open (f"{IMAGEDIR}{photo.filename}", "wb") as buffer:
        buffer.write(photo.file.read())
        user = User(name=name, age=age, email=email, photo=photo.filename)
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"message": "success"}
    else:
        user = User(name=name, age=age, email=email, photo=None)
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"message": "success"}
       