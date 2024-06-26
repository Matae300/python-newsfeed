from flask import session, redirect
from functools import wraps

def login_required(func):
  @wraps(func)
  def wrapped_function(*args, **kwargs):
    print('wrapper')
    return func(*args, **kwargs)
  
  return wrapped_function

@login_required
def callback():
  print('hello')

callback() # prints 'wrapper', then 'hello'