# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fernfern <fernfern@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/22 17:11:41 by fernfern          #+#    #+#              #
#    Updated: 2026/10/22 17:16:51 by fernfern         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day1 = int(input("Day 1 harvest: "))
	day2 = int(input("Day 2 harvest: "))
	day3 = int(input("Day 3 harvest: "))
	total = day1 + day2 + day3
	print(f"Total harvest: {total}")