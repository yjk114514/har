from har import har

myhar = har.load(r'D:\project\facebook\src\ins\resource\ins-1.har')

# 访问第一个 entry 的 request 属性
first_entry = myhar.entries[0]
print(first_entry.request)
first_entry.set_cursor('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# 重发第一个请求
response = myhar.replay(0)
print(response.status_code)