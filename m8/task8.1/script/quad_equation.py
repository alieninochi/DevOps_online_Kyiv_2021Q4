import math
import sys
import time

# exit codes
SUCCESS = 0
INVALID_PARAMETERS = 1


def validate_param(msg):
    tries = 3
    while tries > 0:
        try:
            param = int(input(msg))
        except ValueError:
            print("This is not a number. Try again.")
            tries -= 1
        else:
            print("OK")
            return param

    return sys.exit(f"exit code INVALID_PARAMETERS={INVALID_PARAMETERS}")


def discriminant(a, b, c):
    return b**2 - 4 * a * c


def roots(d, a, b, c):
    if a == 0:
        return None, None

    if d > 0:
        x1 = round((-b + math.sqrt(d)) / (2 * a), 3)
        x2 = round((-b - math.sqrt(d)) / (2 * a), 3)
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + complex(0, math.sqrt(d * (-1)))) / (2 * a)
        x1 = complex(round(x1.real, 3), round(x1.imag, 3))
        x2 = (-b - complex(0, math.sqrt(d * (-1)))) / (2 * a)
        x2 = complex(round(x2.real, 3), round(x2.imag, 3))
    return x1, x2


def solv_square(a, b, c) -> roots:
    dis = discriminant(a, b, c)
    return roots(dis, a, b, c)


def square_print(a, b, c, result):
    if isinstance(result, float):
        print(f"The root of the equation:\n x = {result:.3f}\n")
    else:
        print(f"The roots of the equation:\n x1 = {result[0]}\n x2 = {result[1]}")


def main():
    a = validate_param("Enter parameter a: ")
    b = validate_param("Enter parameter b: ")
    c = validate_param("Enter parameter c: ")

    answer = solv_square(a, b, c)
    print(isinstance(answer, float))
    square_print(a, b, -c, answer)

    time.sleep(1)
    return sys.exit(f"exit code SUCCESS={SUCCESS}")


if __name__ == "__main__":
    main()
