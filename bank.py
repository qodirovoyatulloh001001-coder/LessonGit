bank = input("vvedite deytviye( balans/ snyat/popolnit)   ")
match bank:
    case "balans":
        print("balansi shumo 1000 somoni")
    case "snyat":
        schot = input("summaro vorid kuned")
        print("SHumo", schot, "somoni girifted")


    case "popolnit":
        SChot = input(" Summaro vorid kuned")
        print("SHumo ba",SChot, "somon hisobatonro pur karded")
if bank==0:
    print("Idi nav muborak")