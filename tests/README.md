## Домашнее задание по тестированию

[Условие](https://github.com/siauPatrick/mai-python/blob/master/03-instrumenty-testirovaniya-v-python/issues.md)

Все проверки добавлены в [Github Actions](../.github/workflows/tests_hw.yml)  
Также проверяются все измененные файлы через Ruff с дефолтными правилами, которые включают в себя [все](https://docs.astral.sh/ruff/rules/#pyflakes-f) (или почти все) правила Flake8.

### Issue 1

Задание выполнено в файле [morse.py](./morse.py)  
Проверка doctest: `python -m doctest -o NORMALIZE_WHITESPACE -v morse.py`

### Issue 2

Задание выполнено в файле [issue2/test_morse.py](./issue2/test_morse.py)  
Проверка pytest: `pytest -v issue2/test_morse.py`

### Issue 3

Задание выполнено в файле [issue3/test_ohe_unittest.py](./issue3/test_ohe_unittest.py)  
Проверка unittest: `python -m unittest tests/issue3/test_ohe_unittest.py`

### Issue 4

Задание выполнено в файле [issue4/test_ohe_pytest.py](./issue4/test_ohe_pytest.py)  
Проверка pytest: `pytest -v tests/issue4/test_ohe_pytest.py`

### Issue 5

Задание выполнено в файле [issue5/test_year.py](./issue5/test_year.py)   
Проверка unittest: `python -m unittest tests/issue5/test_year.py`   
Проверка coverage (100% как нижний порог): `pytest tests/issue5 -q --cov=tests.what_is_year_now --cov-report term-missing --cov-fail-under=100`   
Coverage (trust_me.jpg, я не придумал, как вставить интерактивный coverage из html)   
И я исключил код из `__name__=='__main__'`, может потом придумаю как его протестировать    
<img width="601" alt="image" src="https://github.com/pyrogn/aaa/assets/60060559/31397dbc-a32c-402e-90ec-5a2c8cab615f">  

Как запускалась генерация html файла:  
`pytest tests/issue5 -q --cov=tests.what_is_year_now --cov-report html:tests/issue5/html_dir`
