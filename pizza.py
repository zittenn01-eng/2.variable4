#[2장]
#피자메뉴
pizza1 = "페퍼로니 피자"
pizza2 = "치즈 피자"
pizza3 = "콤비네이션 피자"
pizza4 = "불고기 피자"
pizza5 = "해산물 피자"
price1 = 3500

# 피자 선택
print("피자를 선택해주세요/한 종류의 피자만 선택가능합니다.")
print(pizza1, "(",price1,"원)")
print(pizza2, "(",price1,"원)")
print(pizza3, "(",price1,"원)")
print(pizza4, "(",price1,"원)")
print(pizza5, "(",price1,"원)")

pizza = input("피자 이름을 입력하세요: ")
pizza_count = int(input("수량을 입력하세요:여러 조각을 선택가능합니다 "))
# 피자 총 주문 가격 계산
total_price = 0

print("===========================")
print("주문 내역:")
print("===========================")
print("피자:")

subtotal = price1 * pizza_count
total_price = total_price + subtotal

print("-",pizza,"(",price1,"원) x",pizza_count)
print("---------------------------")
print(" 피자 총 가격:", subtotal,"원")