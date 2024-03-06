qestions = [
  [
    "Which language was used to create fb?", "Python","none", "French", "JavaScript","d"
  ],
  [
    "India Prime minister name?", "Modi", "Rahul", "Sagar","none","a"
  ],
  [
    "Surat kesa city he", "Smart", "Cleane", "Green","none","a"
  ],
  [
    "Apdi Company kevi che?", "Gosod", "V.Good", "Bed","none","c"
  ],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,3200000]
money = 0

for i in range(0,len(qestions)):
  qestion = qestions[i]
  print(f"Qestions for Rs.{levels[i]} is {qestions[i][0]}")
  print(f"a. {qestions[i][1]}      b.{qestions[i][2]}")
  print(f"c. {qestions[i][3]}      d.{qestions[i][4]}")

  reply = str(input("Enter your answer:"))
  if(reply == qestions[i][5]):
    print(f"Correct answear, you have win Rs.{levels[i]}")
  else:
    print("Wrong answer!")
    break;
