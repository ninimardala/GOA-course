def fake_binary(s):
    return ''.join('0' if int(d) < 5 else '1' for d in s)
print(fake_binary("2"))