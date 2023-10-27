from Note import Note
from scale import Scale

def main():
    note_c = Note("E", False, False)
    scale_1 = Scale(note_c, True, False)
    print(scale_1.get_scale())

if __name__ == "__main__":
    main()