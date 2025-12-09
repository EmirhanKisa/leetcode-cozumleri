# Zorluk : Kolay

nums = [1,2,5,1]

kutu = set()
cevap = False

for i in range(len(nums)):
    if nums[i] in kutu:   # kutu set’inin içinde bu sayı zaten var mı?”
        cevap = True
        break

    kutu.add(nums[i])

print(cevap)

