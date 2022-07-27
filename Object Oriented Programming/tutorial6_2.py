import tutorial6
from tutorial6 import NotPrivate

test = NotPrivate('tim')
test.display()
# As you can see, we can still use the private function but it is a private function.
test._display()