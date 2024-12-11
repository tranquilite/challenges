# --- Day 1: Calorie Counting ---

def day1_part1(elf_manifest: list) -> int:
    elf_cal_count = 0
    elf_carrying = []
    for line in elf_manifest:
        if line != '\n':
            elf_cal_count += int(line)
        else:
            elf_carrying.append(elf_cal_count)
            elf_cal_count = 0

    return [max(elf_carrying), sum(sorted(elf_carrying)[-3:])]


if __name__ == '__main__':
    try:
        with open('inputs/day1.txt', mode='r') as fh:
            print(day1_part1(elf_manifest=fh.readlines()))
    except FileNotFoundError:
        print('oof')
