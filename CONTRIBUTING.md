# Contributing to barre

## Development

1. Fork and clone:
```bash
git clone https://github.com/FeelTheFonk/barre.git
cd barre
```

2. Create a branch:
```bash
git checkout -b feature-name
```

3. Make changes and test:
```bash
python -c "from barre import b; list(b(range(10)))"
```

## Pull Request Process

1. Update documentation
2. Follow commit convention:
   - `feat:` New features
   - `fix:` Bug fixes
   - `docs:` Documentation
   - `style:` Code style
   - `refactor:` Code refactoring
   - `perf:` Performance
   - `test:` Tests
   - `chore:` Maintenance

3. Create PR against `main` branch

## Code Style
- Keep it minimal
- No dependencies
- PEP 8 compliant
- Maintain <1KB size

## Testing
Run basic test:
```python
from barre import b
assert list(b(range(3))) == [0,1,2]
```