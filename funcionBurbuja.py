def burbuja(nums):

    intercambio = True

    while intercambio:
        intercambio = False

        for i in range(len(nums) - 1):

            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                intercambio = True

listaNumeros = [5, 2, 1, 8, 4]
burbuja(listaNumeros)
print(listaNumeros)