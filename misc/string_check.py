def main():
    us = 'hakan'
    print(us)
    print(type(us))
    bs = b'hakan'
    print(bs)
    print(type(bs))
    ubs = bs.decode("utf-8")
    print(ubs)
    print(type(ubs))
    bus = us.encode("utf-8")
    print(bus)
    print(type(bus))


if __name__ == '__main__':
    main()