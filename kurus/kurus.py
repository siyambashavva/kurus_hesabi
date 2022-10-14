kurus = (int(input('lutfen 0-99 arasında bir kuruş değeri girin: ')))

kurus_2 = kurus % 50
bolum = kurus // 50

kurus_3 = kurus_2 % 10
bolum_2 = kurus_2 // 10

kurus_4 = kurus_3 % 5
bolum_3 = kurus_3 // 5

kurus_5 = kurus_4 % 1
bolum_4 = kurus_4 // 1

print(f'{kurus} kurusun esiti:')
print(f'{bolum} tane 50 kurus')
print(f'{bolum_2} tane 10 kurus')
print(f'{bolum_3} tane 5 kurus')
print(f'{bolum_4} tane 1 kurus')