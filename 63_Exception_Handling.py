a = 5
b = 2

try:
    print("resource open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError:
    print("Hey, cannot divide a Number by Zero:")
except ValueError:
    print("Invalid Input")
except Exception as e:
    print("Something went wrong.....\n", e)
finally:
    print("resource Closed")

print("Bye")