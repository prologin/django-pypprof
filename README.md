django-pypprof
===================

`django-pypprof` is a wrapper of
[pypprof](https://github.com/timpalpant/pypprof) for ease of use with Django.

### Installation

Install the package:

```sh
pip install django-pypprof --extra-index-url https://gitlab.com/api/v4/projects/36832129/packages/pypi/simple
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
  ...
  "django_pypprof",
  ...
]
```

Add the urls to your `urls.py`:

```python
urlpatterns = [
  ...
  path("debug/pprof/", include("django_pypprof.urls")),
  ...
]
```

### Configuration

You can configure the sample rate of `mprofile` by adding the following setting:

```python
PPROF_SAMPLE_RATE = 128 * 1024 # the default
```
