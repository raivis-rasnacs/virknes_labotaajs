virkne = "kkkuuuģiiiisss"

def labo_virkni(virkne, p1, p2):
    if virkne[p1] == virkne[p2]:
        virkne = virkne.replace(virkne[p1], "_", 1)
    print(virkne)
    labo_virkni(virkne, p1 + 1, p2 + 1)
    
labo_virkni(virkne, 0, 1)
