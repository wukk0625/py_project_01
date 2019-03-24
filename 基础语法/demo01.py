coding = 'utf - 8'


def test_print():
    a = 'hello'
    b = 'world'
    print(a + b)  # helloworld，+号连接字符串
    print(a * 2)  # hellohello，*号重复字符串
    print(a[1])  # e，[]索引字符
    print(a[1:4])  # ell，[:]截取字符串
    print("h" in a)  # True，in是否包含
    print("M" not in a)  # True，not in是否不包含
    print(r'\n')  # \n，r原始字符串（不解析转义字符）
    print("=" * 20),
    print("My name is %s and weight is %d kg!" % ('Zara', 21))
    print("=" * 20),
    hi = 'hi\nthere'
    print(hi)


if __name__ == '__main__':
    test_print()
