import requests, time, os, subprocess, shutil, json
from instances import error, monokai, newlog, success, warning, info
from urllib.request import urlretrieve
import getpass
import pyzipper

version = requests.get('https://gist.githubusercontent.com/monokaiidev/ba04c8c3e1254560062c3a6f58a92897/raw/4c4613a2dc78ddeab171def3eb78b9ee2c22df60/gistfile1.txt').text.strip()
url = 'https://github.com/monokaiidev/vscode-patcher/releases/download/1/be5invis.vscode-custom-css-7.4.0.zip'
github_config1 = 'https://github.com/monokaiidev/vscode-patcher/releases/download/2/vscode-script.js'
github_config2 = 'https://github.com/monokaiidev/vscode-patcher/releases/download/3/custom-vscode.css'
filename = f'be5invis.vscode-custom-css-{version}.zip'
vscode_dir = os.path.expandvars(f"%USERPROFILE%\\.vscode\\extensions")
extracted_folder = f'be5invis.vscode-custom-css-{version}'
config_1 = 'vscode-script.js'
config_2 = 'custom-vscode.css'
user_config_dir = os.path.expandvars("%APPDATA%\\Code\\User")

settings_data = {
    "editor.copyWithSyntaxHighlighting": False,
    "diffEditor.ignoreTrimWhitespace": False,
    "editor.emptySelectionClipboard": False,
    "workbench.editor.enablePreview": False,
    "window.newWindowDimensions": "inherit",
    "editor.multiCursorModifier": "ctrlCmd",
    "files.trimTrailingWhitespace": True,
    "diffEditor.renderSideBySide": False,
    "editor.snippetSuggestions": "top",
    "editor.detectIndentation": False,
    "window.nativeFullScreen": True,
    "files.insertFinalNewline": True,
    "files.trimFinalNewlines": True,
    "workbench.editor.showTabs": "none",
    "editor.minimap.enabled": False,
    "editor.lineNumbers": "off",
    "editor.guides.indentation": False,
    "breadcrumbs.enabled": False,
    "scm.diffDecorations": "none",
    "editor.hover.delay": 1500,
    "editor.hover.enabled": True,
    "editor.matchBrackets": "never",
    "workbench.tips.enabled": False,
    "editor.colorDecorators": False,
    "git.decorations.enabled": False,
    "workbench.startupEditor": "none",
    "editor.lightbulb.enabled": "off",
    "editor.selectionHighlight": False,
    "editor.overviewRulerBorder": False,
    "editor.renderLineHighlight": "none",
    "editor.occurrencesHighlight": "off",
    "problems.decorations.enabled": False,
    "editor.renderControlCharacters": False,
    "editor.hideCursorInOverviewRuler": True,
    "editor.gotoLocation.multipleReferences": "goto",
    "editor.gotoLocation.multipleDefinitions": "goto",
    "editor.gotoLocation.multipleDeclarations": "goto",
    "workbench.editor.enablePreviewFromQuickOpen": False,
    "editor.gotoLocation.multipleImplementations": "goto",
    "editor.gotoLocation.multipleTypeDefinitions": "goto",
    "editor.fontFamily": "Geist Mono, JetBrains Mono, Fira Code",
    "editor.suggestFontSize": 16,
    "editor.suggestLineHeight": 30,
    "terminal.integrated.lineHeight": 1.5,
    "terminal.integrated.fontSize": 16,
    "search.useIgnoreFiles": False,
    "search.exclude": {
        "**/vendor/{[^l],?[^ai]}*": True,
        "**/public/{[^i],?[^n]}*": True,
        "**/node_modules": True,
        "**/dist": True,
        "**/_ide_helper.php": True,
        "**/composer.lock": True,
        "**/package-lock.json": True,
        "storage": True,
        ".phpunit.result.cache": True
    },
    "editor.wordSeparators": "`~!@#%^&*()=+[{]}\\|;:'\",.<>/?",
    "emmet.includeLanguages": {
        "blade": "html",
        "vue-html": "html",
        "vue": "html",
        "react": "html",
        "javascript": "html"
    },
    "files.associations": {
        ".php_cs": "php",
        ".php_cs.dist": "php"
    },
    "php.suggest.basic": False,
    "[javascript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True
    },
    "[typescriptreact]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True
    },
    "[tailwindcss]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True
    },
    "[vue]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True
    },
    "[javascriptreact]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True
    },
    "prettier.requireConfig": True,
    "prettier.useEditorConfig": False,
    "explorer.sortOrder": "type",
    "prettier.tabWidth": 4,
    "vetur.format.options.tabSize": 4,
    "workbench.tree.indent": 15,
    "[html]": {
        "editor.defaultFormatter": "apility.beautify-blade",
        "editor.formatOnSave": True
    },
    "editor.wordWrapColumn": 120,
    "files.autoSave": "afterDelay",
    "[css]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True
    },
    "editor.quickSuggestions": {
        "strings": True
    },
    "[jsonc]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "[json]": {
        "editor.defaultFormatter": "vscode.json-language-features"
    },
    "security.workspace.trust.untrustedFiles": "open",
    "editor.linkedEditing": True,
    "editor.formatOnSave": False,
    "editor.fontLigatures": "'ss01', 'ss02', 'ss03', 'ss04', 'ss05', 'ss06', 'ss07', 'ss08', 'calt', 'dlig'",
    "diffEditor.wordWrap": "on",
    "notebook.output.wordWrap": True,
    "editor.fontSize": 16,
    "editor.minimap.maxColumn": 250,
    "codesnap.containerPadding": "8em",
    "codesnap.boxShadow": "rgba(0, 0, 0, 0.55) 0px 12px 24px",
    "explorer.confirmDelete": False,
    "editor.accessibilitySupport": "off",
    "chat.editor.wordWrap": "on",
    "editor.wordWrap": "wordWrapColumn",
    "[php]": {
        "editor.defaultFormatter": "bmewburn.vscode-intelephense-client"
    },
    "tailwindCSS.includeLanguages": {
        "plaintext": "html"
    },
    "tailwindCSS.experimental.configFile": None,
    "editor.fontWeight": "400",
    "workbench.statusBar.visible": False,
    "editor.inlineSuggest.suppressSuggestions": True,
    "codesnap.backgroundColor": "#FFC540",
    "codesnap.showLineNumbers": False,
    "codesnap.roundedCorners": True,
    "editor.padding.top": 16,
    "editor.cursorBlinking": "phase",
    "editor.stickyScroll.enabled": False,
    "editor.lineHeight": 32,
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
              "scope": [
                "comment",
                "keyword",
                "variable.language",
                "entity.other.attribute-name.html",
                "entity.other.attribute-name",
                "keyword.control",
                "storage.type",
                "comment",
                "comment.block",
                "comment.line"
              ],
              "settings": {
                "fontStyle": ""
              }
            }
          ]
    },
    "material-icon-theme.saturation": 0,
    "vscode_custom_css.imports": [
        f"file:///C:/Users/{getpass.getuser()}/.vscode/extensions/custom-vscode.css",
        f"file:///C:/Users/{getpass.getuser()}/.vscode/extensions/vscode-script.js"
    ],
    "workbench.colorTheme": "Default Dark Modern",
    "workbench.iconTheme": "eq-material-theme-icons-light",
    "workbench.sideBar.location": "right",
    "material-icon-theme.files.color": "#42a5f5",
    "workbench.tree.enableStickyScroll": False,
    "workbench.activityBar.location": "hidden",
    "editor.cursorSmoothCaretAnimation": "on",
    "tabnine.experimentalAutoImports": True
}
monokai("Welcome to Monokai's VSCode Patcher! Press 1 to continue and download everything.")
# requests.post(webhook_url, data={"content": "Someone ran your script! :blush:"})
this_input = input("> ")

