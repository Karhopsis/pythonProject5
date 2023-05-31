def ingreedients (s, n):
    dict = {'cups':0, 'tablespoons':0, 'teaspoons':0}
    if s in dict.keys():
        dict[s]=n
    if dict['teaspoons']>=3:
        while dict['teaspoons']>=3:
            dict['tablespoons']+=1
            dict['teaspoons']-=3
    if dict['tablespoons']>=16:
        while dict['tablespoons']>=16:
            dict['cups']+=1
            dict['tablespoons']-=16
    return dict



print(ingreedients('tablespoons',16))