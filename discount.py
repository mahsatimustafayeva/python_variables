price=float(input("Mehsulun ilkin qiymetini daxil edin: "))
discount=float(input("Endirim faizi: "))

discount_amount=price*discount/100
final_price=price-discount_amount
print("Endirim meblegi:", discount_amount)
print("Mehsulun endirimli qiymeti: ", final_price)