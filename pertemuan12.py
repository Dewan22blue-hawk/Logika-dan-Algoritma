# def seqSearch(data, key):
#     i = 0
#     pos = i + 1
#     while (i < len(data)):
#         if data[i] == key:
#             break
#         i += 1
#         pos = i+1
#     if pos <= len(data):
#         print('data', key, 'ditemukan di posisi', pos)
#     else:
#         print('data tidak ditemukan')
#     return pos


# data = [15, 4, 9, 1, 15, 7]
# seqSearch(data, 15)


def seqSearch(data, key):
    i = 0
    a = 0
    pos = i + 1
    while (i < len(data)):
        if data[i] == key:
            # break
            a += 1
            print('data', key, 'ditemukan di posisi', pos)
        i += 1
        pos = i + 1

    if a == 0:
        print("tidak ditemukan")
    # else:
    #     print('data tidak ditemukan')
    return pos


data = [15, 4, 9, 1, 15, 7]
seqSearch(data, 5)


# def STRAITMAXMIN(A, n):
#     max = A[0]
#     min = A[0]
#     for i in range(1, n):
#         if A[i] > max:
#             max = A[i]
#     else:
#         if A[i] < min:
#             min = A[i]
#     print("Max =", max, ", Min =", min)


# A = [3, 23, 12, 4, 5, 21, 24, 14]
# a = len(A)
# STRAITMAXMIN(A, len(A))
# STRAITMAXMIN(A, 2)
