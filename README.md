# CSS Extractor

A Python tool that automatically extracts inline CSS from HTML files into separate CSS files, creating a cleaner and more maintainable codebase. Perfect for static websites and GitHub Pages projects.

## Author
Mohd Mahmodi  
GitHub: [MohdYahyaMahmodi/CSS-Hash-Manager](https://github.com/MohdYahyaMahmodi/CSS-Hash-Manager)

## Features

- 📂 Automatically creates a `css` directory for organization
- 🔄 Extracts inline CSS from `<style>` tags into separate CSS files
- 🔗 Updates HTML files with proper `<link>` tags
- 🔒 Implements cache busting with version parameters
- 🛠️ Processes multiple HTML files in one command
- 💪 Maintains CSS content integrity during extraction
- ⚡ Supports UTF-8 encoding

## Why Use CSS Extractor?

1. **Better Organization**: Separates CSS from HTML for cleaner code structure
2. **Improved Maintainability**: Easier to update styles when they're in separate files
3. **Cache Control**: Built-in versioning helps manage browser caching
4. **Development Workflow**: Perfect for converting legacy inline styles to external stylesheets
5. **Multiple File Support**: Process entire websites in one command

## Prerequisites

- Python 3.6 or higher
- BeautifulSoup4 library

Install required dependency:
```bash
pip install beautifulsoup4
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MohdYahyaMahmodi/CSS-Hash-Manager.git
cd CSS-Hash-Manager
```

2. Make sure you have BeautifulSoup4 installed:
```bash
pip install beautifulsoup4
```

## Usage

Basic usage:
```bash
python css_extractor.py file1.html file2.html file3.html
```

Example:
```bash
python css_extractor.py index.html about.html contact.html
```

## How It Works

1. **Directory Creation**: Creates a `css` directory if it doesn't exist
2. **File Processing**: For each HTML file:
   - Extracts CSS from `<style>` tags
   - Creates corresponding CSS file in the `css` directory
   - Removes the original `<style>` tag
   - Adds a `<link>` tag with versioning parameter
3. **Version Control**: Adds `?v=1.0.0` to CSS links for cache control

## Example

### Before (index.html):
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background: #f0f0f0;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
```
## Demo Files

For your convenience, this repository includes demo HTML files to test the extractor:

### demo.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Extractor Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        h1 {
            color: #333;
            text-align: center;
        }

        .card {
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>CSS Extractor Demo</h1>
        <div class="card">
            <h2>This is a demo page</h2>
            <p>Run the extractor to move the CSS to a separate file!</p>
        </div>
    </div>
</body>
</html>
```

### about.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Page</title>
    <style>
        body {
            font-family: 'Helvetica', sans-serif;
            background: #2c3e50;
            color: white;
            padding: 30px;
        }

        .about-section {
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }

        h1 {
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="about-section">
        <h1>About Us</h1>
        <p>This is another demo page with different styles.</p>
    </div>
</body>
</html>
```

Try the extractor with these demo files:
```bash
python css_extractor.py demo.html
```

This will create the CSS files and update the HTML files automatically, giving you a practical example of how the tool works.

### After Running:
```bash
python css_extractor.py index.html
```

#### Generated Structure:
```
your-project/
├── css/
│   └── index.css
└── index.html
```

#### Modified index.html:
```html
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>
   CSS Extractor Demo
  </title>
  <link href="css/demo.css?v=1.0.0" rel="stylesheet"/>
 </head>
 <body>
  <div class="container">
   <h1>
    CSS Extractor Demo
   </h1>
   <div class="card">
    <h2>
     This is a demo page
    </h2>
    <p>
     Run the extractor to move the CSS to a separate file!
    </p>
   </div>
  </div>
 </body>
</html>

```

#### Generated css/index.css:
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f0f0f0;
}

.container {
    max-width: 800px;
    margin: 0 auto;
}
    
h1 {
    color: #333;
    text-align: center;
}

.card {
    background: white;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

## Cache Busting

When you update your CSS, simply change the version number in the link tag:
```html
<link href="css/styles.css?v=1.0.0" rel="stylesheet"/>
<!-- After CSS update -->
<link href="css/styles.css?v=1.0.1" rel="stylesheet"/>
```

## Error Handling

The script includes comprehensive error handling:
- Checks for missing HTML files
- Validates presence of `<style>` tags
- Ensures proper HTML structure with `<head>` tag
- UTF-8 encoding support for international characters

## Best Practices

1. **Backup**: Always backup your HTML files before running the script
2. **Version Control**: Commit your changes before running on multiple files
3. **Testing**: Test the script on a single file before processing multiple files
4. **Maintenance**: Increment version numbers when updating CSS

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please:
1. Check existing GitHub issues
2. Create a new issue with a detailed description
3. Include example HTML that demonstrates the problem

## Acknowledgments

- BeautifulSoup4 library for HTML processing
- Python community for feedback and suggestions
- All contributors and users of this tool

---
Made with ❤️ by [Mohd Mahmodi](https://github.com/MohdYahyaMahmodi)