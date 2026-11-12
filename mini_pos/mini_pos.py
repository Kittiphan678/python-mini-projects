#ด่านที่ 1: ระบบล็อกอินแคชเชียร์
print ("==============================")
print ("ระบบล็อกอินแคชเชียร์")
sys_user,sys_pass,attempts = "admin", "1234",3
bill_total,daily_sales = 0,0
while attempts > 0:
    ip_user = input("กรุณากรอก username : ")
    if ip_user == sys_user :
        print ("มี username")
        ip_pass = input("กรุณากรอก password : ")
        if ip_pass == sys_pass:
            print ("เข้าสู่ระบบสำเร็จ เปิดใช้งานระบบ POS")
            break
        else :
            print (f"ีรหัสผ่านผิด! เหลือโอกาสอีก {attempts-1} ครั้ง (กรุณาลองใหม่)")
    else :
        print (f"ข้อมูลผิด! เหลือโอกาสอีก {attempts-1} ครั้ง (กรุณาลองใหม่)")
    attempts -= 1
#ด่านที่ 2: ระบบเมนูหลักและการรับออเดอร์
if attempts >0 :
    print ("==============================")
    print ("[เมนูหลัก] 1: รับออเดอร์ | 2: ดูยอดขายรวม | 0: ปิดระบบ")
    while True:
        service = input("กรุณาเลือกบริการ : ")
        match service:
            case "1":
                print ("--- เริ่มคิดเงินบิลใหม่ ---")
                total_price = 0
                items = int(input("จำนวนรายการที่สั่ง: "))
                for bill in range (1,items+1):
                    price,amount = map(int,input(f"รายการที่ {bill} (กรอก ราคา และ จำนวน เว้นวรรคคั่น) : ").split())
                    total_price += price * amount
                member = input("เป็นสมาชิกหรือไม่ (y/n) : ")
                if member == "y":
                    discount = total_price * 0.10 if total_price >= 500 else total_price * 0.05
                else:
                    discount = 0
                net_price = total_price - discount
                daily_sales += net_price
                bill_total += 1
                print (f"ยอดรวม : {total_price:.2f} บาท | ส่วนลด: {discount:.2f} บาท | ยอดสุทธิ: {net_price:.2f} บาท")
            case "2":
                print (f"สรุปยอดวันนี้ : ขายได้ {bill_total} บิล | ยอดขายรวมสุทธิ: {daily_sales:.2f} บาท")
            case "0":
                break
                    
else:
    print ("บัญชีถูกล็อก กรุณาติดต่อผู้จัดการ")