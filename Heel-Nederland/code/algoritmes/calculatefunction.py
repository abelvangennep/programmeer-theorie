def calculate(solution):
    minutes = 0
    for traject in solution["trajecten"]:
        minutes += traject.travel_time
    
    solution["trajecten"]
    P = solution["visited_trajects"] / solution["total_trajects"]
    T = len(solution["trajecten"])
    # print("_____________________________________________")
    # print(P * 10000 - (T * 100 + minutes))
    score = P * 10000 - (T * 100 + minutes)

    # f= open("solution.txt","a+")

    # f.write(f"SCORE:{score}\n" + f"MINUTES:{minutes}\n" + f"P:{P}\n" + f"T:{T}\n" + "\n")
    # f.close()

    return score