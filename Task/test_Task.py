import sys
import pytest


@pytest.mark.skip(reason="Баг в продукте - <ссылка>")
def test_one(): # Это наш тест, который находит тот самый баг
    pass


@pytest.mark.skipif(sys.version_info < (3, 6), reason="Тест требует python версии 3.6 или выше")
def test_python36_and_greater():
    pass


@pytest.mark.xfail
def test_flaky():
    assert 1 == 2

@pytest.mark.xfail(sys.platform == "win32", reason="Ошибка в системной библиотеке") # На платформе Windows ожидаем, что тест будет падать
def test_not_for_windows():
    pass

c
@pytest.mark.xfail(raises=RuntimeError)
def test_x_status_runtime_only():
    pass


