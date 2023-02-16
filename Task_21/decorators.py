# def do_twice(func):
#     def wrapper():
#         func()
#         func()
#     return wrapper


# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper

import functools


def do_twice(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
      func(*args, **kwargs)
      return func(*args, **kwargs)
  return wrapper

# import functools

# def debug(func):
#     """Выводит сигнатуру функции и возвращаемое значение"""
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Вызываем {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__} вернула значение - {value}")
#         return value
#     return wrapper_debug

