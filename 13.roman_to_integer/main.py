from solve import Solution 


def main():
#print(Solution().romanToInt("CMXCVIII"))
    s = Solution()
    a = s.romanToInt("MCMVII")
    b = s.romanToInt("MMXI")
    c = s.romanToInt("XC")
    d = s.romanToInt("MCMXC")

    print(a, b, c, d, sep="\n")


if __name__ == "__main__":
    main()
