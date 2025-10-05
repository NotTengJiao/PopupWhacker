### 1. `README_CN.md`

```markdown
# PopupWhacker - 开机弹窗终结者

![PopupWhacker](https://img.shields.io/badge/Windows-10%2B-brightgreen?logo=windows) ![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)

一款专为Windows系统设计的轻量级脚本，可自动关闭开机时不会最小化的应用弹窗。

[View English Documentation](README.md)

## 🔧 主要功能

- 基于**模糊标题匹配**自动关闭弹窗
- 后台静默运行
- 通过纯文本文件配置规则
- **支持正则表达式**

## 🛠️ 安装指南

1. **安装依赖库**：
   ```bash
   pip install pywinauto
   ```

2. **配置规则文件**：
   - 第一次运行会在同级目录自动创建 `titles.txt`
     ```
     Microsoft Teams
     WhatsApp
     Adobe Reader
     ```
   - 保存并关闭记事本后，再次运行脚本即可生效

## ⚙️ 使用方法

### 1. 手动测试运行
```powershell
PopupWhacker.pyw
```

### 2. 设置开机启动（推荐）
1. 打开 **任务计划程序**（运行 `taskschd.msc`）
2. 创建基本任务：
   - **触发器**：用户登录时
   - **操作**：启动程序
   - **程序/脚本**：选择 `PopupWhacker.pyw`
   - **起始于**：填写脚本所在目录（例如：`C:\Tools\PopupWhacker`）
3. 勾选"使用最高权限运行"
4. 保存任务

## 🔍 模糊匹配机制

脚本使用正则表达式进行智能匹配：
- **大小写不敏感**（`teams` 匹配 `Microsoft Teams`）
- **支持正则表达式**（`^Teams` 匹配 `Teams Meeting`）
- 自动转义特殊字符（避免正则错误）
- 部分匹配（`Teams` 匹配 `Microsoft Teams`）

## 📝 示例规则文件
```
Teams
Edge
^Teams
```

将关闭以下窗口：
- 包含 "Teams" 的窗口（如 `Microsoft Teams`）
- 包含 "Edge" 的窗口（如 `Microsoft Edge`）
- 以 "Teams" 开头的窗口（如 `Teams Meeting`）

## 📁 目录结构示例
```
PopupWhacker/
├── PopupWhacker.pyw
├── titles.txt        # 添加需要关闭的窗口标题（支持正则）
└── README.md
```

## ⚠️ 注意事项

- **必须以管理员权限运行**（窗口自动化所需）
- 适用于 **Windows 10/11**
- 不处理已最小化的窗口

## 📜 开源协议

MIT License

---

> 专为讨厌开机弹窗的Windows用户而生 ❤️