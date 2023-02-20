#mod3.py 저장
def baz():
    print("[mod3] baz()함수")

class Baz:
    pass

from ..import sub1
print(sub1)
from ..sub1.mod1 import foo
foo()

# from pkg2.sub1.mod1 import foo
# foo()