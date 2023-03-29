def generate_info() -> tuple[int, str]:
    return 'Yossi', 'A'


def concat_str(str1, str2) -> str:
    concatinated = str1 + '' + str2
    return concatinated



def summarize_info() -> str:
    str1, str2 = generate_info()
    concatinated = concat_str(str1, str2)
    return concatinated


print(summarize_info())




# def calculate_purchases(items_prices: dict[str, str], wallet: str) -> list | str: