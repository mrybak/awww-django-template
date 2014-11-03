AWWW exams starter kit*
====================

### Includes (most up-to-date versions if not stated otherwise):
- jQuery & jQuery UI (datepicker etc.)
- Twitter Bootstrap 
- Django with admin enabled
- example of a simple model
- example of a simple view (accessible at `/zadanie/index`)
- a simple base template (`base.html`), ready to be extended
- logging to a file (see `models.py`)

### Recommended usage:
0. `DIR_NAME` is directory where you've cloned this repo.
1. Create virtual environment: `virtualenv --no-site-packages DIR_NAME`
2. Do 
  - `cd DIR_NAME`
  - `. bin/activate`
  - `pip install django`  
3. Open PyCharm, go to `File -> Open Directory -> DIR_NAME -> Alt-4`  
*If you don't have PyCharm, get it. There are free trial versions as well as academic licenses.*
*It has a lot of nice features, for example lets you download jQuery documentation, which is the only way to legally use it during the exam.*
4. Go to `Settings` (or `Ctrl+Alt+S`), search for `Python interpreters` and add `Local` from virtualenv created in step 1
5. In `settings.py` supply correct absolute/relative path to database file (`db.sqlite`) and logfile (`zadanie.log`). 
6. If needed:  
  - `chmod 700 manage.py`
  - `python manage.py syncdb`

*\* Disclaimer:*
*Using this template is **officially allowed by professors**. I am not responsible for any technical or other problems caused by using this template. *