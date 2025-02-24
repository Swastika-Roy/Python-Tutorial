questions =[["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4],["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4],["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4],["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4],["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4],["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4],["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4],["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4],["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4],["which language was used to create fb?","Python","French","JavaScript",
             "Php","None",4]]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0 , len(questions)):
        question = questions[i]
        print(f"Question for Rs.{levels[i]}")
        print(f"a.{question [1]}        b.{question [2]}")
        print(f"c.{question [3]}       d.{question [4]}")
        reply = int(input("Enter your answer(1-4):"))
        if(reply == question [-1]):
           print(f"Correct answer, you have won Rs.{levels[i]}")
           if i == 4:
               money = 10000
           elif i == 9:
               money = 320000
           elif i == 14:
               money = 10000000
        else:
            print("Wrong answer")
            break
 # levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
print(f"Your take home money is {money}")
