
def frame_id_validator(id: int):
    if not 0 < id < 1000:
        raise ValueError("Frame id value must be into interval (0, 1000)")
