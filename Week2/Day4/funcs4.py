def sunny_dark(hour: int) -> str | None:
    if 10 < hour < 18:
        return "sunnny"
    elif 24 > hour > 18 or 0 < hour < 10:
        return "dark"
    else:
        return None
    
print(sunny_dark(35))

