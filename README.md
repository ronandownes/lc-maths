# Leaving Certificate Mathematics - Ordinary Level

PreTeXt textbook for LC Mathematics (Ordinary Level) aligned with the Irish curriculum.

## Project Structure

- `source/` - PreTeXt source files organized by curriculum strand
- `assets/` - Images and other static assets
- `generated-assets/` - Auto-generated images (LaTeX, TikZ, etc.)
- `publication/` - Publication configuration files
- `output/` - Built HTML and PDF output

## Building the Book

### Build HTML
```bash
python -m pretext build web
```

### Build PDF
```bash
python -m pretext build print
```

### View HTML locally
```bash
python -m pretext view web
```

## Curriculum Strands

1. **Statistics and Probability** - 7 sections covering counting, probability concepts, data analysis
2. **Geometry and Trigonometry** - 4 sections covering synthetic geometry, coordinate geometry, trig, transformations
3. **Number** - 4 sections covering number systems, sequences, indices, arithmetic, measurement
4. **Algebra** - 3 sections covering expressions, equations, inequalities
5. **Functions** - 2 sections covering functions and calculus

## Author

Mr Ronan Downes

## License

[Add your license here]
