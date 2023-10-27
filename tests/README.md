## Домашка по тестированию

[Условие](https://github.com/siauPatrick/mai-python/blob/master/03-instrumenty-testirovaniya-v-python/issues.md)

Все проверки добавлены в [Github Actions](../.github/workflows/tests_hw.yml)  
Также проверяются все измененные файлы через Ruff с дефолтными правилами, которые включают в себя все (или почти все) правила Flake8.

### Issue 1
Задание выполнено в файле [morse.py](./morse.py)  
Проверка doctest: `python -m doctest -o NORMALIZE_WHITESPACE -v morse.py`

### Issue 2

Задание выполнено в файле [issue2/test_morse.py](./issue2/test_morse.py)  
Проверка pytest: `pytest -v issue2/test_morse.py`

### Issue 3

### Issue 4

### Issue 5
