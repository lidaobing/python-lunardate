# python-lunardate

## 项目结构

单文件库，唯一源码是 `lunardate.py`，无 `src/` 目录，无 `__init__.py`。

- setup.py 使用 `py_modules = ['lunardate']`（不是 `packages=`）
- 无 requirements.txt，零外部依赖（纯标准库）
- 兼容 Python 3.7+

## 测试

所有测试是 `lunardate.py` 中的 doctest，无第三方测试框架：

```bash
python lunardate.py -v
```

CI 中运行方式同上。

## Lint & 类型检查

```bash
flake8 . --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
mypy lunardate.py
```

## 限制

农历仅支持 1900–2099 年。

## 公共 API

仅 `LunarDate` 类。关键方法：

- `LunarDate(year, month, day, is_leap_month=False)` — 构造农历日期
- `LunarDate.from_solar_date(year, month, day)` — 公历转农历
- `LunarDate.to_solar_date()` — 农历转公历
- `LunarDate.today()` — 当前农历日期
- `LunarDate.leap_month_for_year(year)` — 获取某年闰月（无闰月返回 None）
