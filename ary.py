# calon_istri = "Icha Ariany"
# print(
#     f"Tunangan saya kelak di masa depan adalah {calon_istri} tercinta, tersayang, tulang rusukku")


def STRAITMAXMIN(A, n):
    max = A[0]
    min = A[0]
    for i in range(1, n):
        if A[i] > max:
            max = A[i]
        elif A[i] < min:
            min = A[i]
    print("Max =", max, ", Min =", min)


n = [10, 4, 9, 1, 15, 7]
a = [1, 14, 3, 6, 5, 17]
STRAITMAXMIN(a, n)
