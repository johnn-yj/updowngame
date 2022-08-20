def guess_number():
    import random
    
    #숫자 정하고 최소/최대/중앙값 정하기
    number=random.sample(range(1,101),3)
    number.sort()
    minimum=int(number[0])
    median=int(number[1])
    maximum=int(number[2])
    #시도횟수
    tries = 0
    #맞춘 횟수
    count = 0
    
    print("1~100 사이의 숫자를 맞추세요.")
    print("=============================")
    
    guess_list=[]
    while count<3:
        print(tries+1, "차 시도")
        #5회, 10회 시도할때 힌트
        if tries == 4 or tries == 9:
            help(minimum, maximum, guess)
        #중복하는 값 입력 불가
        while True:
            guess = int(input("숫자를 예측해보세요:"))
            if guess in guess_list:
                print("이미 예측에 사용한 숫자입니다.")
                continue
            guess_list.append(guess)
            break
        #숫자 맞췄을 경우, 못맞췄을 경우
        if int(guess)==minimum:
            count+=1
            tries+=1
            print("숫자를 맞추셨습니다! ", guess, "는 최솟값입니다.")
            continue
        elif int(guess)==median:
            count+=1
            tries+=1
            print("숫자를 맞추셨습니다! ", guess, "는 중간값입니다.")
            continue
        elif int(guess)==maximum:
            count+=1
            tries+=1
            print("숫자를 맞추셨습니다! ", guess, "는 최대값입니다.")
            continue
        else:
            tries+=1
            print(guess, "는 없습니다.")
            continue
    print("게임종료")
    print(tries, "번 시도만에 예측 성공")
    

#힌트주기
def help(minimum, maximum,guess):
    while True:
        choice = input("최솟값/최대값 힌트중 어느 힌트를 보시겠습니까?(최대/최소 를 입력해주세요)")
        if choice == "최대":
            if guess<maximum:
                print("최대값은 ", guess, "보다 큽니다.")
                break
            elif guess>maximum:
                print("최대값은 ", guess, "보다 작습니다.")
                break
        elif choice == "최소":
            if guess<minimum:
                print("최솟값은 ", guess, "보다 큽니다.")
                break
            elif guess>minimum:
                print("최솟값은 ", guess, "보다 작습니다.")
                break
        else:
            print("'최대' 혹은 '최소'를 입력하여 주세요")

            
guess_number()