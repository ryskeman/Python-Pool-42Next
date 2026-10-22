# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fernfern <fernfern@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/22 16:52:04 by fernfern          #+#    #+#              #
#    Updated: 2026/10/22 16:59:54 by fernfern         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plot_area():
	length = int(input("Enter length: "))
	width = int(input("Enter width: "))
	area = length * width
	print(f"Plot area: {area}")