def fruit_price(number_of_momo, number_of_mikan):
    total_momo = number_of_momo * 100
    total_mikan = number_of_mikan * 40
    total = total_momo + total_mikan
    return total

count_momo = 5
count_mikan = 10

total = fruit_price(count_momo, count_mikan)

print(f'もも{count_momo}個と、みかん{count_mikan}個で、{total}円です')
