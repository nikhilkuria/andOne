

def build_padded_header(title:str) -> str:
    return "***   {title}   ***".format(title=title)


def build_upper_header(title:str) -> str:
    return title.upper()
