denver = [1_700_000, 4_600_000, 2_100_000]

philadelhpia = []
philadelhpia.append(1_800_000)
philadelhpia.append(5_000_000)
philadelhpia.append(2_500_000)

total = [0, 0, 0]
total[0] = denver[0] + philadelhpia[0]
total[1] = denver[1] + philadelhpia[1]
total[2] = denver[2] + philadelhpia[2]


average = (total[0] + total[1] + total[2]) / len(total)

print("Produkcja w roku 2012 wyniosła ", "{:,d}".format(total[0]).replace(","," "), " sztuk")
print("Produkcja w roku 2013 wyniosła ", "{:,d}".format(total[1]).replace(","," "), " sztuk")
print("Produkcja w roku 2014 wyniosła ", "{:,d}".format(total[2]).replace(","," "), " sztuk")
print("Średnia produkcja wuniosła", "{:,.0f}".format(average).replace(","," "), "sztuk.")