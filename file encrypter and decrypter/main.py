with open('i1.jpg',"rb") as f:
    with open('i1_enc.jpg','wb') as e:
        for chunk in f:
            e.write(~chunk)
print("Encrypted...")