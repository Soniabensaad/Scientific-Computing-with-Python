#!/usr/bin/python3
def main():
    # Test case 1
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    print(arithmetic_arranger(problems))
    # Output:
    #    32      3801      45      123
    # + 698    -    2    + 43    +  49
    # -----    ------    ----    -----

    # Test case 2
    problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
    print(arithmetic_arranger(problems, True))
    # Output:
    #    32         1      9999      523
    # +  8    - 3801    + 9999    -  49
    # ----    ------    ------    -----
    #   40     -3800     19998      474

if __name__ == '__main__':
    main()
