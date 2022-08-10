'''
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

'''
class greet:
    def __init__(self):
        pass
    def hello(self,name):
        return print(f'Hello {name}!')

if __name__ == "__main__":
    sunil = greet()
    sunil.hello('Sunil')