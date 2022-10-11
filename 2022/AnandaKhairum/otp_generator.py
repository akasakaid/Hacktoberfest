import math, random

#GENERATE OTP CODE RANDOM 6 DIGITS

digits = "0123456789"
OTP = ""
for i in range(6) :
    OTP += digits[math.floor(random.random() * 10)]

print('This Your OTP CODE : ', OTP)