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
