with open("input.txt") as f:
    all_lines = list(f.readlines())
    for i in [all_lines[i:i + 7] for i in range(0, len(all_lines), 7)]:
        _domain = i[2].strip().strip("x")
        _record_type = i[-3].strip().strip("x")
        _ip = i[-1].strip()
        bind_line = _domain + ". 1 IN " + _record_type + " " + _ip
        print(bind_line)
