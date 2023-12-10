from re import M


spelled_digit_tree = {
    "o": {
        "n": {
            "e": 1
        }
    },
    "t": {
        "w": {
            "o": 2
        },
        "h": {
            "r": {
                "e": {
                    "e": 3
                }
            }
        }
    },
    "f": {
        "o": {
            "u": {
                "r": 4
            }
        },
        "i": {
            "v": {
                "e": 5
            }
        }
    },
    "s": {
        "i": {
            "x": 6
        },
        "e": {
            "v": {
                "e": {
                    "n": 7
                }
            }
        }
    },
    "e": {
        "i": {
            "g": {
                "h": {
                    "t": 8
                }
            }
        }
    },
    "n": {
        "i": {
            "n": {
                "e": 9
            }
        }
    }
}

rev_spelled_digit_tree = {
    "e": {
        "n": {
            "o": 1,
            "i": {
                "n": 9
            }
        },
        "e": {
            "r": {
                "h": {
                    "t": 3
                }
            }
        },
        "v": {
            "i": {
                "f": 5
            }
        }
    },
    "o": {
        "w": {
            "t": 2
        }
    },
    "r": {
        "u": {
            "o": {
                "f": 4
            }
        }
    },
    "x": {
        "i": {
            "s": 6
        }
    },
    "t": {
        "h": {
            "g": {
                "i": {
                    "e": 8
                }
            }
        }
    },
    "n": {
        "e": {
            "v": {
                "e": {
                    "s": 7
                }
            }
        }
    }
}

def traverse_tree(code, i, dict=spelled_digit_tree, reversed=False):
    # print(code[i], dict)
    v = dict.get(code[i])
    if not v:
        return False
    if isinstance(v, int):
        return v
    if reversed:
        i-=1
    else:
        i+=1
    return traverse_tree(code, i, v, reversed)

def find_num(code):
    num = 0
    for i in range(len(code)):
        if code[i].isdigit():
            num += int(code[i])*10
            break
        v = traverse_tree(code, i)
        if v:
            num += v*10
            break
    for i in range(len(code)-1, -1, -1):
        if code[i].isdigit():
            num += int(code[i])
            break
        v = traverse_tree(code, i, rev_spelled_digit_tree, True)
        if v:
            num += v
            break
    print(code, num)
    return num

def solve():
    f = open('day1/codes.txt')
    total = 0
    for code in f.readlines():
        total += find_num(code)
    print(total)

if __name__ == "__main__":
    # find_num('kvhfqspcpsxndjqlonesixthree24kdmqvone')
    solve()
