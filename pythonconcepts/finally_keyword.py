# Finally keyword in Python~~

def func():
    try:
      l = [1,2,3,4]
      i = int(input("Enter the index: "))
      print(l[i])
      return 1
    except:
        print("Some Error Occurred")
        return 0

    finally:
        print("I'm always executed")

x = func()
print(x)