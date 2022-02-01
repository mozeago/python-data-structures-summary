def func(x, ans):
    if x == 0:
        return 0
    else:
        return func(x - 1, x + ans)


if __name__ == "__main__":
    print(func(2, 66))
