import contextlib

from Crypto.Util.number import long_to_bytes
from sage.all import Integer, Rational, assume, solve, var

def u(a, x, y):
    assert a.is_integer() and x.is_rational() and y.is_rational()
    return x + Rational((a * x - y)/(x ** 2 + y ** 2))

def v(a, x, y):
    assert a.is_integer() and x.is_rational() and y.is_rational()
    return y - Rational((x + a * y)/(x ** 2 + y ** 2))

A = Rational(
    Integer(6080057478320734754578252336954411086329731226445881868123716230995225973869803901199434606333357820515656618869146654158788168766842914410452961599054518002813068771365518772891986864276289860125347726759503163130747954047189098354503529975642910040243893426023284760560550058749486622149336255123273699589) /
    Integer(10166660077500992696786674322778747305573988490459101951030888617339232488971703619809763229396514541455656973227690713112602531083990085142454453827397614)
)
U = Rational(
    Integer(3225614773582213369706292127090052479554140270383744354251548034114969532022146352828696162628127070196943244336606099417210627640399143341122777407316956319347428454301338989662689983156270502206905873768685192940264891098471650041034871787036353839986435) /
    Integer(9195042623204647899565271327907071916397082689301388805795886223781949921278129819112624089473306486581983153439866384171645444456400131619437018878598534536108398238424609)
)
V = Rational(
    Integer(1971582892158351181843851788527088806814104010680626247728311504906886858748378948163011806974145871263749452213375101951129675358232283650086419295655854343862361076089682606804214329522917382524296561295274823374483828323983651110722084223144007926678084087) /
    Integer(9195042623204647899565271327907071916397082689301388805795886223781949921278129819112624089473306486581983153439866384171645444456400131619437018878598534536108398238424609)
)

a = Integer(A.denominator() / 17)
assert A == u(Integer(5), a, 4 * a)

x, y = var("x, y")
assume([x > 0, y > 0])
sol = solve([
    U.denominator() * (x * (x ** 2 + y ** 2 + a) - y) == U.numerator() * (x ** 2 + y ** 2),
    V.denominator() * (y * (x ** 2 + y ** 2 - a) - x) == V.numerator() * (x ** 2 + y ** 2),
], x, y)

for x0, y0 in sol:
    # RuntimeError: no explicit roots found
    # TypeError: Unable to coerce x0 to an integer
    with contextlib.suppress(RuntimeError, TypeError):
        x0, y0 = Integer(x0.roots()[0][0]), Integer(y0.roots()[0][0])
        assert U == u(a, x0, y0)
        assert V == v(a, x0, y0)
        print((long_to_bytes(x0) + long_to_bytes(y0)).decode())