import hashlib

user = "john"
password = "moreThan10CharPassword"

password_hash = "70e0f6cba9351375d1ec3440c6e2a5e41389d92c632baa1a28ca3d930c4a5a05"
print(len(password_hash))
# session = "user={}|pass={}|admin={}".format(user, password_hash, 1)
# print(session)

session = "757365723d6a6f686e7c706173733d373065306636636261393335313337356431656333343430633665326135653431333839643932633633326261613161323863613364393330633461356130357c61646d696e3d30"

session = "user=john|pass=70e0f6cba9351375d1ec3440c6e2a5e41389d92c632baa1a28ca3d930c4a5a05|admin=1"
print(session)