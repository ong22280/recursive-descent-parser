# Recursive Descent Parser

### สมาชิกในกลุ่ม

| รหัสนักศึกษา | ชื่อ-นามสกุล              |
| ------------ | ------------------------- |
| 6410401183   | นาย สิทธิพงค์ เหมล้วน     |
| 6410402121   | นาย ภูริต เทพกฤษณ์        |
| 6410406568   | นาย ณัชพล เรืองนาม        |
| 6410406878   | นาย ศรันย์ภวัต โพธิ์สร้อย |

<hr>

โปรแกรมนี้เป็น Recursive Descent Parser เพื่อวิเคราะห์และตรวจสอบความถูกต้องของสตริงที่กำหนด Grammar เป็น

```txt
E -> T | T + E
T -> int | int * T | (E)
```

### ขั้นตอนการทำงานของโปรแกรม
  1. แปลง E เป็นฟังก์ชัน ตาม Grammar `E -> T | T + E` ดังนี้
      ```python
      def E(tokens):
          global index
          if index >= len(tokens):
              print("reject")
              exit()
          
          # T
          T(tokens)
          
          # T + E
          if index < len(tokens) and tokens[index] == '+':
              index += 1
              if index >= len(tokens):
                  print("reject")
                  exit()
              E(tokens)
      ```
  2. แปลง T เป็นฟังก์ชัน ตาม Grammar `T -> int | int * T | (E)` ดังนี้
      ```python
      def T(tokens):
          global index
          if index >= len(tokens):
              print("reject")
              exit()
          
          # int
          if tokens[index] == 'int':
              index += 1
              
              # int * T
              if index < len(tokens) and tokens[index] == '*':
                  index += 1
                  if index >= len(tokens):
                      print("reject")
                      exit()
                  T(tokens)
                  
          # (E)
          elif tokens[index] == '(':
              index += 1
              E(tokens)
              if index < len(tokens) and tokens[index] == ')':
                  index += 1
              else:
                  print("reject")
                  exit()
      ```
  3. ใช้ recursive_descent_parser เพื่อเรียกใช้ฟังก์ชัน E และตรวจสอบความถูกต้องของสตริงที่กำหนด
      ```python
      def recursive_descent_parser(tokens):
        global index
        
        E(tokens)
        if index == len(tokens):
            print("accept")
        else:
            print("reject")
      ```

### วิธีการใช้งาน
  1. run โปรแกรม `python3 recursive_descent_parser.py`
  2. พิมพ์ Token stream ที่ต้องการตรวจสอบความถูกต้อง เช่น `( int )` หรือ `int * int + int`
  3. โปรแกรมจะแสดงผลลัพธ์ว่า `accept` หรือ `reject` ตามความถูกต้องของ Token stream ที่ใส่เข้าไป