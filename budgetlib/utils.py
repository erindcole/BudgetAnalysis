from functools import wraps

def init_dec(fn):
  """
  genric coroutine initializer
  """
  @wraps(fn)
  def inner(*args, **kw):
    start = fn(*args, **kw)
    next(start)
    return start
  return inner

def is_tuple(x):
  return type(x) is tuple

def expected_len(x, n):
  return len(x) == n
