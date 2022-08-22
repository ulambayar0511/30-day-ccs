# Мат-даа сайн хүн л хийж чадна . v1

![challenge image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/badangel/30-Day/Day-4/task/challenge.png)

> **Өгөгдсөн холбоосын дагуу terminal -аас "nc 18.141.145.22 10000" хийж TCP холболт үүсгэвэл** 

![task image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/badangel/30-Day/Day-4/task/terminal.png)

> **netcat хийж TCP холболт үүсгэсэний дараа 2 тооны нийлбэрийг бодох нь харагдана.**

> **3 секундын дотор нийлбэрийг оруулахгүй бол timeout зааж *"2 тоо бодож чадахгүй ямар суга юм бэ:("* хэмээн баннер харагдаж холболт сална. Мөн хариуг буруу оруулсан үед холболт сална.**

## Ийм учир script бичиж ажилуулвал
```

    import socket
    host = 'localhost'
    port = 10000
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    answer = s.recv(size)
    print(answer.decode())
    exp = s.recv(size).decode("utf-8") 
    arr = exp.split('+')
    print(arr)
    a = arr[1]
    result = int(arr[0])+int(a[:a.index('=')])
    s.send(str(result).encode())
    print(s.recv(size).decode())
    s.close()

```

### flag "M@tH_iS_k0n1_0F_sC13nCe" гэж олдох болно.


