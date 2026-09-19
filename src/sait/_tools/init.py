from sait._tools.config import read_config


def initialize() -> None:
    pass

def is_initialized() -> bool:
    try:
        read_config()
    except FileExistsError:
        return False
    except ValueError:
        return False
    except SyntaxError:
        return False

    return True