if this_input == '1':
    if os.path.isdir(vscode_dir):
        info("VSCode exists...")
        time.sleep(1)
    else:
        error("No VSCode found! Please install VSCode and try again.")
    os.system("cls")
    info("Downloading file...")
    urlretrieve(url, filename)
    success("Download complete!")

    def move_files_to_vscode(source_dir, destination_dir):
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            destination_path = os.path.join(destination_dir, item)

            if os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
            else:
                shutil.copy2(source_path, destination_path)
            success(f"Installed files to VSCode Directory: %s" % source_path)

    def move_file_to_vscode(source, destination_dir):
        shutil.copy(source, os.path.join(destination_dir, os.path.basename(source)))
        success(f"Installed file to VSCode directory")

    def extract_files_from_zip(zip_file, extraction_dir):
        with pyzipper.AESZipFile(zip_file, "r") as zf:
            zf.extractall(extraction_dir)
        success("Extraction complete!")

    def remove(file):
        os.remove(file)

    info("Extracting files from zip...")
    extract_files_from_zip(filename, extracted_folder)

    move_files_to_vscode(extracted_folder, vscode_dir)

    urlretrieve(github_config1, config_1)
    urlretrieve(github_config2, config_2)
    move_file_to_vscode(config_1, vscode_dir)
    move_file_to_vscode(config_2, vscode_dir)

    settings_file_path = os.path.join(user_config_dir, "settings.json")
    if os.path.exists(settings_file_path):
        os.remove(settings_file_path)
    with open(settings_file_path, "w") as file:
        json.dump(settings_data, file, indent=4)
    success("VSCode configuration update complete!")
    info("Please restart your VSCode, then press CTRL + Shift + P, then search for Reload Custom CSS and JS and press it.\nYou will get a box at the bottom left asking you to click it, then click it. And know, you will have a beautiful VSCode! Happy Coding!")
else:
    exit(1)
