"""gugudan.py

간단한 구구단 출력 스크립트.

사용법:
  python gugudan.py        # 2단부터 9단까지 전체 출력
  python gugudan.py 3      # 3단만 출력
  python gugudan.py all    # 전체 출력 (python gugudan.py와 동일)
"""

import sys


def print_table(n: int) -> None:
    if n < 1 or n > 9:
        raise ValueError("n must be between 1 and 9")
    print(f"{n}단")
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")
    print()


def print_all() -> None:
    for n in range(2, 10):
        print_table(n)


def main() -> None:
    if len(sys.argv) == 1:
        print_all()
        return

    arg = sys.argv[1]
    if arg.lower() == "all":
        print_all()
        return

    try:
        n = int(arg)
    except ValueError:
        print("Usage: python gugudan.py [n|all]  where n is 1..9")
        sys.exit(2)

    if not (1 <= n <= 9):
        print("n must be between 1 and 9")
        sys.exit(2)

    print_table(n)


if __name__ == "__main__":
    main()
