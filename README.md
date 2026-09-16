# 星言 (XingYan) - Morse Code Translator

<div align="center">

✨ **摩斯密码翻译器** — 支持自定义"迷语"对照表 ✨

[![Build APK](https://github.com/user/repo/actions/workflows/build-apk.yml/badge.svg)](../../actions/workflows/build-apk.yml)

</div>

## 📱 功能特性

| 功能 | 说明 |
|------|------|
| 📋 **对照表管理** | 支持导入 `.json` / `.xlsx` 对照表文件，内置默认表 |
| 🔤 **文本 → 迷语** | 将英文字母/数字翻译为"迷语"编码 |
| 🔠 **迷语 → 文本** | 将"迷语"编码翻译回字母/数字 |
| 🈶 **中文 → 拼音 → 迷语** | 自动将中文转为拼音，再编码为迷语 |
| ✨ **精美界面** | 深色星空主题，贴合"星言"品牌调性 |

## 📐 编码规则

- **迷** = 短信号（滴）
- **~** = 长信号（嗒）
- **字符间**：1 个空格
- **单词间**：2 个空格

### 示例

```
输入:  LOVE YOU
输出: 迷~迷迷 ~~~ 迷迷迷~ 迷  ~迷~~ ~~~ 迷迷~

输入: 迷~迷迷 ~~~ 迷迷迷~ 迷  ~迷~~ ~~~ 迷迷~
输出: LOVE YOU
```

## 🚀 快速开始（开发者）

### 本地运行（需要 Kivy 环境）

```bash
pip install kivy pypinyin openpyxl
python main.py
```

### 构建 APK（自动 via GitHub Actions）

1. Fork 本仓库
2. Push 到 `main` 分支
3. GitHub Actions 自动构建 APK
4. 在 Actions 页面下载 Artifact

> 也可以在 **Releases** 页面下载正式版本。

## 📂 对照表格式

### JSON 格式
```json
{
  "A": "迷~",
  "B": "~迷迷迷",
  ...
}
```

### XLSX 格式
| 字符 | 迷语 |
|------|------|
| A | 迷~ |
| B | ~迷迷迷 |

## 🛠️ 技术栈

- **Framework**: Kivy 2.x
- **Language**: Python 3.10+
- **拼音**: pypinyin
- **Excel**: openpyxl
- **Build**: Buildozer → GitHub Actions

## 📄 License

MIT License
