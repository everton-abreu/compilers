inteiro: x

x := 2

inteiro: a[x][x], b
flutuante: c

a[1] := 1 || 1

func(inteiro: a[], flutuante: b)
  se 1 < 2 então
    leia(a[1])
    b := a[1]
  fim
fim

inteiro principal()
  a[2] := 2
  b := 3
  func(a, b)
  func()
  se 1 > 0 então
    escreva(0)
  fim
  retorna(a + b)
fim
