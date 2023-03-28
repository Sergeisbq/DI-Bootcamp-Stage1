sample_dict = { 
            "class":{ 
                    "student":{ 
                            "name":"Mike",
                            "marks":{ 
                                    "physics":70,
                                    "history":80
                                    }
                            }
                    }
            }

print(sample_dict)
print(sample_dict["class"]["student"]["marks"]["history"])

history_mark = None
current_dict = sample_dict
while not history_mark:
    if "history" in current_dict:
        history_mark = current_dict["history"]
        break
    else:
        for key in current_dict:
            if isinstance(current_dict[key], dict):
                current_dict = current_dict[key]

print(history_mark)


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(type(keys))

dict_i = dict(zip(keys, values))
print(dict_i)