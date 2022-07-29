# Optional Parameters.

def func(word, add=5, freq=1):
    print(word * (freq+add))

func('tim')
func('dogshit ', 0)

# If you want to change frequency to some other value but want to keep add to default value, you cant actually do that
# Without giving add a value.
# So, the most used optional parameters should be placed first.