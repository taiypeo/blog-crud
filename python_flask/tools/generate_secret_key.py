import random
import string

LENGTH = 30
CHARS = string.ascii_letters + string.digits

token = "".join(random.choices(CHARS, k=LENGTH))
print(token)
