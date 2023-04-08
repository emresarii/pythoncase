#This function returns a string based on N with using "+" and "-" repetitively
def solution(n: int):
 return "".join(["+" if i % 2 == 0 else "-" for i in range(n)]) if 1 <= n <= 100 else "N should be between 1-100"
        
        
# Driver code
if __name__ == "__main__":
    result=solution(100)
    print(result)
