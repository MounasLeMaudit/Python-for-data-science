ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[1] = "World!"

list_tmp = list(ft_tuple)
list_tmp[1] = "France!"
ft_tuple = tuple(list_tmp)

ft_set.remove("tutu!")
ft_set.add("Perpignan!")

ft_dict["Hello"] = "42Perpignan!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
