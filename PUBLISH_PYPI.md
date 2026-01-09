# Publishing `pic-standard` to PyPI (Release Checklist)

This guide publishes the Python package and tags a matching GitHub release.

---

## 0) Pre-flight checklist

- [ ] CI is green on `main`
- [ ] `pyproject.toml` has the correct `name` and `version`
- [ ] `CHANGELOG.md` includes an entry for the version you’re shipping
- [ ] `README.md` includes the Quickstart commands (`pip install pic-standard`, `pic-cli verify ...`)

---

## 1) Clean build locally

From repo root:

```bash
python -m pip install --upgrade pip
pip install build twine
```

Build artifacts:

```bash
python -m build
```

You should see:

- `dist/pic_standard-<version>-py3-none-any.whl`
- `dist/pic-standard-<version>.tar.gz`

---

## 2) Test install locally (recommended)

Install the wheel you just built:

```bash
pip install dist/pic_standard-*.whl
```

Run:

```bash
pic-cli verify examples/financial_irreversible.json
```

Expected output:

```text
✅ Schema valid
✅ Verifier passed
```

---

## 3) Publish to TestPyPI first (strongly recommended)

Create a TestPyPI account:
https://test.pypi.org/account/register/

Upload:

```bash
twine upload --repository testpypi dist/*
```

Install from TestPyPI:

```bash
pip install -i https://test.pypi.org/simple/ pic-standard
```

Run:

```bash
pic-cli verify examples/financial_irreversible.json
```

If it works, proceed to real PyPI.

---

## 4) Publish to real PyPI

Create a PyPI account:
https://pypi.org/account/register/

Upload:

```bash
twine upload dist/*
```

Verify install:

```bash
pip install pic-standard
pic-cli verify examples/financial_irreversible.json
```

---

## 5) Tag and push a GitHub release

Make sure your repo is committed:

```bash
git add README.md CHANGELOG.md pyproject.toml
git commit -m "Release <version>"
```

Tag:

```bash
git tag v<version>
git push origin main --tags
```

Then on GitHub:
- Go to **Releases**
- Click **Draft a new release**
- Select tag `v<version>`
- Title: `v<version>`
- Paste release notes from `CHANGELOG.md`

---

## 6) Notes on versioning

- Bump `version` in `pyproject.toml`
- Add an entry in `CHANGELOG.md`
- Repeat the steps above for the next release
