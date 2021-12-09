# def datacalc(Wiek, Jestes, Waga, Wzrost, Ile_razy_w_tygodniu_uprawiasz_60_min_sportu, Jaki_masz_cel):
#     calori = 0
#     if Jestes == 'Mężczyzna':
#         c1 = 66
#         hm = 6.2 * Wzrost
#         wm = 12.7 * Waga
#         am = 6.76 * Wiek
#         bmr_result = c1 + hm + wm - am
#         calori += (int(bmr_result))
#     if Jestes == 'Kobieta':
#         c1 = 655.1
#         hm = 4.35 * Wzrost
#         wm = 4.7 * Waga
#         am = 4.7 * Wiek
#         bmr_result = c1 + hm + wm - am
#         calori += (int(bmr_result))
#     if Ile_razy_w_tygodniu_uprawiasz_60_min_sportu == '0':
#         calori *= 1.1
#     elif Ile_razy_w_tygodniu_uprawiasz_60_min_sportu == '1':
#         calori *= 1.2
#     elif Ile_razy_w_tygodniu_uprawiasz_60_min_sportu == '2':
#         calori *= 1.3
#     elif Ile_razy_w_tygodniu_uprawiasz_60_min_sportu == '3':
#         calori *= 1.4
#     elif Ile_razy_w_tygodniu_uprawiasz_60_min_sportu == '4':
#         calori *= 1.5
#     elif Ile_razy_w_tygodniu_uprawiasz_60_min_sportu == '5':
#         calori *= 1.6
#     elif Ile_razy_w_tygodniu_uprawiasz_60_min_sportu == '6':
#         calori *= 1.7
#     elif Ile_razy_w_tygodniu_uprawiasz_60_min_sportu == '7':
#         calori *= 1.8
#
#     if Jaki_masz_cel == 'lose':
#         calori -= 500
#     elif Jaki_masz_cel == 'maintain':
#         calori -= 0
#     elif Jaki_masz_cel == 'gain':
#         calori += 500
#     return float(calori)
# print( datacalc(23,'Mężczyzna',66,170,2,"maintain"))
#
# {% url 'mainapp:Product_data' item.category item.slug %}


def test(i,sex):
    sex_dic={"men":10,"women":30}
    d_data=sex_dic.get(sex)


    return i*d_data


print(test(3,"women"))








