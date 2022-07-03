def sum(n):
    result = 0

    i = 1
    while i <= n:
        result += i
        i += 1
    
    return result

if __name__ == "__main__": # 직접 실행하면
    print("sumModule.py 직접 실행함")
    print("동작 확인")
    print(f"1 부터 10 까지의 합은 {sum(10)}")